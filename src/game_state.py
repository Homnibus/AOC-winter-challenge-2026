from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Point:
    x: int
    y: int


@dataclass(slots=True)
class Snakebot:
    snakebot_id: int
    body: tuple[Point, ...]


Body = tuple[Point, ...]


@dataclass(slots=True)
class GameConfig:
    my_id: int
    width: int
    height: int
    platforms: frozenset[Point]
    my_snake_ids: tuple[int, ...]
    enemy_snake_ids: tuple[int, ...]


@dataclass(slots=True)
class TurnState:
    turn: int
    power_sources: tuple[Point, ...]
    snakebots: dict[int, Snakebot]


def parse_point(raw: str) -> Point:
    x_str, y_str = raw.split(",")
    return Point(x=int(x_str), y=int(y_str))


def parse_body(raw: str) -> Body:
    if not raw:
        return ()
    return tuple(parse_point(part) for part in raw.split(":"))


def iter_points_from_grid(grid_lines: Iterable[str]) -> frozenset[Point]:
    points: set[Point] = set()
    for y, line in enumerate(grid_lines):
        for x, char in enumerate(line):
            if char == "#":
                points.add(Point(x=x, y=y))
    return frozenset(points)
