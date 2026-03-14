from game_state import Point, iter_points_from_grid, parse_body


def test_parse_body_reads_head_first() -> None:
    body = parse_body("0,1:1,1:2,1")

    assert body == (Point(0, 1), Point(1, 1), Point(2, 1))


def test_parse_body_empty_returns_empty_tuple() -> None:
    assert parse_body("") == ()


def test_iter_points_from_grid_extracts_platforms() -> None:
    grid = [
        "..#.",
        "#...",
    ]

    platforms = iter_points_from_grid(grid)

    assert Point(2, 0) in platforms
    assert Point(0, 1) in platforms
    assert Point(1, 0) not in platforms
