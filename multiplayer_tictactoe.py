class TicTacToe:
    def __init__(self):
        self.board = []
        self.win = False
        self.player = {}

    def initBoard(self,length):
        for _ in range(length):
            arr = []
            for _ in range(length):
                arr.append('-')
            self.board.append(arr) 

    def printBoard(self):
        for i in self.board:
            print(i,end = '\n')

    def getPlayerDetails(self):
        print("enter size of grid",end="\n")
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
        counter_diagonal_left = 0
        counter_diagonal_right = 0
        for i in range(len(self.board)):
            counter_horizental = 0
            counter_vertical = 0
            for j in range(len(self.board)):
                if self.board[i][j] == marker:
                    counter_horizental+=1
                if self.board[j][i] == marker:
                    counter_vertical+=1
                if i == j and self.board[i][j] == marker:
                    counter_diagonal_left+=1
                if i +j == len(self.board) and self.board[i][j] == marker:
                    counter_diagonal_right+=1
                
            if counter_horizental == len(self.board) or counter_vertical == len(self.board):
                print("Hurray!! We found our winner")
                self.win = True
                print('our winner is ',pl)
                return True
                
        if counter_diagonal_left == len(self.board) or counter_diagonal_right == len(self.board):
                print("Hurray!! We found our winner")
                self.win = True
                print('our winner is ',pl)
                return True
        # check vertical

        return False

    def checkDraw(self):
        for i in range(len(self.block)):
            for j in range(len(self.block)):
                if self.block[i][j] == '-':
                    return False

        else:
            self.win = True
            print('The match has been drawn')
            return Trues


    def play(self):
        self.getPlayerDetails()
        self.printBoard()

        while not self.win:
            for pl,marker in self.player.items():
                print(pl,', This is your turn please enter and ',marker,' this is your marker')

                x,y = list(input().split(" "))
                while not (x.isnumeric() and y.isnumeric() and 0 < int(x)-1,int(y)-1 < len(self.board)   and self.board[int(x)-1][int(y)-1] == '-'):
                    print('this is incorrect move please enter your move again')
                    x,y = list(input().split(" "))

                self.board[int(x)-1][int(y)-1] = marker
                self.printBoard()
                if(self.checkWin(pl,marker)):
                    break
                if(self.checkDraw()):
                    break


obj = TicTacToe()
obj.play()