class grid():

    def __init__(self):
        self.grid = []
        self.selector = ''
        self.turn = 1

    def setGrid(self):
        for i in range(3):
            self.grid.append([' ',' ',' '])

    def dispGrid(self):

        print("   1   2   3 ")
        print("     |   |   ")
        print("A ", self.grid[0][0],"|", self.grid[0][1],"|", self.grid[0][2],"")
        print("  ---|---|---")
        print("B ", self.grid[1][0],"|", self.grid[1][1],"|", self.grid[1][2],"")
        print("  ---|---|---")
        print("C ", self.grid[2][0],"|", self.grid[2][1],"|", self.grid[2][2],"")
        print("     |   |   ")

    def getMove(self):
        validCoord = ["A3","A1",'A2','B3','B1','B2','C3','C1','C2']
        coord = input("Select a position: ").upper()

        while coord not in validCoord:
            print("Invalid Coord", end='\r')
            coord = input("Select a position: ").upper() 

        match coord:
            case "A1":
                self.grid[0][0] = self.selector
            case "A2":
                self.grid[0][1] = self.selector
            case "A3":
                self.grid[0][2] = self.selector
            case "B1":
                self.grid[1][0] = self.selector
            case "B2":
                self.grid[1][1] = self.selector
            case "B3":
                self.grid[1][2] = self.selector
            case "C1":
                self.grid[2][0] = self.selector
            case "C2":
                self.grid[2][1] = self.selector
            case "C3":
                self.grid[2][2] = self.selector

    def switchPlayer(self):
        if self.turn % 2 == 0:
            self.selector = 'O'
        else:
            self.selector = 'X'

    def checkWin(self):
        lines = [
            [self.grid[0][0], self.grid[0][1], self.grid[0][2]],
            [self.grid[1][0], self.grid[1][1], self.grid[1][2]],
            [self.grid[2][0], self.grid[2][1], self.grid[2][2]],
            [self.grid[0][0], self.grid[1][0], self.grid[2][0]],
            [self.grid[0][1], self.grid[1][1], self.grid[2][1]],
            [self.grid[0][2], self.grid[1][2], self.grid[2][2]],
            [self.grid[0][0], self.grid[1][1], self.grid[2][2]],
            [self.grid[2][0], self.grid[1][1], self.grid[0][2]],
        ]
        
        for line in lines:
            if line[0] == line[1] == line[2] != ' ':
                if line[0] == "X":
                    return "X"
                else:
                    return 'O'

if __name__ == "__main__":
    play = True
    winner = None

    grid = grid()
    grid.setGrid()

    while play == True:
        grid.dispGrid()
        grid.switchPlayer()
        grid.getMove()
        winner = grid.checkWin()
        if winner == None:
            grid.turn += 1
        else:
            grid.dispGrid()
            print(winner,"Wins!")
            play = False