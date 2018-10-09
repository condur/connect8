import pytest
from connect5 import *


def test_init():
    connect5 = Connect5()
    assert connect5.last_player is None
    assert connect5.grid == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]


def test_validate_player_value():
    connect5 = Connect5()
    connect5.move(Player.Red, 1)
    with pytest.raises(PlayerDuplicateMoveError):
        connect5.move(Player.Red, 1)


def test_validate_column_range():
    connect5 = Connect5()
    with pytest.raises(ColumnOutofRangeError):
        connect5.move(Player.Red, 0)
    with pytest.raises(ColumnOutofRangeError):
        connect5.move(Player.Red, 8)


def test_move():
    connect5 = Connect5()
    connect5.move(Player.Red, 1)
    assert connect5.grid[5][0] == 1
    connect5.move(Player.Yellow, 1)
    assert connect5.grid[4][0] == 2


def test_validate_column_full():
    connect5 = Connect5()
    for i in range(len(connect5.grid)):
        if i % 2 == 0:
            connect5.move(Player.Red, 1)
        else:
            connect5.move(Player.Yellow, 1)
    with pytest.raises(ColumnFullError):
        connect5.move(Player.Red, 1)


def test_is_game_over():
    connect5 = Connect5()
    for i in range(10):
        if i % 2 == 0:
            assert connect5.move(Player.Red, 1) is False
        else:
            assert connect5.move(Player.Yellow, 2) is False
    assert connect5.move(Player.Red, 1) is True
