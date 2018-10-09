import pytest
from connect8 import *


def test_init():
    connect = Connect8()
    assert connect.last_player is None
    assert connect.grid == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]


def test_validate_player_value():
    connect = Connect8()
    connect.move(Player.Red, 1)
    with pytest.raises(PlayerDuplicateMoveError):
        connect.move(Player.Red, 1)


def test_validate_column_range():
    connect = Connect8()
    with pytest.raises(ColumnOutofRangeError):
        connect.move(Player.Red, 0)
    with pytest.raises(ColumnOutofRangeError):
        connect.move(Player.Red, 8)


def test_move():
    connect = Connect8()
    connect.move(Player.Red, 1)
    assert connect.grid[5][0] == 1
    connect.move(Player.Yellow, 1)
    assert connect.grid[4][0] == 2


def test_validate_column_full():
    connect = Connect8()
    for i in range(len(connect.grid)):
        if i % 2 == 0:
            connect.move(Player.Red, 1)
        else:
            connect.move(Player.Yellow, 1)
    with pytest.raises(ColumnFullError):
        connect.move(Player.Red, 1)


def test_is_game_over():
    connect = Connect8()
    for i in range(10):
        if i % 2 == 0:
            assert connect.move(Player.Red, 1) is False
        else:
            assert connect.move(Player.Yellow, 2) is False
    assert connect.move(Player.Red, 1) is True
