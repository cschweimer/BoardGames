import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Define the board
dict0 = {'position': 0, 'name': 'Start', 'owner': -1, 'x': 0.5, 'y': 0.5}

dict1 = {'position': 1, 'price': 10, 'owner': 0, 'houses': 0, 'house_price': 5, 'rent': 1, 'x': 0.5, 'y': 1.5}

dict2 = {'position': 2, 'price': 20, 'owner': 0, 'houses': 0, 'house_price': 5, 'rent': 2, 'x': 0.5, 'y': 2.5}

dict3 = {'position': 3, 'rent': 10, 'owner': -1, 'name': 'Prison', 'x': 0.5, 'y': 3.5}

dict4 = {'position': 4, 'price': 30, 'owner': 0, 'houses': 0, 'house_price': 10, 'rent': 4, 'x': 1.5, 'y': 3.5}

dict5 = {'position': 5, 'price': 30, 'owner': 0, 'houses': 0, 'house_price': 10, 'rent': 4, 'x': 2.5, 'y': 3.5}

dict6 = {'position': 6, 'rent': 25, 'owner': -1, 'name': 'Taxes', 'x': 3.5, 'y': 3.5}

dict7 = {'position': 7, 'price': 40, 'owner': 0, 'houses': 0, 'house_price': 15, 'rent': 6, 'x': 3.5, 'y': 2.5}

dict8 = {'position': 8, 'price': 40, 'owner': 0, 'houses': 0, 'house_price': 15, 'rent': 6, 'x': 3.5, 'y': 1.5}

dict9 = {'position': 9, 'owner': -1, 'name': 'Go to Prison', 'x': 3.5, 'y': 0.5}

dict10 = {'position': 10, 'price': 50, 'owner': 0, 'houses': 0, 'house_price': 20, 'rent': 8, 'x': 2.5, 'y': 0.5}

dict11 = {'position': 11, 'price': 60, 'owner': 0, 'houses': 0, 'house_price': 25, 'rent': 10, 'x': 1.5, 'y': 0.5}

board = [dict0, dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10, dict11]

# Define the players
player1 = {'position': 0, 'money': 400, 'color': 'cyan', 'number': 1, 'properties': []}
player2 = {'position': 0, 'money': 400, 'color': 'green', 'number': 2, 'properties': []}

players = [player1, player2]

def plot_board(SIZE):
    # Plot the board
    fig,ax = plt.subplots(figsize=(8,8))

    plt.xlim(-1,SIZE+3)
    plt.ylim(-1,SIZE+3)

    plt.hlines(0,0,SIZE+2, linewidth=1, color='black')   
    plt.hlines(1,0,SIZE+2, linewidth=1, color='black')   
    plt.hlines(SIZE+1,0,SIZE+2, linewidth=1, color='black')   
    plt.hlines(SIZE+2,0,SIZE+2, linewidth=1, color='black')   

    plt.vlines(0,0,SIZE+2, linewidth=1, color='black')
    plt.vlines(1,0,SIZE+2, linewidth=1, color='black')
    plt.vlines(SIZE+1,0,SIZE+2, linewidth=1, color='black')
    plt.vlines(SIZE+2,0,SIZE+2, linewidth=1, color='black')

    for i in range(SIZE-1):
        plt.plot((0,1),(SIZE-i,SIZE-i), linewidth=1, color='black')
        plt.plot((SIZE-i,SIZE-i),(0,1), linewidth=1, color='black')
        plt.plot((SIZE-i,SIZE-i),(SIZE+1,SIZE+2), linewidth=1, color='black')
        plt.plot((SIZE+1,SIZE+2),(SIZE-i,SIZE-i), linewidth=1, color='black')

    # Corners
    ax.add_patch(Rectangle((0,0), 1, 1, color ='limegreen'))
    ax.annotate('Start', xy=(0.4,0.4), color='black', fontsize=8)

    ax.add_patch(Rectangle((0,SIZE+1), 1, 1, color ='grey'))
    ax.annotate('Prison', xy=(0.4,SIZE+1+0.4), color='black', fontsize=8)

    ax.add_patch(Rectangle((SIZE+1,SIZE+1), 1, 1, color ='red'))
    ax.annotate('Taxes', xy=(SIZE+1+0.4,SIZE+1+0.4), color='black', fontsize=8)

    ax.add_patch(Rectangle((SIZE+1,0), 1, 1, color ='grey'))
    ax.annotate('Go to prison', xy=(SIZE+1+0.2,0.4), color='black', fontsize=8)

    # Other fields
    ax.add_patch(Rectangle((0,1), 1, 1, color ='lightblue'))
    ax.add_patch(Rectangle((0,2), 1, 1, color ='lightblue'))

    ax.add_patch(Rectangle((1,3), 1, 1, color ='orange'))
    ax.add_patch(Rectangle((2,3), 1, 1, color ='orange'))

    ax.add_patch(Rectangle((3,1), 1, 1, color ='yellow'))
    ax.add_patch(Rectangle((3,2), 1, 1, color ='yellow'))

    ax.add_patch(Rectangle((1,0), 1, 1, color ='blue'))
    ax.add_patch(Rectangle((2,0), 1, 1, color ='blue'))
    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.axis('off')
    
    plt.scatter(x=board[players[0]['position']]['x'], y=board[players[0]['position']]['y'], c=players[0]['color'])
    plt.scatter(x=board[players[1]['position']]['x']+0.1, y=board[players[1]['position']]['y'], c=players[1]['color'])

    plt.pause(1)
    plt.close('all')
    