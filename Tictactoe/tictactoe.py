cells = ["_"] * 9


def print_grid():
    print("---------")
    print("|", cells[0], cells[1], cells[2], "|")
    print("|", cells[3], cells[4], cells[5], "|")
    print("|", cells[6], cells[7], cells[8], "|")
    print("---------")


def check_winner(symbol):
    lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 3, 6), (1, 4, 7), (2, 5, 8),
             (0, 4, 8), (2, 4, 6)]
    for a, b, c in lines:
        if cells[a] == cells[b] == cells[c] == symbol:
            return True
    return False


print_grid()

player = "X"

while True:
    coords = input("Enter the coordinates: ").split()

    try:
        row = int(coords[0])
        column = int(coords[1])
    except (ValueError, IndexError):
        print("You should enter numbers!")
        continue

    if row < 1 or row > 3 or column < 1 or column > 3:
        print("Coordinates should be from 1 to 3!")
        continue

    index = (row - 1) * 3 + (column - 1)

    if cells[index] != "_":
        print("This cell is occupied! Choose another one!")
        continue

    cells[index] = player
    print_grid()

    if check_winner(player):
        print(player + " wins")
        break

    if "_" not in cells:
        print("Draw")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"
