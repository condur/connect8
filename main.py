from connect5 import *
import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def main():
    connect5 = Connect5()
    i, game_over, has_winner = 0, False, True
    while True:
        try:
            if i % 2 == 0:
                game_over = connect5.move(Player.Red, get_random(1, 7))
            else:
                game_over = connect5.move(Player.Yellow, get_random(1, 7))
        except ColumnFullError:
            if all([connect5.grid[0][j] != 0 for j in range(len(connect5.grid[0]))]):
                # no more available slots, quit the
                has_winner = False
                break
            else:
                continue

        if game_over is True:
            break
        i += 1

    if has_winner:
        print(f"The {str(connect5.last_player)} ({connect5.last_player}) won.")
    else:
        print("No winner this time. Please try again.")

    print(connect5)


if __name__ == "__main__":
    main()
