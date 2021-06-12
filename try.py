class TicTacToe:
    def __init__(self):
        self.board = []
        self.win = False
        self.player = {}

    def initBoard(self,length):
        for _ in range(length):
            arr = []
            for _ in range(length):
                arr.append('')
            self.board.append(arr) 

    def printBoard(self):
        for i in self.board:
            print(self.board[i],' ',end = '')
            if i%3 == 0:
                print('\n')

    def getPlayerDetails(self):
        print("enter size of grid",end="\n"):
        self.initBoard(int(input()))
        print('Enter number of players',end="\n")
        x = int(input())
        s = 'Welcome,'
        for i in range(x):
            print(i+1,' player name',end = '\n')
            play = input()
            print(i+1,' marker',end = '\n')
            mark = input()
            self.player[play] = mark
            s = play + ', '
        print('Welcome',s,'!')

    def checkWin(self,pl,marker):

        # check horizental

        for i in range(len(self.board)):
            counter = 0
            for j in range(len(self.board)):
                if self.board[i][j] == marker:
                    counter+=1
            if counter == len(self.board):
                print("Hurray!! We found our winner")
                self.win = True
                print('our winner is ',pl)
                return True

        # check vertical

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
            print('our winner is ',pl)
            return True
        else:
            return False

    def play(self):
        self.getPlayerDetails()
        self.printBoard()

        while not self.win:
            for pl,marker in self.player.items():
                print(pl,', This is your turn please enter and ',marker,' this is your marker')

                move = input()
                while not (move.isnumeric() and 0 < int(move) < 10 and self.board[int(move)] == ''):
                    print('this is incorrect move please enter your move again')
                    move = input()

                move = int(move)
                self.board[move] = marker
                self.printBoard()
                if(self.checkWin(pl,marker)):
                    break


obj = TicTacToe()
obj.play()