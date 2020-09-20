import random

class GameState:
    board = list()
    count_token_for_win = 3

    def __init__(self, n, k):
        self.board = empty_board(n)
        self.count_token_for_win = k

    def set_board(self, board):
        self.board = board

    def generate_possible_moves(self):
        moves = [];
        n = len(self.board)
        for i in range(n):
            for j in range(n):
                if self.board[i][j] == ".":
                    moves.append([i,j])
        return moves

    def state_is_terminal(self):
        k = self.count_token_for_win
        n = len(self.board)
        is_terminal = False
        win_coord = []
        for j in range(n):
            i = 0
            while n - i >= k:
                moves = list()
                for l in range(k):
                    moves.append([i + l, j])
                win_coord.append(moves)
                i+=1
        for i in range(n):
            j = 0
            while n - j >= k:
                moves = list()
                for l in range(k):
                    moves.append([i, j + l])
                win_coord.append(moves)
                j+=1
        # for i in range(n):
        #     j = 0
        #     while n - j < k:
        #         moves = set()
        #         for l in range(k):
        #             moves.add([i, j + l])
        #         win_coord.append(moves)
        #     win_coord.append({[i + l, j + l]})

        for each in win_coord:
            for l in range(1,k-1):
                is_terminal = self.board[each[l-1][0]][each[l-1][1]] == self.board[each[l][0]][each[l][1]] \
                              and self.board[each[l-1][0]][each[l-1][1]] != "." \
                              and self.board[each[l][0]][each[l][1]] != "."
            if is_terminal:
                print(each)
                break
        print("win_coord = ", win_coord)
        return is_terminal



    def empty_board(n):
        return ["." * n for _ in range(n)]

    def draw_board(self):
        for row in self.board:
            print()
            for el in row:
                print(el, end='')

def draw_board(board):
    for row in board:
        print()
        for el in row:
            print(el, end='')

def empty_board(n):
    return ["."*n for _ in range(n)]

def take_input(player_token, board):
    valid = False
    n = len(board)
    while not valid:
        x, y = input("\nКуда поставим " + player_token + "? ").split()
        try:
            x, y = int(x), int(y)
        except:
            print
            "Некорректный ввод. Вы уверены, что ввели число?"
            continue
        if x >= 1 and x <= n and y >= 1 and y <= n:
            if (board[x-1][y-1] not in "XO"):
                board[x-1] = board[x-1][:y-1] + player_token + board[x-1][y:]
                valid = True
            else:
                print
                "Эта клеточка уже занята"
        else:
            print
            "Некорректный ввод. Введите число от 0 до", n-1, " чтобы походить."

def move(board, player_token, x, y):
        board[x] = board[x][:y] + player_token + board[x][y+1:]

A = GameState(3, 3)
win = False
counter = 0
board = empty_board(3)
A.draw_board()
while not win:
    if counter % 2 == 0:
        take_input("X", board)
        A.set_board(board)
        win = A.state_is_terminal()
    if win:
        break
    x, y = random.choice(A.generate_possible_moves())
    move(board, "O", x, y)
    A.set_board(board)
    A.draw_board()

print("GAME OVER")