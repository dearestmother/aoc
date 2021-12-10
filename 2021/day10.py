from aocd.models import Puzzle
import statistics

def part1(input):
    syntaxsets = ["()", "{}", "[]", "<>"]
    score = 0

    for x in range(len(input)):
        matchFound = True

        #Remove all the matches
        while matchFound:
            matchFound = False
            for syntax in syntaxsets:
                if (input[x].find(syntax) > -1):
                    matchFound = True
                    input[x] = input[x].replace(syntax, "")

        print(input)

        #Remove all the leading chars. That way the first char in string is the first error
        for syntax in syntaxsets:
            input[x] = input[x].replace(syntax[0], "")

        if (len(input[x]) > 0):
            match input[x][0]:
                case ")":
                    score += 3
                case "]":
                    score += 57
                case "}":
                    score += 1197
                case ">":
                    score += 25137

    #print(input)

    print ("Part 1: {}".format(score))

def part2(input):
    syntaxsets = ["()", "{}", "[]", "<>"]
    scores = []

    for x in range(len(input)):
        matchFound = True

        #Remove all the matches
        while matchFound:
            matchFound = False
            for syntax in syntaxsets:
                if (input[x].find(syntax) > -1):
                    matchFound = True
                    input[x] = input[x].replace(syntax, "")

        #Remove all the corrupt lines.
        for syntax in syntaxsets:
            if (input[x].find(syntax[1]) > 0):
                input[x] = ""
            
        if (len(input[x]) > 0):
            input[x] = input[x][::-1]
            #for syntax in syntaxsets:
            #    input[x] = input[x].replace(syntax[0], syntax[1])
            
            score = 0
            for y in range(len(input[x])):
                match input[x][y]:
                    case "(":
                        score = (score * 5) + 1
                    case "[":
                        score = (score * 5) + 2
                    case "{":
                        score = (score * 5) + 3
                    case "<":
                        score = (score * 5) + 4
            scores.append(score) 
    #print(input)
    scores.sort()
    middleIndex = (len(scores) - 1)/2
    print ("Part 2: {}".format(scores[int(middleIndex)]))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=10)

    example = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())
