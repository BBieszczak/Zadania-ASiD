# Zad 1
print("ZADANIE 1")
signs = ['A', 'B', 'C', 'D']
words = []
word = ''
backtrack = 0

for i in range(len(signs)):
    for j in range(len(signs)):
        for k in range(len(signs)):
            word = ''
            word += signs[i]
            if signs[i] == 'A' and signs[j] == 'A':
                j += 1
                backtrack += 1
            word += signs[j]
            if signs[j] == 'A' and signs[k] == 'A':
                k += 1
                backtrack += 1
            word += signs[k]
            words.append(word)
print(words)
print(f'Ilość słów: {str(len(words))}')
print(f'Ilość cofnięć: {str(backtrack)}\n')

# Zad 2
print("ZADANIE 2")
osoby_zadania = [[10,20,40],[20,15,5],[8,16,24]]
finalne_zadania = [0,0,0]
max = max(osoby_zadania[0] + osoby_zadania[1] + osoby_zadania[2])
breach = 0
for i in range(3):
    for j in range(3):
        for k in range(3):
            start = 0
            start += osoby_zadania[0][i]
            if(start > max):
                breach += 1
                break
            start += osoby_zadania[1][j]
            if(start > max or i == j):
                breach += 1
                break
            start += osoby_zadania[2][k]
            if(start > max or i == k or j == k):
                breach += 1
                break
            max = start
print(f'Minimalny koszt: {str(max)}')
print(f'Ilość cięć: {str(breach)}\n')

# Zad 3
print("ZADANIE 3")
ROWS, COLS = 4, 4
PIECES = {
    "I": [ [(0,0), (1,0), (2,0), (3,0)],       # pionowo
           [(0,0), (0,1), (0,2), (0,3)] ],     # poziomo
    "L": [ [(0,0), (1,0), (2,0), (2,1)],       # standardowe L
           [(0,0), (0,1), (0,2), (1,0)],       # odwrócone
           [(0,0), (0,1), (1,1), (2,1)],       # L w prawo
           [(1,0), (1,1), (1,2), (0,2)] ]      # L w górę
}
def can_place(board, shape, row, col):
    for dr, dc in shape:
        r, c = row + dr, col + dc
        if not (0 <= r < ROWS and 0 <= c < COLS):
            return False
        if board[r][c] != '.':
            return False
    return True

def place_piece(board, shape, row, col, mark):
    for dr, dc in shape:
        r, c = row + dr, col + dc
        board[r][c] = mark

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def solve(board, pieces_left):
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == '.':
                break
        else:
            continue
        break
    else:
        print("Znaleziono rozwiązanie:")
        print_board(board)
        return True

    for name in pieces_left:
        for shape in PIECES[name]:
            if can_place(board, shape, r, c):
                place_piece(board, shape, r, c, name)
                new_pieces = pieces_left.copy()
                new_pieces.remove(name)
                if solve(board, new_pieces):
                    return True
                place_piece(board, shape, r, c, '.')
    return False

board = [['.']*4]*4
pieces_to_use = ["L", "L", "I", "I"]
if not solve(board, pieces_to_use):
    print("Brak rozwiązania.")

# Zad 4
print("ZADANIE 4")
answers , answers2 = [], []
n = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            if i + j + k == 15:
                if i != j and i != k and j != k:
                    if i != 0 and j != 0 and k != 0:
                        answers.append([i,j,k])

for i in range(len(answers)):
    for j in range(len(answers)):
        for k in range(len(answers)):
            if i != j and i != k and j != k:
                if not set(answers[i]) & set(answers[j]):
                    if not set(answers[i]) & set(answers[j]):
                        if not set(answers[j]) & set(answers[k]):
                            answers2.append([answers[i],answers[j],answers[k]])

for i in range(len(answers2)):
    if answers2[i][0][0] + answers2[i][1][1] + answers2[i][2][2] == 15:
        if answers2[i][0][2] + answers2[i][1][1] + answers2[i][2][0] == 15:
            if answers2[i][0][0] + answers2[i][1][0] + answers2[i][2][0] == 15:
                if answers2[i][0][1] + answers2[i][1][1] + answers2[i][2][1] == 15:
                    if answers2[i][0][2] + answers2[i][1][2] + answers2[i][2][2] == 15:
                        print(answers2[i])
                        n += 1

print(f'Ilość rozwiązań: {n}')

# ZADANIE 5
words = ["frog", "ball", "road", "tide", "boo", "lab"]
final_words = []
word = ""
grid = [
    ["f", "r", "r", "t"],
    ["b", "o", "o", "i"],
    ["a", "g", "a", "d"],
    ["l", "l", "x", "e"]
]

def move():
    return None

visited = [[False]*4]*4
for i in range(4):
    for j in range(4):
        word = grid[i][j]
        for k in range(16):
            word += ""