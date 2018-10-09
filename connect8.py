from enum import IntEnum

# Custom Exceptions
class PlayerDuplicateMoveError(Exception):
    """Error in case of player duplicate move"""

    def __init__(self, player):
        msg = f"Duplicate move for player {player}"
        super(PlayerDuplicateMoveError, self).__init__(msg)


class ColumnOutofRangeError(Exception):
    """Error in case of column number out of range"""

    def __init__(self, column):
        msg = f"Column number {column} out of range, expected a value between 1 and 7"
        super(ColumnOutofRangeError, self).__init__(msg)


class ColumnFullError(Exception):
    """Error in case of column is full"""

    def __init__(self, column):
        msg = f"The column {column} is full"
        super(ColumnFullError, self).__init__(msg)


# Enums
class Player(IntEnum):
    Red = 1
    Yellow = 2


class Connect8(object):
    def __init__(self):
        self.last_player = None
        self.grid = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]

    def _validate_player(self, player):
        """Validate player duplicate move"""
        if player == self.last_player:
            raise PlayerDuplicateMoveError(player)

    def _validate_column(self, column):
        """validate columns"""
        if not 1 <= column <= len(self.grid[0]):
            raise ColumnOutofRangeError(column)

        if self.grid[0][column - 1] != 0:
            raise ColumnFullError(column)

    def _get_1_diagonal(self, row, column):
        x, y = row + 1, column + 1
        while 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            yield (x, y)
            x, y = x + 1, y + 1

        x, y = row - 1, column - 1
        while 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            yield (x, y)
            x, y = x - 1, y - 1

    def _get_2_diagonal(self, row, column):
        x, y = row - 1, column + 1
        while 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            yield (x, y)
            x, y = x - 1, y + 1

        x, y = row + 1, column - 1
        while 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            yield (x, y)
            x, y = x + 1, y - 1

    def _is_game_over(self, player, row, column) -> bool:
        """Check if the game is over"""

        player = int(player)

        # check the column
        if all([self.grid[i][column] == player for i in range(len(self.grid))]):
            return True

        # check the row
        if all([self.grid[row][j] == player for j in range(len(self.grid[0]))]):
            return True

        # check 1st diagonal
        diagonal = list(self._get_1_diagonal(row, column))
        if len(diagonal) > 3 and all([self.grid[x][y] == player for x, y in diagonal]):
            return True

        # check 2 diagonal
        diagonal = list(self._get_2_diagonal(row, column))
        if len(diagonal) > 3 and all([self.grid[x][y] == player for x, y in diagonal]):
            return True

        return False

    def move(self, player, column) -> bool:
        """Move method"""
        self._validate_player(player)
        self._validate_column(column)

        self.last_player = player

        column -= 1
        for row in range(len(self.grid) - 1, -1, -1):
            if self.grid[row][column] == 0:
                self.grid[row][column] = int(player)
                break

        return self._is_game_over(player, row, column)

    def __str__(self):
        return "\n".join([str(row) for row in self.grid])
