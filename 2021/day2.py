from aocd.models import Puzzle

def part1(input):
    x = 0
    y = 0
    
    for command in input:
        splitcommand = command.split(" ")
        match(splitcommand[0]):
            case "forward":
                x += int(splitcommand[1])
            case "up":
                y -= int(splitcommand[1])
            case "down":
                y += int(splitcommand[1])
            case _:
                print("Huh?")
    print ("Part 1: {}".format(x*y))

def part2(input):
    x = 0
    y = 0
    aim = 0

    for command in input:
        splitcommand = command.split(" ")
        match(splitcommand[0]):
            case "forward":
                x += int(splitcommand[1])
                y = y + (aim * int(splitcommand[1]))
            case "up":
                #y -= int(splitcommand[1])
                aim -= int(splitcommand[1])
            case "down":
                #y += int(splitcommand[1])
                aim += int(splitcommand[1])
            case _:
                print("Huh?")
    print ("Part 2: {}".format(x*y))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=2)

    testdata=["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


    part1(puzzle.input_data.splitlines())
    part2(testdata)
    part2(puzzle.input_data.splitlines())
