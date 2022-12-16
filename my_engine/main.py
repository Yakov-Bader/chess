import json
import chess
import time
# from in the folder my_engine c:\users\yakov\appdata\local\packages\pythonsoftwarefoundation.python.3.8_qbz5n2kfra8p0\localcache\local-packages\python38\scripts\pyinstaller  --onefile main.py

class Node:

    def __init__(self, move, val):
        self._children = []
        self._val = val
        self._father= None
        self._children_max = -100000
        self._children_min = 100000
        self._move = move

    def add_child(self, child):
        self._children.append(child)
        child.father = self

    @property
    def father(self):
        return self._father

    @father.setter
    def father(self, father):
        self._father = father

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val

    @property
    def children_max(self):
        return self._children_max

    @children_max.setter
    def children_max(self, children_max):
        self._children_max = children_max

    @property
    def children_min(self):
        return self._children_min

    @children_min.setter
    def children_min(self, children_min):
        self._children_min = children_min

    @property
    def move(self):
        return self._move

    @property
    def children(self):
        return self._children

def get_max(root, depth):
    for child in root.children:
        val = get_best(child, depth-1)
        if val > root.children_max:
            root.val = child.val
            root.children_max=val
            if  root.father!=None and root.father.val!=None and (root.children_max > root.father.children_min):
                break
    return root.val


def get_min(root, depth):
    for child in root.children:
        val = get_best(child, depth-1)
        if val < root.children_min:
            root.children_min=val
            root.val = child.val
            if root.father.val!=None and (root.children_min < root.father.children_max):
                break
    return root.val


def get_best(root, depth):
    # with dfs set tree with min max
    if root.children != []:
        if depth % 2 == 0:  # blacks move
            return get_max(root, depth)
        else:
            return get_min(root, depth)
    return root.val


def get_sums(board, values):
    black_sum = 0
    white_sum = 0
    for (piece, value) in [(chess.PAWN, values[6]["value"]), (chess.ROOK, values[7]["value"]), (chess.KNIGHT, values[8]["value"]), (chess.BISHOP, values[9]["value"]), (chess.QUEEN, values[10]["value"]), (chess.KING, values[11]["value"])]:
        black_sum += len(board.pieces(piece, False)) * value
    for (piece, value) in [(chess.PAWN, values[0]["value"]), (chess.ROOK, values[1]["value"]), (chess.KNIGHT, values[2]["value"]), (chess.BISHOP, values[3]["value"]), (chess.QUEEN, values[4]["value"]), (chess.KING, values[5]["value"])]:
        white_sum += len(board.pieces(piece, True)) * value
    return black_sum, white_sum


def create_tree(root, board, depth, values):
    if depth > 0:
        for move in board.legal_moves:
            move_val = None
            board.push(move)
            if board.is_checkmate():
                move_val = 1000
            elif depth == 1:
                black_sum, white_sum = get_sums(board, values)
                move_val = black_sum-white_sum
            child = Node(str(move), move_val)
            root.add_child(child)
            create_tree(child, board, depth-1, values)
            board.pop()


def find(board):
    file = open("yakov/Python-Easy-Chess-GUI-master/pecg_engines.json", "r")
    data = json.load(file)
    values = []
    for engine in data:
        if engine["name"] == "yakov":
            values = engine["options"]
            break
    depth = 4
    root = Node(None, 0)
    start_tree = time.time()
    create_tree(root, board, depth, values)
    print("creating tree took {} seconds".format(time.time() - start_tree))
    start_time = time.time()
    get_best(root, depth)
    print("getting best took {} seconds".format(time.time() - start_time))
    for child in root.children:
        if child.val == root.val:
            return child.move
    


if __name__ == "__main__":

    board = chess.Board()

    board.push(chess.Move.from_uci("e2e4"))
    board.push(chess.Move.from_uci(find(board)))
    print(board)
    print('_____________________')
    board.push(chess.Move.from_uci("d1f3"))
    board.push(chess.Move.from_uci(find(board)))
    print(board)
    # print('_____________________')
    # board.push(chess.Move.from_uci("f1c4"))
    # board.push(chess.Move.from_uci(find(board)))
    # print(board)
    # print('_____________________')
    # board.push(chess.Move.from_uci("f3g3"))
    # board.push(chess.Move.from_uci(find(board)))
    # print(board)

