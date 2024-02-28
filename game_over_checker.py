def check_game_over(gameboard):
    is_game_over = False

    # Check for match in rows
    for num in range(3):
        if check_list(list(gameboard[num].values())):
            is_game_over = True

    # Check for match in columns
    for num in range(3):
        column = []
        for col in range(3):
            column += list(gameboard[col].values())[num]
        if check_list(column):
            is_game_over = True

    # Check for diagonal matches
    if gameboard[0][1] == gameboard[1][5] and gameboard[0][1] == gameboard[2][9] and gameboard[0][1] != '_':
        is_game_over = True
    elif gameboard[0][3] == gameboard[1][5] and gameboard[0][3] == gameboard[2][7] and gameboard[0][3] != '_':
        is_game_over = True
    return is_game_over


def check_list(value_list):
    if value_list[0] == value_list[1] and value_list[0] == value_list[2] and value_list[0] != '_':
        return True
    else:
        return False