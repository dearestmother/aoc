from aocd.models import Puzzle

def printOctopuses(octopuses):
    for y in range(len(octopuses)):
        for x in range(len(octopuses[0])):
            print(octopuses[y][x],end='')
        print()
    print()

def part1(input):
    octopuses = list()
    for d in input:
        octopuses.append([int(i) for i in list(d)])
    #printOctopuses(octopuses)
    flashes = 0

    for step in range(100):
        # list of octopuses that flashed during this step
        flashed = list()
        # increment all by one
        for y in range(len(octopuses)):
            for x in range(len(octopuses[0])):
                octopuses[y][x] += 1
        somethingChanged = True
        while somethingChanged:
            # assume that the situation has stabilized
            somethingChanged = False
            for y in range(len(octopuses)):
                for x in range(len(octopuses[0])):
                    # if the energy level is greater than 9
                    if (octopuses[y][x] > 9):
                        octopuses[y][x] = 0
                        flashes += 1
                        flashed.append((x,y))
                        # for each neighbour...
                        for nx,ny in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
                            # ...that exists on the board...
                            if (-1 < nx < len(octopuses[0]) and -1 < ny < len(octopuses)):
                                # ...increase its energy level 
                                octopuses[ny][nx] += 1
                        somethingChanged = True
                        # don't let multiple changes overlap
                        break
                if (somethingChanged):
                    break
        # "any octopus that flashed during this step has its energy level set to 0"
        for fx, fy in flashed:
            octopuses[fy][fx] = 0
        # print situation
        #print(f'after {s+1} steps:')
        #printOctopuses(octopuses)

    print ("Part 1: {}".format(flashes))

def part2(input):
    octopuses = list()
    for d in input:
        octopuses.append([int(i) for i in list(d)])
    #printOctopuses(octopuses)
    flashes = 0
    step = 0
    while True:
        # list of octopuses that flashed during this step
        flashed = list()
        # increment all by one
        for y in range(len(octopuses)):
            for x in range(len(octopuses[0])):
                octopuses[y][x] += 1
        somethingChanged = True
        while somethingChanged:
            # assume that the situation has stabilized
            somethingChanged = False
            for y in range(len(octopuses)):
                for x in range(len(octopuses[0])):
                    # if the energy level is greater than 9
                    if (octopuses[y][x] > 9):
                        octopuses[y][x] = 0
                        flashes += 1
                        flashed.append((x,y))
                        # for each neighbour...
                        for nx,ny in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
                            # ...that exists on the board...
                            if (-1 < nx < len(octopuses[0]) and -1 < ny < len(octopuses)):
                                # ...increase its energy level 
                                octopuses[ny][nx] += 1
                        somethingChanged = True
                        # don't let multiple changes overlap
                        break
                if (somethingChanged):
                    break
        # "any octopus that flashed during this step has its energy level set to 0"
        for fx, fy in flashed:
            octopuses[fy][fx] = 0
        step += 1
        # if the number of octopuses that flashed is equal to the total number of octopuses
        if (len(flashed) == len(octopuses) * len(octopuses[0])):
            break
    print ("Part 2: {}".format(step))

if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=11)

    example = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())
