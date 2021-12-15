from aocd.models import Puzzle
import networkx as nx
import numpy as np

def get_neighbors(x: int, y: int, m: int, n: int) -> list[tuple[int, int]]:
    potential = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(x, y) for x, y in potential if 0 <= x <= m and 0 <= y <= n]


def create_graph(grid: np.ndarray, m: int, n: int) -> nx.Graph:
    g = nx.grid_2d_graph(m, n, create_using=nx.DiGraph)
    for x in range(m):
        for y in range(n):
            for neighbour in get_neighbors(x, y, m, n):
                g.add_edge(neighbour, (x, y), weight=grid[x][y])
    return g


def create_big_grid(small_grid: np.ndarray, size: int = 5) -> np.ndarray:
    return np.block(
        [[(small_grid + i + j - 1) % 9 + 1 for j in range(size)] for i in range(size)]
    )

def pathgrid(grid):
    m, n = grid.shape
    g = create_graph(grid, m, n)
    return  nx.shortest_path_length(g, (0, 0), target=(m - 1, n - 1), weight="weight")

def part1(input):
    grid = np.array([[int(x) for x in list(row)] for row in input]) 
    print ("Part 1: {}".format(pathgrid(grid)))

def part2(input):
    grid = np.array([[int(x) for x in list(row)] for row in input])
    big_grid = create_big_grid(grid)
    print ("Part 2: {}".format(pathgrid(big_grid)))

if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=15)

    example = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())
