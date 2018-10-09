from connect8 import *
import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def main():
    connect = Connect8()
    i, game_over, has_winner = 0, False, True
    while True:
        try:
            if i % 2 == 0:
                game_over = connect.move(Player.Red, get_random(1, 7))
            else:
                game_over = connect.move(Player.Yellow, get_random(1, 7))
        except ColumnFullError:
            if all([connect.grid[0][j] != 0 for j in range(len(connect.grid[0]))]):
                # no more available slots, quit the
                has_winner = False
                break
            else:
                continue

        if game_over is True:
            break
        i += 1

    if has_winner:
        print(f"The {str(connect.last_player)} ({connect.last_player}) won.")
    else:
        print("No winner this time. Please try again.")

    print(connect)


if __name__ == "__main__":
    main()
