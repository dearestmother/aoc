from aocd.models import Puzzle


def part1(input):
    gamma = ""
    epsilon = ""
    
    
    for position in range(len(input[0])):
        bit0 = 0
        bit1 = 0
        for item in input:
            if item[position] == "0":
                bit0 += 1
            else:
                bit1 += 1
        if (bit0 > bit1):
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    #print("Gamma: {}".format(int(gamma, 2)))
    #print("Epsilon: {}".format(int(epsilon, 2)))

    returnval = int(gamma, 2) * int(epsilon, 2)

    print ("Part 1: {}".format(returnval))

def valueCheck(item, position, checkvalue):
    return bool(item[position] == checkvalue)

def findMostCommon(values, largest):
    input = values.copy()
    for position in range(len(input[0])):
        bit0 = 0
        bit1 = 0

        for item in input:
            if item[position] == "0":
                bit0 += 1
            else:
                bit1 += 1

        if (largest):
            if (bit1 >= bit0) :
                input = [value for value in input if valueCheck(value,position,"1")]    
            else:
                input = [value for value in input if valueCheck(value,position,"0")]    
        else:
            if (bit1 >= bit0) :
                input = [value for value in input if valueCheck(value,position,"0")]    
            else:
                input = [value for value in input if valueCheck(value,position,"1")]

        if (len(input) == 1):
            return input[0]

    return(input[0])


def part2(input):    
    Oxygen = findMostCommon(input, True) 
    CO2Scubber = findMostCommon(input, False)

    returnval = int(Oxygen, 2) * int(CO2Scubber, 2)

    print ("Part 2: {}".format(returnval))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=3)

    exampledata = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

    #part1(exampledata)
    part1(puzzle.input_data.splitlines())
    #part2(exampledata)
    part2(puzzle.input_data.splitlines())
