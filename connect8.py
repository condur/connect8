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


# Main class
class Connect8(object):
    def __init__(self):
        """
        The __init__ method is roughly what represents
        a constructor in Python.

        The 'self' variable represents the instance
        of the object itself.
        """
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
        """
        Validate player move.

        Args:
            player (Enum.Player): the player making the move

        Raises:
            PlayerDuplicateMoveError
        """
        if player == self.last_player:
            raise PlayerDuplicateMoveError(player)

    def _validate_column(self, column):
        """
        Validate columns for the last move.

        Args:
            column (int):

        Raises:
            ColumnOutofRangeError: if column value is not between 1 and 7
            ColumnFullError: Is the column is filled
        """
        if not 1 <= column <= len(self.grid[0]):
            raise ColumnOutofRangeError(column)

        if self.grid[0][column - 1] != 0:
            raise ColumnFullError(column)

    def _get_1_diagonal(self, row, column):
        """
        A generator function to get one of the diagonal coordinates.

        Args:
            row (int):
            column (int):

        Yields:
            (x, y): coordinates pair

        """
        x, y = row + 1, column + 1
        while 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            yield (x, y)
            x, y = x + 1, y + 1

        x, y = row - 1, column - 1
        while 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            yield (x, y)
            x, y = x - 1, y - 1

    def _get_2_diagonal(self, row, column):
        """
        A generator function to get one of the diagonal coordinates.

        Args:
            row (int):
            column (int):

        Yields:
            (x, y): coordinates pair

        """
        x, y = row - 1, column + 1
        while 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            yield (x, y)
            x, y = x - 1, y + 1

        x, y = row + 1, column - 1
        while 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            yield (x, y)
            x, y = x + 1, y - 1

    def _is_game_over(self, player, row, column) -> bool:
        """
        Check if the game is over.

        Args:
            player (Enum.Player): the player making the move
            row (int):
            column (int):

        Returns:
             True if a row, column or diagonal of succesive
             tokens are present, False otherwise.
        """

        player = int(player)

        # check the column
        if all([self.grid[i][column] == player for i in range(len(self.grid))]):
            return True

        # check the row
        if all([self.grid[row][j] == player for j in range(len(self.grid[0]))]):
            return True

        min_diagonal_length = 3
        # check 1st diagonal
        diagonal = list(self._get_1_diagonal(row, column))
        if len(diagonal) > min_diagonal_length and all(
            [self.grid[x][y] == player for x, y in diagonal]
        ):
            return True

        # check 2 diagonal
        diagonal = list(self._get_2_diagonal(row, column))
        if len(diagonal) > min_diagonal_length and all(
            [self.grid[x][y] == player for x, y in diagonal]
        ):
            return True

        return False

    def move(self, player, column) -> bool:
        """
        Move method.

        Args:
            player (Enum.Player): the player making the move
            column (int):

        Returns:
             True if game is over, False otherwise.
        """
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
        """A string representation of the class"""
        return "\n".join([str(row) for row in self.grid])
