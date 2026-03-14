from game_state import GameConfig, Point, Snakebot, TurnState
from strategy import StrategyMemory, choose_actions


def make_config() -> GameConfig:
    return GameConfig(
        my_id=0,
        width=10,
        height=8,
        platforms=frozenset(),
        my_snake_ids=(1,),
        enemy_snake_ids=(2,),
    )


def test_choose_actions_targets_nearest_power_source() -> None:
    config = make_config()
    turn_state = TurnState(
        turn=0,
        power_sources=(Point(3, 1),),
        snakebots={
            1: Snakebot(snakebot_id=1, body=(Point(1, 1), Point(1, 2), Point(1, 3))),
        },
    )
    memory = StrategyMemory(last_direction_by_id={})

    action = choose_actions(config, turn_state, memory)

    assert action == "1 RIGHT"


def test_choose_actions_wait_if_no_alive_snake() -> None:
    config = make_config()
    turn_state = TurnState(turn=0, power_sources=(Point(3, 1),), snakebots={})
    memory = StrategyMemory(last_direction_by_id={})

    action = choose_actions(config, turn_state, memory)

    assert action == "WAIT"


def test_choose_actions_avoids_blocked_preferred_cell() -> None:
    config = GameConfig(
        my_id=0,
        width=10,
        height=8,
        platforms=frozenset({Point(1, 0)}),
        my_snake_ids=(1,),
        enemy_snake_ids=(2,),
    )
    turn_state = TurnState(
        turn=0,
        power_sources=(Point(1, 0),),
        snakebots={
            1: Snakebot(snakebot_id=1, body=(Point(1, 1), Point(1, 2), Point(1, 3))),
        },
    )
    memory = StrategyMemory(last_direction_by_id={})

    action = choose_actions(config, turn_state, memory)

    assert action == "1 RIGHT"


def test_choose_actions_returns_direction_when_boxed_in() -> None:
    config = GameConfig(
        my_id=0,
        width=3,
        height=3,
        platforms=frozenset({Point(1, 0), Point(0, 1)}),
        my_snake_ids=(1,),
        enemy_snake_ids=(),
    )
    turn_state = TurnState(
        turn=0,
        power_sources=(),
        snakebots={1: Snakebot(snakebot_id=1, body=(Point(0, 0),))},
    )
    memory = StrategyMemory(last_direction_by_id={})

    action = choose_actions(config, turn_state, memory)

    assert action.startswith("1 ")
