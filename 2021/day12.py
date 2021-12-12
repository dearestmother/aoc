from aocd.models import Puzzle
from queue import Queue

def build_graph(edges):
    graph = {}
    for cave1, cave2 in edges:
        if cave1 not in graph:
            graph[cave1] = set()
        if cave2 not in graph:
            graph[cave2] = set()
        graph[cave1].add(cave2)
        graph[cave2].add(cave1)
    return graph

def count_paths(graph, double_pass_used, node='start', seen=['start']):
    if node == 'end':
        return 1
    count = 0
    for neighbour in graph[node]:
        if neighbour != 'start':
            if neighbour[0].isupper() or neighbour not in seen:
                count += count_paths(graph, double_pass_used, neighbour, seen + [neighbour])
            elif not double_pass_used:
                count += count_paths(graph, True, neighbour, seen)
    return count

def part1(input):
    edges = list(map(lambda x: x.split('-'), input))

    graph = build_graph(edges)
    answer = count_paths(graph, True)
    print ("Part 1: {}".format(answer))

def part2(input):
    edges = list(map(lambda x: x.split('-'), input))

    graph = build_graph(edges)
    answer = count_paths(graph, False)
    print ("Part 2: {}".format(answer))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=12)

    example = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

    example2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

    example3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""
    #part1(example.splitlines())
    #part1(example2.splitlines())
    #part1(example3.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    #part2(example2.splitlines())
    #part2(example3.splitlines())
    part2(puzzle.input_data.splitlines())
