import os

def clearScreen():
    # Store output into any var
    # _ is used here as python shell always
    # stores the last output into _
    if os.name == 'nt':
        _ = os.system('cls')
    # This is for linux and mac os.name = 'posix'
    else:
        _ = os.system('clear')

import subprocess

def clearScreenViaSubprocess():
    _ = subprocess.call('clear' if os.name == 'posix' else 'cls')
 
# Render TicTacToe board
def displayBoard(board):
    clearScreen()
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])

def playerInput():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O: ').upper()
    
    if marker == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def placeMarker(board, position, marker):
    board[position] = marker

def winCheck(board, marker):
    return (
        (board[1] == marker and board[2] == marker and board[3] == marker) or #row
        (board[4] == marker and board[5] == marker and board[6] == marker) or #row
        (board[7] == marker and board[8] == marker and board[9] == marker) or #row
        (board[1] == marker and board[4] == marker and board[7] == marker) or #column
        (board[2] == marker and board[5] == marker and board[8] == marker) or #column
        (board[3] == marker and board[6] == marker and board[9] == marker) or #column
        (board[1] == marker and board[5] == marker and board[9] == marker) or #diagonal
        (board[7] == marker and board[5] == marker and board[3] == marker) #diagonal
        )

def spaceCheck(board, position):
    return board[position] == ' '
    
def fullBoardSpaceCheck(board):
    for i in range(1, 10):
        if (spaceCheck(board, i)):
            return False
    return True

def playerChoice(board):
    position = 0
    while position not in range(1, 10) or not spaceCheck(board, position):
        position = int(input('Enter position (1-9): '))
    return position

def replay():
    return input('Want to replay? (y/n): ').upper() == 'Y'

if __name__ == '__main__':
    print("Welcome to TicTacToe Game!")

    while True:
        #Reset the board
        board = [' '] * 10
        players = ['P1', 'P2']
        markers = playerInput()
        playersMarkers = []

        for item in zip(players, markers):
            playersMarkers.append(item)
        print(playersMarkers)
        turn = 0
        gameOn = True

        while gameOn:
            displayBoard(board)
            print('{} turn:'.format(players[turn]))
            position = playerChoice(board)
            marker = playersMarkers[turn][1]
            placeMarker(board, position, marker)
            displayBoard(board)
            if (winCheck(board, marker)):
                print("{} Won the game !!".format(players[turn]))
                break
            elif (fullBoardSpaceCheck(board)):
                displayBoard(board)
                print('Game is drawn.')
                break
            else:
                turn = 1 if turn == 0 else 0
        
        if not replay():
            break