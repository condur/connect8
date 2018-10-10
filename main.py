#!/usr/bin/python3

import random
from connect8 import *


def print_result(connect, has_winner):
    if has_winner:
        print(f"The {str(connect.last_player)} ({connect.last_player}) has won.")
    else:
        print("No winner this time, please try again.")

    print("\n")
    print(connect)


def main():

    # Simulate a game
    connect = Connect8()
    i, game_over, has_winner = 0, False, True
    while True:
        try:
            column = random.randrange(1, 8)
            if i % 2 == 0:
                game_over = connect.move(Player.Red, column)
            else:
                game_over = connect.move(Player.Yellow, column)
        except ColumnFullError:
            if all([connect.grid[0][j] != 0 for j in range(len(connect.grid[0]))]):
                # no more available slots, quit the game
                has_winner = False
                break
            else:
                continue

        if game_over is True:
            break
        i += 1

    # Game over, print the results
    print_result(connect, has_winner)


if __name__ == "__main__":
    main()
