from ast import And
from operator import truediv
from aocd.models import Puzzle

def getboard(inputlist):
    board = [None] * 5
    for count in range(5):
        values = inputlist.pop(0)
        values = values.replace("  ", " ").lstrip()
        board[count] = (list(map(int,values.split(" "))))

    #pop the blank row
    if (len(inputlist) > 0):
        inputlist.pop(0)
    return board

def sumboard(board):
    sum = 0
    for y in range(5):
        for x in range(5):
            if (board[x][y] != -1):
                sum = sum + board[x][y]
    return sum

def checkboard(board):
    #check X Axis
    for x in range(5):
        if (board[x].count(-1) == 5):
            #bingo found
            return sumboard(board)
    #check Y Axis
    for y in range(5):
        if ((board[0][y] == -1) and
            (board[1][y] == -1) and
            (board[2][y] == -1) and
            (board[3][y] == -1) and
            (board[4][y] == -1)):
            #bingo found
                return sumboard(board)

    return 0

def part1(input):

    draws = list(map(int, input[0].split(",")))

    boardsinput = input.copy()
    boardsinput.pop(0)
    boardsinput.pop(0)

    boards = []
    while (len(boardsinput)>0):
        boards.append(getboard(boardsinput))

    for draw in draws:
        for board in boards:
            for ycount in range(5):
                for xcount in range(5):
                    if board[xcount][ycount] == draw:
                        board[xcount][ycount] = -1
            retval = checkboard(board)
            if (retval > 0):
                print ("Part 1: {}".format(retval * draw) )
                return

def part2(input):
    draws = list(map(int, input[0].split(",")))

    boardsinput = input.copy()
    boardsinput.pop(0)
    boardsinput.pop(0)

    boards = []
    while (len(boardsinput)>0):
        boards.append(getboard(boardsinput))

    for draw in draws:
        for board in boards:
            for ycount in range(5):
                for xcount in range(5):
                    if board[xcount][ycount] == draw:
                        board[xcount][ycount] = -1
        prevboards = boards.copy() 
        boards = [board for board in boards if checkboard(board) == 0]        
        if (len(boards) == 0):
            retval = sumboard(prevboards[0])
            print ("Part 2: {}".format(retval * draw) )
            return


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=4)

    example="""7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())
