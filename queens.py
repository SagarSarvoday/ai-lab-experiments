N = 8

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_queens(board, row):
    if row == N:
        print_solution(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1):
                return True
            board[row] = -1  # Backtrack

    return False


def print_solution(board):
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Driver code
board = [-1] * N
solve_queens(board, 0)
