from aocd.models import Puzzle

def part1(input):
    counter = 0
    inputsize = len(input)

    for num in range(inputsize-1):
        if (int(input[num]) < int(input[num+1])):
            #print ("{} - {} = INC".format(input[num], input[num+1]))
            counter += 1
        #else: 
            #print ("{} - {} = DEC".format(input[num], input[num+1]))

    print ("Part 1: {}".format(counter))

def threesum(x,y,z):
    return x+y+z

def part2(input):
    counter = 0
    inputsize = len(input)

    currentsum = threesum(int(input[0]),int(input[1]),int(input[2]))
    for num in range(3, inputsize):
        nextsum = threesum(int(input[num-2]),int(input[num-1]),int(input[num]))
        if (currentsum < nextsum ):
            counter += 1
        currentsum = nextsum
    print ("Part 2: {}".format(counter))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=1)

    part1(puzzle.input_data.splitlines())
    part2(puzzle.input_data.splitlines())
