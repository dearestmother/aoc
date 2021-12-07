from aocd.models import Puzzle
import numpy as np
import sys

def part1(input):
    crabs = np.array(input)

    minfuel = sys.maxsize

    minpoint = -1

    for point in range(crabs.min(), crabs.max()):
        fuel = 0
        for crab in crabs:
            fuel += abs(crab - point)
        if fuel < minfuel:
            minfuel = fuel
            minpoint = point

    print ("Part 1: {}".format(minfuel))

def part2(input):
    crabs = np.array(input)

    minfuel = sys.maxsize

    minpoint = -1

    for point in range(crabs.min(), crabs.max()):
        fuel = 0
        for crab in crabs:
            for x in range(abs(crab - point)):
                fuel += 1 + x
        if fuel < minfuel:
            minfuel = fuel
            minpoint = point
    print ("Part 2: {}".format(minfuel))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=7)

    example = [16,1,2,0,4,2,7,1,2,14]

    #part1(example)
   
    part1(list(map(int, puzzle.input_data.split(","))))
    #part2(example)
    part2(list(map(int, puzzle.input_data.split(","))))
