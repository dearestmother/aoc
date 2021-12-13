from aocd.models import Puzzle
from dataclasses import dataclass
from typing import List


@dataclass
class Dot:
    x: int
    y: int


class Grid:
    def __init__(self, lines):
        poss, folds = lines[:lines.index('')], lines[lines.index('') + 1:]
        self.dots = []  # type: List[Dot]
        self.folds = []  # type: List[dict]

        for pos in poss:
            self.dots.append(Dot(*[int(x) for x in pos.split(',')]))

        for fold in folds:
            axis, coord = fold.split(" ")[-1].split("=")
            self.folds.append({'axis': axis, 'coord': int(coord)})

    def get_display(self) -> str:
        maxx = max([d.x for d in self.dots])
        maxy = max([d.y for d in self.dots])

        code = ""
        for y in range(maxy+1):
            for x in range(maxx+1):
                has_dot = False
                for dot in self.dots:
                    if x == dot.x and y == dot.y:
                        has_dot = True
                        break
                code += "#" if has_dot else "."
            code += "\n"

        return code

    def fold(self, times: int, get_display=False):
        if times == -1:
            times = len(self.folds)

        for i in range(times):
            fold = self.folds.pop(0)
            coord = fold['coord']
            axis = fold['axis']

            for dot in self.dots:
                if axis == 'y' and dot.y > coord:
                    dot.y = coord - (dot.y - coord)
                if axis == 'x' and dot.x > coord:
                    dot.x = coord - (dot.x - coord)

            unique = []
            for dot in self.dots:
                is_unique = True
                for u in unique:
                    if u.x == dot.x and u.y == dot.y:
                        is_unique = False
                        break
                if is_unique:
                    unique.append(dot)

            self.dots = unique

        if get_display:
            return self.get_display()

        return len(self.dots)


def run():
    test_data = """  6,10
                0,14
                9,10
                0,3
                10,4
                4,11
                6,0
                6,12
                4,1
                0,13
                10,12
                3,4
                3,0
                8,4
                1,10
                2,14
                8,10
                9,0
                
                fold along y=7
                fold along x=5  """

    data = [x.strip() for x in test_data.split('\n')]

    # input data
    puzzle = Puzzle(year=2021, day=13)
    data = [d.strip() for d in puzzle.input_data.splitlines()]

    grid = Grid(data)
    print(f'Part 1 = {grid.fold(1)} \n')
    print(f'Part 2 = \n\n{grid.fold(-1, get_display=True)}')


if __name__ == '__main__':
    run()