from aocd.models import Puzzle
import numpy as np

def part1(input):
    cavemap = np.zeros((len(input[0]), len(input)))

    row = 0
    for line in input:
        column = 0
        for char in line:
            cavemap[column,row] = char
            column += 1
        row += 1

    riskcount = 0

    for y in range(cavemap.shape[1]):
        for x in range(cavemap.shape[0]):
            lowest = True
            #Left
            if (x > 0):
                if (cavemap[x,y] >= cavemap[x-1,y]):
                    lowest = False
            #Right
            if (x < cavemap.shape[0] - 1):
                if (cavemap[x,y] >= cavemap[x+1,y]):
                    lowest = False
            #Up
            if (y > 0):
                if (cavemap[x,y] >= cavemap[x,y-1]):
                    lowest = False
            #Down
            if (y < cavemap.shape[1] - 1):
                if (cavemap[x,y] >= cavemap[x,y+1]):
                    lowest = False
            if (lowest):
                riskcount += cavemap[x,y] + 1

    #print (cavemap)
    print ("Part 1: {}".format(riskcount))


def basin_coords(input_, coords):
    n = len(input_)
    coords_increasing = []
    for (x,y) in coords:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            xdx, ydy = x+dx, y+dy
            if (xdx, ydy) in coords_increasing:
                continue
            if not (0 <= xdx < n and 0 <= ydy < n):
                continue
            a = input_[xdx, ydy]            
            if a < 9 and a > input_[x, y]:
                coords_increasing.append((xdx, ydy))
    if len(coords_increasing) == 0:
        return coords
    else: # How to better avoid duplicates than to remove at the end?
        return list(set(coords + basin_coords(input_, coords_increasing)))


def part2(input):
    input2 = np.array([list(map(int, x)) for x in input])
    is_local_minimum = np.ones_like(input2, dtype=bool)
    min_coords = list(zip(*np.where(is_local_minimum)))
    basin_sizes = [len(basin_coords(input2, [c])) for c in min_coords]

    print ("Part 2: {}".format(np.sort(basin_sizes)[-3:].prod()))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=9)
    example="""2199943210
3987894921
9856789892
8767896789
9899965678"""
    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())
