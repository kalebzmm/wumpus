import queue
import os
import time


def clear(): return os.system('cls')


cheeses = {}


def pathPrettyPrint(path):
    return path.replace('U', '↑').replace('R', '→').replace('D', '↓').replace('L', '←')


def readmap():
    with open('./map.txt') as file:
        lines = file.readlines()
        return [list(line.rstrip()) for line in lines]


def isAgent(e):
    return e == 'A'


def isBreeze(e):
    return e == 'B'


def isPit(e):
    return e == 'P'


def isStench(e):
    return e == 'S'


def isGold(e):
    return e == 'G'


def isWall(e):
    return e == '#'


def findStart(map):
    for x, pos in enumerate(map):
        if isAgent(pos[1]):
            return x


def valid(map, start, moves):
    x = 0
    y = start
    for move in moves:
        if move == "L":
            x -= 1

        elif move == "R":
            x += 1

        elif move == "U":
            y -= 1

        elif move == "D":
            y += 1

        if not (0 <= x < len(map[0]) and 0 <= y < len(map)):
            return False
        elif isWall(map[y][x]):
            return False
        elif isPit(map[y][x]):
            # print('PIT')
            ''
        elif isBreeze(map[y][x]):
            # print('BREEZE')
            ''
        elif isStench(map[y][x]):
            # print('STENCH')
            ''
        elif isGold(map[y][x]):
            # print('GOLD')
            ''

    return True


def findEnd(map, start, moves):
    x = 0
    y = start
    for move in moves:
        if move == "L":
            x -= 1

        elif move == "R":
            x += 1

        elif move == "U":
            y -= 1

        elif move == "D":
            y += 1

    # if isEnd(map[y][x]):
    #     clear()
    #     print('Encontrado em', "%s segundos" % (time.time() - start_time), ':', pathPrettyPrint(add))
    #     printMap(map, start, add)
    #     return True

    return False


def printMap(map, start, path=""):
    x = 0
    y = start
    pos = set()
    for move in path:
        if move == "L":
            x -= 1

        elif move == "R":
            x += 1

        elif move == "U":
            y -= 1

        elif move == "D":
            y += 1

        pos.add((y, x))

    for y, row in enumerate(map):
        for x, col in enumerate(row):
            if (y, x) in pos:
                print("\033[92m" + "@ " + "\033[0m", end="")
            else:
                print("\033[91m" + col + " \033[0m", end="")
        print()


def validMoves(map, lastMove):
    moves = ["L", "R", "U", "D"]
    if(not lastMove):
        return moves
    moves.remove(lastMove)
    moves.insert(0, lastMove)
    if(lastMove == 'R'):
        moves.remove('L')
    if(lastMove == 'L'):
        moves.remove('R')
    if(lastMove == 'U'):
        moves.remove('D')
    if(lastMove == 'D'):
        moves.remove('U')
    return moves


nums = queue.Queue()
add = ""
nums.put(add)
map = readmap()
start = findStart(map)
lastPos = (start, 0)  # y, x
lastMove = ''
start_time = time.time()

while not findEnd(map, start, add):
    add = nums.get()
    clear()
    moves = validMoves(map, lastMove)
    print('Tentativa: ', moves, pathPrettyPrint(add))
    printMap(map, start, add)
    for j in moves:
        put = add + j
        if valid(map, start, put):
            nums.put(put)
            lastMove = j
            continue
