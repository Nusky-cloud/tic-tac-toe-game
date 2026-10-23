# Tic Tac Toe Game

This repository contains Tic Tac Toe Game which is built in Python.

# How to run?

## Requirements

For running the game you need:

- [Python 3.14.5](https://www.python.org/downloads/)
- pip 26.1.2

NOTE : pip will be installed with Python. You can check the Python and pip version in a console by 

```shell
python --version 
python -m pip --version
```

## Running

- First, install a required package

```shell
pip install numpy
```

- Secondly, clone this repository on your computer or download as a zip file.
```shell
git clone https://github.com/Nusky-cloud/tic-tac-toe-game.git
```

- Finally, open a console and change directory to project root and execute below command. This will start the game.

```shell
python Tic-Tac-Toe-Game.py
```

# Game Information

Only two players can play this game. The game board consists of 9 squares (i.e. 3 x 3 grid) where the players can place their token.

```shell
token of 1st player : x
token of 2ns player : o
```

The game will keep on prompting each player to place their token which should be provided as the number of row and the column with a comma separator. The game will not allow to place two tokens on the same place.

```shell
Dear Player 1, Please specify the position as row, col : 3,3
['.', '.', '.']
['.', '.', '.']
['.', '.', 'x']
```

Once all the squares are filled, the winner will be announced based on same tokens in a matching row (i.e. horizontally / vertically / diagonally).

The game can be played unlimited number of times and the final winner will be announced with the score of each player.