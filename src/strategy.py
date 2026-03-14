from __future__ import annotations

from dataclasses import dataclass

from game_state import GameConfig, Point, TurnState

DIRECTION_VECTORS: dict[str, tuple[int, int]] = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0),
}

DEFAULT_DIRECTION_ORDER: tuple[str, ...] = ("UP", "RIGHT", "DOWN", "LEFT")


@dataclass(slots=True)
class StrategyMemory:
    last_direction_by_id: dict[int, str]


def in_bounds(point: Point, width: int, height: int) -> bool:
    return 0 <= point.x < width and 0 <= point.y < height


def manhattan(a: Point, b: Point) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


def horizontal_direction(dx: int) -> str:
    return "RIGHT" if dx > 0 else "LEFT"


def vertical_direction(dy: int) -> str:
    return "DOWN" if dy > 0 else "UP"


def dedupe_directions(candidates: list[str]) -> list[str]:
    deduped: list[str] = []
    for direction in candidates:
        if direction not in deduped:
            deduped.append(direction)
    return deduped


def nearest_power_source(head: Point, power_sources: tuple[Point, ...]) -> Point | None:
    if not power_sources:
        return None
    return min(power_sources, key=lambda pos: manhattan(head, pos))


def build_preferred_directions(head: Point, target: Point | None, last_direction: str) -> list[str]:
    ordered: list[str] = []

    if target is not None:
        dx = target.x - head.x
        dy = target.y - head.y

        if abs(dx) >= abs(dy) and dx != 0:
            ordered.append(horizontal_direction(dx))
        if dy != 0:
            ordered.append(vertical_direction(dy))
        if abs(dy) > abs(dx) and dy != 0:
            ordered.insert(0, vertical_direction(dy))
        horizontal = horizontal_direction(dx) if dx != 0 else None
        if horizontal is not None and horizontal not in ordered:
            ordered.append(horizontal)

    ordered.append(last_direction)
    ordered.extend(DEFAULT_DIRECTION_ORDER)
    return dedupe_directions(ordered)


def build_blocked_cells(config: GameConfig, turn_state: TurnState) -> set[Point]:
    blocked: set[Point] = set(config.platforms)
    for snakebot in turn_state.snakebots.values():
        blocked.update(snakebot.body)
    return blocked


def choose_direction(
    head: Point,
    preferred_directions: list[str],
    blocked_cells: set[Point],
    width: int,
    height: int,
) -> str:
    for direction in preferred_directions:
        dx, dy = DIRECTION_VECTORS[direction]
        nxt = Point(x=head.x + dx, y=head.y + dy)
        if in_bounds(nxt, width, height) and nxt not in blocked_cells:
            return direction

    for direction in DEFAULT_DIRECTION_ORDER:
        dx, dy = DIRECTION_VECTORS[direction]
        nxt = Point(x=head.x + dx, y=head.y + dy)
        if in_bounds(nxt, width, height):
            return direction

    return "UP"


def choose_actions(config: GameConfig, turn_state: TurnState, memory: StrategyMemory) -> str:
    alive_my_snake_ids = [
        snake_id for snake_id in config.my_snake_ids if snake_id in turn_state.snakebots
    ]
    if not alive_my_snake_ids:
        return "WAIT"

    blocked_cells = build_blocked_cells(config, turn_state)
    actions: list[str] = []

    for snake_id in alive_my_snake_ids:
        snakebot = turn_state.snakebots[snake_id]
        if not snakebot.body:
            continue

        head = snakebot.body[0]
        target = nearest_power_source(head, turn_state.power_sources)
        last_direction = memory.last_direction_by_id.get(snake_id, "UP")
        preferred_directions = build_preferred_directions(head, target, last_direction)
        chosen_direction = choose_direction(
            head=head,
            preferred_directions=preferred_directions,
            blocked_cells=blocked_cells,
            width=config.width,
            height=config.height,
        )
        memory.last_direction_by_id[snake_id] = chosen_direction
        actions.append(f"{snake_id} {chosen_direction}")

    if not actions:
        return "WAIT"
    return ";".join(actions)
