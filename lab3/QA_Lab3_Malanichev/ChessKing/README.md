# Chess King in Python

## Overview


This project is a simple chess game model implemented in Python, demonstrating object-oriented programming (OOP) principles. It includes a class hierarchy with at least two levels of inheritance, focusing on chess pieces and a game board. The code provides a foundation for a chess game, with basic functionality for piece movement and board management.

## Features

- **OOP Structure**: Implements a class hierarchy with `GameObject` as the base class, `Piece` as an intermediate class, and specific piece classes (`Pawn` and `Knight`) inheriting from `Piece`.
- **Chess Pieces**: Includes two chess pieces (`Pawn` and `Knight`) with simplified movement logic:
  - Pawns can move forward one or two squares (on their first move).
  - Knights move in an L-shape (2x1 or 1x2).
- **Board Management**: The `Board` class manages piece placement and movement, with basic validation and capture mechanics.
- **Position Tracking**: Pieces are tracked by their (x, y) coordinates on an 8x8 chessboard.
- **Extensibility**: The structure allows for easy addition of new piece types or rules.

## Project Structure

- `chess.py`: The main Python file containing all classes and logic.
  - `GameObject`: Base class for all game objects, storing position.
  - `Piece`: Intermediate class for chess pieces, adding color and move validation.
  - `Pawn`: Represents a pawn with basic movement rules.
  - `Knight`: Represents a knight with L-shaped movement.
  - `Board`: Manages the chessboard and piece interactions.
- Example usage is included at the bottom of `chess.py` to demonstrate piece creation, placement, and movement.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chess-game-model.git
