# HakD_2022_Connect-4
### This is a project for HakD 2022: Game On.
#### Code by Shuntao Z., with help from Daniel H., Harrison W. and Eddie.
###### Music: www.bensound.com
You may use this code, and the win checking code is actually quite good, go check it out. Libraries used: Pygame, Art, Colorama
In main.py, between lines 155 and 192, you can find a wincheck section that can be aplied to multiple situations where you have to find a certain amount of the same character in a line in a 2D array. Simply change the `'Y'` and `'R'` in `for turn in ['Y','R']` to the values you want to check for (one for each team). If you want to check for different lengths, change the If statements. The function returns the winning symbol, "No" (The game has yet to finish) or "Draw" (A draw).
###### The original SFXs and Music have been added for your convenience.
```
def checkWin():
    for x in range(7):
        for y in range(7):
            for turn in ['Y', 'R']:
                try:
                    # Sideways line checking
                    if grid[x][y] == turn and grid[x][y + 1] == turn and grid[x][y + 2] == turn and grid[x][y + 3]: pass
                except:  # In case of a RangeError, meaning it checks for Board off the edge of the board
                    pass
                else:
                    if grid[x][y] == turn and grid[x][y + 1] == turn and grid[x][y + 2] == turn and grid[x][y + 3] == turn:
                        return turn
                try:  # Diagonal-right check
                    if grid[x][y] == turn and grid[x + 1][y + 1] == turn and grid[x + 2][y + 2] == turn and grid[x + 3][y + 3]: pass
                except:
                    pass
                else:
                    if grid[x][y] == turn and grid[x + 1][y + 1] == turn and grid[x + 2][y + 2] == turn and grid[x + 3][y + 3] == turn:
                        return turn
                try:  # Vertical Check
                    if grid[x][y] == turn and grid[x + 1][y] == turn and grid[x + 2][y] == turn and grid[x + 3][y]: pass
                except:
                    pass
                else:
                    if grid[x][y] == turn and grid[x + 1][y] == turn and grid[x + 2][y] == turn and grid[x + 3][y] == turn:
                        return turn
                try:  # Diagonal-left check
                    if grid[x][y] == turn and grid[x - 1][y + 1] == turn and grid[x - 2][y + 2] == turn and grid[x - 3][y + 3]: pass
                except:
                    pass
                else:
                    if grid[x][y] == turn and grid[x - 1][y + 1] == turn and grid[x - 2][y + 2] == turn and grid[x - 3][y + 3] == turn:
                        return turn
    for i in range(6):
        for j in range(7):
            if grid[i][j] == 0:
                return "No" # Checks for Tie (if there is any empty spaces in the top row after checking for a win)
    return "Draw"
```
