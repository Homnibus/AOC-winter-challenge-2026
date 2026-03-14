# Winter Challenge 2026 - Rules Summary

## Goal

Collect energy to grow snakebots and finish with more total body segments than opponent.

## Core Mechanics

- Grid with platform cells (`#`) and free cells (`.`).
- Snakebots are made of adjacent body segments; first segment is head.
- Gravity applies after movement resolution: snakebots fall until at least one segment is supported.
- Solid cells include: platforms, snakebot bodies, and energy cells.

## Movement

- Snakebots keep moving in previous direction unless commanded.
- Initial direction is `UP`.
- Movement and collisions are resolved simultaneously for all snakebots.

### Collision outcomes

1. Head enters platform/body:

- If snake has at least 3 segments remaining after head destruction: remove head, next segment becomes head.
- Otherwise snakebot is removed.

2. Head enters energy:

- Snake grows by one segment at tail.
- Energy disappears and is no longer solid.

Special case:

- If multiple heads enter same energy cell simultaneously, all are considered to have eaten it.

Out-of-bounds:

- Extension beyond map bounds can happen during growth logic, but falling outside play area removes snakebot.

## Actions

At least one action per turn. Actions separated by `;`.

- `<id> UP|DOWN|LEFT|RIGHT` (optional debug text after direction)
- `MARK x y` (up to 4 markers/turn)
- `WAIT`

## End Conditions

Game ends at end of turn if:

- One player has no snakebots left, or
- No energy remains, or
- 200 turns elapsed.

## I/O Protocol

### Init

1. `myId`
2. `width`
3. `height`
4. `height` grid lines (`#` or `.`)
5. `snakebotsPerPlayer`
6. `snakebotsPerPlayer` lines: my snakebot IDs
7. `snakebotsPerPlayer` lines: opponent snakebot IDs

### Per turn

1. `powerSourceCount`
2. `powerSourceCount` lines: `x y`
3. `snakebotCount`
4. `snakebotCount` lines: `snakebotId body`

- `body` format: `x,y:x,y:...` with head first.

### Output

Single line with one or more actions separated by `;`.

## Constraints

- First turn <= 1000 ms
- Other turns <= 50 ms
- 15 <= width <= 45
- 10 <= height <= 30
- 1 <= snakebotCount <= 8
