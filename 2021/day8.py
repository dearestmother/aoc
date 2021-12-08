from aocd.models import Puzzle
import numpy as np
from collections import Counter

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


def decode_dictionary(inp):
    digits = {}
    five_len, six_len = [], []

    for digit in inp:
        if len(digit) == 2:
            digits["1"] = set(digit)
        elif len(digit) == 4:
            digits["4"] = set(digit)
        elif len(digit) == 3:
            digits["7"] = set(digit)
        elif len(digit) == 7:
            digits["8"] = set(digit)
        elif len(digit) == 5:
            five_len.append(set(digit))
        elif len(digit) == 6:
            six_len.append(set(digit))

    for digit in five_len:
        # 2, 3, 5
        if len(digit & digits["1"]) and len(digit & digits["4"]) == 2:
            digits["2"] = digit
        elif len(digit & digits["7"]) == 3:
            digits["3"] = digit
        elif len(digit & digits["1"]) == 1 and len(digit & digits["4"]) == 3:
            digits["5"] = digit

    for digit in six_len:
        # 6, 9, 0
        if len(digit & digits["1"]) == 1:
            digits["6"] = digit
        elif len(digit & digits["4"]) == 4:
            digits["9"] = digit
        elif len(digit & digits["4"]) == 3:
            digits["0"] = digit

    decoded = {"".join(sorted(v)): k for k, v in digits.items()}
    return decoded


def part2(input):
    problem = []
    for line in input:
        inp, out = line.split("|")
        inp, out = inp.split(), out.split()
        problem.append((inp, out))
    
    sum = 0
    for inp, out in problem:
        decoded = decode_dictionary(inp)
        result = []
        for digit in out:
            digit = "".join(sorted(digit))
            result.append(decoded[digit])
        sum += int("".join(result))
    print ("Part 2: {}".format(sum))


    #digits = ['','','','','','','','','']
#
    #for line in input:
#
    #    # Find the ones we know
    #    values = line.split("|")[0].split(" ")
    #    for value in values:
    #        match len(value):
    #            case 2:
    #                digits[1] = value
    #            case 3:
    #                digits[3] = value
    #            case 4:
    #                digits[4] = value
    #            case 7:
    #                digits[8] = value
    #    for value in values:
    #        if len(value) == 6:
    #            # 0, 6, 9
    #            for
#
    ## 0: left from 6: and 9:
    ## 2: left from 3: and 5:
    ## 3: (Candidate - 1) -> 3 segments left
    ## 5: (candidate - 4) -> 2 segments left
    ## 6: (8 - candidate) intersect 1
    ## 9: (Candidate - 4) -> 2 segments left
    #part_two = 0
    #for line in input:
    #    p = process_line(line)
    #    part_two += int("".join([str(x) for x in p]))
    #


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
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())
