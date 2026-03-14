from __future__ import annotations

import sys

from game_state import GameConfig, Point, Snakebot, TurnState, iter_points_from_grid, parse_body
from strategy import StrategyMemory, choose_actions


def read_required_line() -> str:
    line = sys.stdin.readline()
    if not line:
        raise EOFError("Unexpected EOF while reading required input line")
    return line.rstrip("\n")


def read_required_int() -> int:
    return int(read_required_line())


def read_init() -> GameConfig:
    my_id = read_required_int()
    width = read_required_int()
    height = read_required_int()

    grid_lines = [read_required_line() for _ in range(height)]
    platforms = iter_points_from_grid(grid_lines)

    snakebots_per_player = read_required_int()
    my_snake_ids = tuple(read_required_int() for _ in range(snakebots_per_player))
    enemy_snake_ids = tuple(read_required_int() for _ in range(snakebots_per_player))

    return GameConfig(
        my_id=my_id,
        width=width,
        height=height,
        platforms=platforms,
        my_snake_ids=my_snake_ids,
        enemy_snake_ids=enemy_snake_ids,
    )


def read_turn(turn: int) -> TurnState | None:
    line = sys.stdin.readline()
    if not line:
        return None
    line = line.strip()
    if not line:
        return None

    power_source_count = int(line)
    power_sources = tuple(
        Point(*map(int, read_required_line().split())) for _ in range(power_source_count)
    )

    snakebot_count = read_required_int()
    snakebots: dict[int, Snakebot] = {}
    for _ in range(snakebot_count):
        snake_id_str, body_str = read_required_line().split()
        snake_id = int(snake_id_str)
        body = parse_body(body_str)
        snakebots[snake_id] = Snakebot(snakebot_id=snake_id, body=body)

    return TurnState(turn=turn, power_sources=power_sources, snakebots=snakebots)


def main() -> None:
    config = read_init()
    memory = StrategyMemory(last_direction_by_id={})
    turn = 0

    while True:
        state = read_turn(turn)
        if state is None:
            break

        print(choose_actions(config, state, memory), flush=True)
        turn += 1


if __name__ == "__main__":
    main()
