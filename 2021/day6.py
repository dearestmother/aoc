from aocd.models import Puzzle

fishlist = []
def simulateday():
    global fishlist
    appendcount = 0
    fishlistlen = len(fishlist)
    for x in range(fishlistlen):
        fishlist[x] -= 1
        if fishlist[x] == -1:
            fishlist[x] = 6
            appendcount += 1
    for x in range(appendcount):
        fishlist.append(8)

def part1(input):
    global fishlist
    fishlist = input.copy()
    for x in range(80):
        simulateday()

    print ("Part 1: {}".format(len(fishlist)))

def n_fishes(data: list[int], n_days: int, n_states=9):
    states = [0] * n_states
    for val in data:
        states[val] += 1
    for _ in range(n_days):
        nb_zeros = states[0]
        states = states[1:] + [nb_zeros]
        states[6] += nb_zeros
    return sum(states)

def part2(input):
    global fishlist
    fishlist = input.copy()

    #using simulateday would take A LONG TIME 
    #for x in range(256):
    #    simulateday()
    #print ("Part 2: {}".format(len(fishlist)))
    
    #Just use a count of each fish in each state
    #And move than count between days
    fishcount = n_fishes(fishlist, 256)
    print ("Part 2: {}".format(fishcount))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=6)

    example = [3,4,3,1,2]
    #part1(example)
    part1(list(map(int,(puzzle.input_data.split(",")))))
    #part2(example)
    part2(list(map(int,(puzzle.input_data.split(",")))))
