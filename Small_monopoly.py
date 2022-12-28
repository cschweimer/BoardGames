import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random
from Inputs import board
from Inputs import players
from Inputs import plot_board

# Size of the board
SIZE = 2

plot_board(SIZE)


def dice():
    return random.choices([1,2,3,4,5,6])[0]

iterator = 0

while players[0]['money'] > 0 and players[1]['money'] > 0 and players[0]['money'] < 500 and players[1]['money'] < 500:

    # Current position of the player
    current_position = [players[0]['position'], players[1]['position']]

    # Roll the dice
    result = dice()
    print(result)

    player_turn = iterator%2

    # New position of the player
    new_position = (current_position[player_turn] + result) % 12

    players[player_turn]['position'] = new_position

    # Go to prison field
    if new_position == 9:
        players[player_turn]['position'] = 3

    # Price at prison
    if new_position == 3:
        players[player_turn]['money'] -= board[new_position]['rent']

    # Taxes
    if new_position == 6:
        players[player_turn]['money'] -= board[new_position]['rent']

    # In case the player passes start he gets 50 if he lands on start, and 25 if he passes start
    if new_position < current_position[player_turn]:
        if new_position == 0:
            players[player_turn]['money'] += 50
        else:
            players[player_turn]['money'] += 25

    # Buy a house
    if board[new_position]['owner'] > 0 and board[new_position]['owner'] == players[player_turn]['number'] and board[1]['houses'] < 3:
        board[new_position]['houses'] += 1
        players[player_turn]['money'] -= board[new_position]['house_price']

    # Buy a property
    if board[new_position]['owner'] == 0:
        board[new_position]['owner'] == players[player_turn]['number']
        players[player_turn]['money'] -= board[new_position]['price']
        players[player_turn]['properties'].append(new_position)
        players[player_turn]['properties'].sort()
        board[new_position]['owner'] = 1

    # Pay rent
    if board[new_position]['owner'] > 0 and board[new_position]['owner'] != players[player_turn]['number']:
        players[player_turn]['money'] -= board[new_position]['rent'] * (board[new_position]['houses']+1)
        players[board[new_position]['owner']-1]['money'] += board[new_position]['rent'] * (board[new_position]['houses']+1)

    iterator += 1

    # Plot the board
    plot_board(SIZE)
    
# Result
if players[0]['money'] >= 500 or players[1]['money'] < 0:
    print('Player ' + str(players[0]['number']) + ' won!')
else:
    print('Player ' + str(players[1]['number']) + ' won!')
    