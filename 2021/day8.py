from aocd.models import Puzzle
import numpy as np

def part1(input):
    digitcounts = np.zeros(10)
    for line in input:
        values = line.split("|")[1].split(" ")
        for value in values:
            valuelength = len(value)
            match valuelength:
                case 2:
                    digitcounts[1] += 1
                case 3:
                    digitcounts[7] += 1
                case 4:
                    digitcounts[4] += 1
                case 7:
                    digitcounts[8] += 1

    print ("Part 1: {}".format(int(np.sum(digitcounts))))

def part2(input):

    print ("Part 2: {}".format(0))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=8)

    example = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |fgae cfgab fg bagce"""

    #part1(example.splitlines())
    #part1(puzzle.input_data.splitlines())
    part2(example.splitlines())
    #part2(puzzle.input_data.splitlines())
