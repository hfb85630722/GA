
Answers=[]

def get_size():
    while True:
        try:
            size = int(input('Please input the size! n = \n'))
            if size <= 3:
                print("Invalid value, it must be bigger than 3!")
                continue
            return size
        except ValueError:
            print("Must be integer, do it again!")

def board_creation(size):
    board = [0] * size
    for ix in range(size):
        board[ix] = [0] * size
    return board


def output_answers(answers):
    for sol in answers:
        # print(sol)
        for row in sol:
            print(row)
        print()


def check(board, row, col, size):
    # check row on left side
    for b in range(col):
        if board[row][b] == 1:
            return False
    # check top left side#往左上移动一次
    a, b = row, col
    while a >= 0 and b >= 0:
        if board[a][b] == 1:
            return False
        a -= 1
        b -= 1
    # check top bottom left side#往左下移动一次
    c, d = row, col
    while c < size and d >= 0:
        if board[c][d] == 1:
            return False
        c += 1
        d -= 1

    return True


def solver(board, col, size):
    """Use backtracking to find all solutions"""
    # base case
    if col >= size:
        return
    for i in range(size):
        if check(board, i, col, size):
            board[i][col] = 1
            if col == size - 1:
                add_answer(board)
                board[i][col] = 0
                return
            solver(board, col + 1, size)
            # backtrack
            board[i][col] = 0


def add_answer(board):
    import copy
    saved_board = copy.deepcopy(board)#如果没有这个函数 那么这个board总是在变
    Answers.append(saved_board)


size = get_size()

board = board_creation(size)

solver(board, 0, size)

output_answers(Answers)

print("You got {} in total".format(len(Answers)))

