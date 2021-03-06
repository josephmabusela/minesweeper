import random

# Global assignments

dim_size = int(input("Enter dimensions: "))
mine_num = dim_size - 1
global nums

print()
print("\t\t\tMINESWEEPER\n")


# Function for drawing the board
def draw_board():
    i = 0
    # dim_sizes = [4, 8, 12]
    horizontal = "--- "
    vertical = "|   "
    horizontal = horizontal * dim_size
    vertical = vertical * (dim_size + 1)
    while i < dim_size + 1:
        print(horizontal)
        if not (i == dim_size):
            print(vertical)
        i += 1


print(draw_board())


# function for setting up the mines
def set_mines():
    mines_num = random.randint(0, dim_size - 1)

    # Track mines already set up
    count = 0
    while count < mines_num:
        val = random.randint(0, dim_size * dim_size - 1)
        row = val // dim_size
        col = val % dim_size

        # place the mine, if it doesn't exist
        if nums[row][col] != -1:
            count = count + 1
            nums[row][col] = -1


# Function for setting up the other grid values
def set_values():
    num = 0

    # Loop fot counting each cell value

    for r in range(dim_size):
        for col in range(dim_size):

            # if mine is there skip
            if num[r][col] == -1:
                continue

                # Check up
                if r > 0 and num[r - 1][col] == -1:
                    num[r][col] = num[r][col] + 1
                # Check down
                if r < dim_size - 1 and num[r + 1][col] == -1:
                    num[r][col] = num[r][col] + 1
                # Check left
                if col > 0 and num[r][col - 1] == -1:
                    num[r][col] = num[r][col] + 1
                # Check right
                if col < n - 1 and num[r][col + 1] == -1:
                    num[r][col] = num[r][col] + 1
                # Check top-left
                if r > 0 and col > 0 and num[r - 1][col - 1] == -1:
                    num[r][col] = num[r][col] + 1
                # Check top-right
                if r > 0 and col < n - 1 and num[r - 1][col + 1] == -1:
                    num[r][col] = num[r][col] + 1
                # Check below-left
                if r < dim_size - 1 and col > 0 and num[r + 1][col - 1] == -1:
                    num[r][col] = num[r][col] + 1
                # Check below-right
                if r < dim_size - 1 and col < n - 1 and num[r + 1][col + 1] == -1:
                    num[r][col] = num[r][col] + 1


# function to show all the 0's

inp = input("Enter row number followed by space and column number = ")
