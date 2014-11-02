"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 20    # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player):
    '''
    takes a current board and the next player to move
    '''
    
    choosen_squares = []
    while board.check_win()== None:
        choosen_squares=  random.choice(board.get_empty_squares())
        board.move(choosen_squares[0],choosen_squares[1],player)
        player= provided.switch_player(player)

       
def mc_update_scores(scores, board, player):
    
    winner = board.check_win()
    # looping through the grid and assigning scores for win/lose
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            player = board.square(row, col)
            if player == 2:
                if winner == 2:
                    scores[row][col] += MCMATCH
                elif winner == 3:
                    scores[row][col] += -MCOTHER
            elif player == 3:
                if winner == 2:
                    scores[row][col] += -MCOTHER
                elif winner == 3:
                    scores[row][col] += MCMATCH
            else:
                # the rest is 0 value, don't care as it has no effect on score
                pass
        
        
def get_best_move(board, scores):
    
    _max = float('-inf')
    empty_items = board.get_empty_squares()
    best_moves = []
    if len(empty_items) == 0:
        return    
    for (row, col) in empty_items:
        if scores[row][col] > _max:
            _max = scores[row][col]
    
    for (row, col) in empty_items:
        if scores[row][col] == _max:
            best_moves.append((row, col))
    
    return random.choice(best_moves)


def mc_move(board, player, trials):
    
#    scores = [[0 for dummy_cols in range(board.get_dim()[1]) for dummy_row in range(board.get_dim()[0])]
    initial_scores = [[0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
    for dummy_trial in range(trials):
        cloned = board.clone()
        mc_trial(cloned, player)
        mc_update_scores(initial_scores, cloned, player)
    return get_best_move(board, initial_scores)        
    
        
       
# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.
# provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
