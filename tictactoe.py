board = {
    1: '',
    2: '',
    3: '',
    4: '',
    5: '',
    6: '',
    7: '',
    8: '',
    9: ''
}

win = False
turnFlagP1 = True
player1 = ''
player2 = ''

def printBoard():
    for i in board:
        print(board[i],' ',end = '')
        if i%3 == 0:
            print('\n')

def getPlayerDetails():
    print("Enter 1st player name",end='\n')
    player1 = input()
    print("Enter 2nd player name",end='\n')
    player2 = input()
    print('Welcome',player1,',',player2,'!')

def checkWin():
    if turnFlagP1:
        marker = 'X'
    else:
        marker = 'O'

    if board[1] == marker and board[2] == marker and board[3] == marker or \
    board[4] == marker and board[5] == marker and board[6] == marker or \
    board[7] == marker and board[8] == marker and board[9] == marker or \
    board[1] == marker and board[4] == marker and board[7] == marker or \
    board[2] == marker and board[5] == marker and board[8] == marker or \
    board[3] == marker and board[6] == marker and board[9] == marker or \
    board[1] == marker and board[5] == marker and board[9] == marker or \
    board[3] == marker and board[5] == marker and board[7] == marker:
        print("Hurray!! We found our winner")
        win = True
        if turnFlagP1:
            print('our winner is 1')
        else:
            print('our winner is 2')
        return True
    else:
        return False


def main():
    getPlayerDetails()
    print(player1,player2)
    while not win:
        printBoard()
        if turnFlagP1:
            print(player1,', This is your turn please enter')
        else:
            print(player2,', This is your turn please enter')

        move = input()
        while not (move.isnumeric() and 0 < int(move) < 10 and board[int(move)] == ''):
            print('this is incorrect move please enter your move again')
            move = input()

        move = int(move)
        if turnFlagP1:
            board[move] = 'X'
        else:
            board[move] = 'O'

        if(checkWin()):
            break
        else:
            pass


main()
