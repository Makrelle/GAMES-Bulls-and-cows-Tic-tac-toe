# 2nd project - Tic Tac Toe

SEPARATOR = "=" * 40
MINI_SEPARATOR = "-" * 9


def introduction() -> None:
    print(SEPARATOR)
    print("""GAME RULES:
Each player can place one mark (or stone) per turn on the 3x3 grid
The WINNER is who succeeds in placing three of their marks in a
* horizontal,
* vertical or
* diagonal row
Let's start the game""")


def creating_table() -> list:
    table = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    return table


def player_move(table: list) -> str:
    players = ["o", "x"]
    i = 0        # i = player index
    moves = 0
    while True:
        player = players[i]
        print(SEPARATOR)
        position = input(f"Player {player} | Please enter your move number: ")
        print(SEPARATOR)
        print(SEPARATOR)

        if check_input(position):
            row = (int(position) - 1) // 3
            column = (int(position) - 1) % 3

            if check_free_position(row, column, table):
                table[row][column] = player  # put player mark into the table
                print_table(table)

                if check_winner(table, player):
                    return f"Congratulations, the player {player} WON!"
                i = switch_player(i)
                moves += 1

                if moves == 9:
                    return "It's a tie!"


def check_input(position: str) -> bool:
    if position.isnumeric():
        if 0 < int(position) < 10:
            return True


def check_free_position(row: int, column: int, table: list) -> bool:
    if table[row][column] == " ":
        return True
    else:
        print("Position already taken")
        return False


def check_winner(table: list, player: str) -> bool:
    winner = ""
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2] != " ":  # check rows
            winner = player
        if table[0][i] == table[1][i] == table[2][i] != " ":  # check columns
            winner = player
    if table[0][0] == table[1][1] == table[2][2] != " "\
            or table[0][2] == table[1][1] == table[2][0] != " ":  # check diagonals
        winner = player
    return True if winner else False


def switch_player(i: int) -> int:
    i = 1 - i
    return i


def print_table(table: list) -> None:
    print(MINI_SEPARATOR)
    for i in range(len(table)):
        print(" | ".join(table[i]))
        print(MINI_SEPARATOR)


def main():
    introduction()
    table = creating_table()
    print_table(table)
    print(player_move(table))


main()
