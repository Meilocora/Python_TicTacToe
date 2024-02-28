import os
import random
from game_over_checker import check_game_over
from prettytable import PrettyTable

gameboard = [
    {1: "_", 2: "_", 3: "_"},
    {4: "_", 5: "_", 6: "_"},
    {7: "_", 8: "_", 9: "_"},
]

def display_gameboard():
    table = PrettyTable(header=False)
    for row in gameboard:
        table.add_row(row.values(), divider=True)
    os.system('cls')
    print(table)

def check_field(row, col):
    if gameboard[row][col] == '_':
        return True
    else:
        return False

def valid_range(row, col):
    if 0 <= row <= 2 and 0 <= col <= 2:
        return True
    else:
        return False
def convert_coords(row, col):
    if row == 1:
        col += 4
    elif row == 2:
        col+=7
    else:
        col += 1
    return col

def bot_turn():
    free_keys = []
    for num in range(3):
        row_free_keys = [k for k, v in gameboard[num].items() if v == '_']
        free_keys += row_free_keys
    bot_choice = random.choice(free_keys)
    for num in range(3):
        if bot_choice in gameboard[num]:
            gameboard[num][bot_choice] = 'O'

def check_draw():
    free_keys = []
    for num in range(3):
        row_free_keys = [k for k, v in gameboard[num].items() if v == '_']
        free_keys += row_free_keys
    if len(free_keys) == 0:
        return True
    else:
        return False

game_over = False
while not game_over:
    players_choice_column_raw = int(input('Select a column: ')) - 1
    players_choice_row = int(input('Select a row: ')) - 1

    if valid_range(players_choice_row, players_choice_column_raw):
        players_choice_column = convert_coords(players_choice_row, players_choice_column_raw)
        if check_field(players_choice_row, players_choice_column):
            gameboard[players_choice_row][players_choice_column] = 'X'
            if check_game_over(gameboard):
                display_gameboard()
                game_over = True
                print('Congratulations, you won!')
            else:
                if not check_draw():
                    bot_turn()
                    display_gameboard()
                    if check_game_over(gameboard):
                        game_over = True
                        print('Oh no, the bot won!')
                else:
                    game_over = True
                    print('Draw!')
        else:
            print('The field is alreasy filled... please choose a free field')
    else:
        print('Invalid inputs. Make sure to pick values from 1 to 3 for the row and column.')

