from aocd.models import Puzzle
import numpy as np


def chart(data, diagonals=True):
    #create a grid using max for each value
    grid = np.zeros((np.max(data)+1, np.max(data)+1), int)

    #draw line for each input value
    for x1,y1,x2,y2 in data:
        if x1 == x2:
            grid[min(y1,y2):max(y1,y2)+1, x1] += 1
        elif y1 == y2:
            grid[y1, min(x1,x2):max(x1,x2)+1] += 1
        elif diagonals:
            for x,y in  zip(range(x1,x2+1) if x2>x1 else range(x2,x1+1)[::-1],
                            range(y1,y2+1) if y2>y1 else range(y2,y1+1)[::-1]):
                grid[y, x] += 1
    return grid


def part1(input):
    data = [line.split('->')[i].strip().split(',') 
        for line in input for i in [0,1]]
    data = np.array(data, int).reshape(-1,4)

    hits = np.bincount(chart(data, diagonals=False).flatten())[2:].sum()
    
    print ("Part 1: {}".format(hits))


def part2(input):

    data = [line.split('->')[i].strip().split(',') 
        for line in input for i in [0,1]]
    data = np.array(data, int).reshape(-1,4)

    hits = np.bincount(chart(data, diagonals=True).flatten())[2:].sum()
    
    print ("Part 1: {}".format(hits))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=5)

    exampledata = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

    #part1(exampledata.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(exampledata.splitlines())
    part2(puzzle.input_data.splitlines())
