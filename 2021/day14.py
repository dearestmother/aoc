from aocd.models import Puzzle
from collections import Counter

def poly_element_count(polymer, rules, iterations=10):
    element_counts = Counter(polymer)
    pair_counts = Counter(polymer[i:i+2] for i in range(len(polymer)-1))
    for _ in range(iterations):
        pair_counts_new = Counter()
        for pair, n in pair_counts.items():
            p1, p2 = pair
            insert = rules[pair]
            pair_counts_new[p1+insert] += n
            pair_counts_new[insert+p2] += n
            element_counts[insert] += n
        pair_counts = pair_counts_new

    return element_counts

def part1(input):
    polymer = input[0]
    rules = {r[0]: r[1] for r in map(lambda x: x.split(' -> '), input[2:])}
    
    counts = poly_element_count(polymer, rules).most_common()
    answer = counts[0][1] - counts[-1][1]

    print ("Part 1: {}".format(answer))

def part2(input):
    polymer = input[0]
    rules = {r[0]: r[1] for r in map(lambda x: x.split(' -> '), input[2:])}

    counts = poly_element_count(polymer, rules, iterations=40).most_common()
    answer = counts[0][1] - counts[-1][1]
    
    print ("Part 2: {}".format(answer))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=14)

    example = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())
