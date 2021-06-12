class TicTacToe:
    def __init__(self):
        self.board = {
            1: '-',
            2: '-',
            3: '-',
            4: '-',
            5: '-',
            6: '-',
            7: '-',
            8: '-',
            9: '-'
        }

        self.win = False
        self.turnFlagP1 = True
        self.player1 = ''
        self.player2 = ''

    def printBoard(self):
        for i in self.board:
            print(self.board[i],' ',end = '')
            if i%3 == 0:
                print('\n')

    def getPlayerDetails(self):
        print("Enter 1st player name",end='\n')
        self.player1 = input()
        print("Enter 2nd player name",end='\n')
        self.player2 = input()
        print('Welcome',self.player1,',',self.player2,'!')

    def checkWin(self):
        if self.turnFlagP1:
            marker = 'X'
        else:
            marker = 'O'

        if self.board[1] == marker and self.board[2] == marker and self.board[3] == marker or \
        self.board[4] == marker and self.board[5] == marker and self.board[6] == marker or \
        self.board[7] == marker and self.board[8] == marker and self.board[9] == marker or \
        self.board[1] == marker and self.board[4] == marker and self.board[7] == marker or \
        self.board[2] == marker and self.board[5] == marker and self.board[8] == marker or \
        self.board[3] == marker and self.board[6] == marker and self.board[9] == marker or \
        self.board[1] == marker and self.board[5] == marker and self.board[9] == marker or \
        self.board[3] == marker and self.board[5] == marker and self.board[7] == marker:
            print("Hurray!! We found our winner")
            self.win = True
            if self.turnFlagP1:
                print('our winner is 1')
            else:
                print('our winner is 2')
            return True
        else:
            return False

    def checkEnd(self):
        for i in self.board:
            if self.board[i] == '-':
                return False
        else:
            self.win = True
            print('The match has been drawn')
            return True

    def play(self):
        self.getPlayerDetails()
        # print(player1,player2)
        self.printBoard()
        while not self.win:
            if self.turnFlagP1:
                print(self.player1,', This is your turn please enter')
            else:
                print(self.player2,', This is your turn please enter')

            move = input()
            while not (move.isnumeric() and 0 < int(move) < 10 and self.board[int(move)] == '-'):
                print('this is incorrect move please enter your move again')
                move = input()

            move = int(move)
            if self.turnFlagP1:
                self.board[move] = 'X'
            else:
                self.board[move] = 'O'
            self.printBoard()
            if(self.checkWin()):
                break
            elif self.checkEnd():
                break
            else:
                self.turnFlagP1 = not self.turnFlagP1


obj = TicTacToe()
obj.play()