import random
def minesweeper(n):
    arr = [[0 for row in range(n)] for column in range(n)]
    for num in range(2):
        x = random.randint(0,4)
        y = random.randint(0,4)
        arr[y][x] = 'X'
        if (x >=0 and x <= 3) and (y >= 0 and y <= 4):
            arr[y][x+1] += 1 # center right
        if (x >=1 and x <= 4) and (y >= 0 and y <= 4):
            arr[y][x-1] += 1 # center left
        if (x >= 1 and x <= 4) and (y >= 1 and y <= 4):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1 # top left
        if (x >= 0 and x <= 3) and (y >= 1 and y <= 4):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1 # top right
        if (x >= 0 and x <= 4) and (y >= 1 and y <= 4):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1 # top center
        if (x >=0 and x <= 3) and (y >= 0 and y <= 3):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1 # bottom right
        if (x >= 1 and x <= 4) and (y >= 0 and y <= 3):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1 # bottom left
        if (x >= 0 and x <= 4) and (y >= 0 and y <= 3):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1 # bottom center
    for row in arr:
        print("\t".join(str(cell) for cell in row))
        print("")
if __name__ == "__main__":
    minesweeper(5)
def minesweeper(n, k):
    arr = [[0 for row in range(n)] for column in range(n)]
    for num in range(k):
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        arr[y][x] = 'X'
        if (x >=0 and x <= 3) and (y >= 0 and y <= 4):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1 # center right
        if (x >=1 and x <= 4) and (y >= 0 and y <= 4):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1 # center left
        if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1 # top left
        if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1 # top right
        if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1 # top center
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1 # bottom right
        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1 # bottom left
        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1 # bottom center
    for row in arr:
        print("\t".join(str(cell) for cell in row))
        print("")
if __name__ == "__main__":
    minesweeper(5, 3) # beginner
    minesweeper(6, 8) # intermediate
    minesweeper(8, 20) # advanced