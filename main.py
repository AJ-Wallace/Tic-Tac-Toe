class grid():

    def __init__(self):
        self.grid = []

    def setGrid(self):
        for i in range(3):
            self.grid.append([' ',' ',' '])

    def dispGrid(self):
   
        print("   |   |   ")
        print("", self.grid[0][0],"|", self.grid[0][1],"|", self.grid[0][2],"")
        print("---|---|---")
        print("", self.grid[1][0],"|", self.grid[1][1],"|", self.grid[1][2],"")
        print("---|---|---")
        print("", self.grid[2][0],"|", self.grid[2][1],"|", self.grid[2][2],"")
        print("   |   |   ")

if __name__ == "__main__":
    grid = grid()
    grid.setGrid()
    grid.dispGrid()