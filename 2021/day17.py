from aocd.models import Puzzle
import re
from dataclasses import dataclass
from math import sqrt


@dataclass
class Velocity:
    forward: int
    vertical: int


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Target:
    min_x: int
    max_x: int
    min_y: int
    max_y: int

    def hit(self, p: Position) -> bool:
        """Check if coordinate is within the target area"""
        if self.min_x <= p.x <= self.max_x and self.min_y <= p.y <= self.max_y:
            return True
        return False


def process_input(input_str: str) -> Target:
    """Extract numbers from input string"""
    return Target(*[int(i) for i in re.findall(r"-?\d+", input_str)])


def calc_v0_max(target: Target) -> Velocity:
    """Calculate the maximum velocity to reach target"""
    return Velocity(target.max_x, abs(target.min_y + 1))


def calc_v0_min(target: Target) -> Velocity:
    """Calculate the minimum velocity to reach target"""
    return Velocity(int(sqrt(target.min_x * 2)), target.min_y)


def reaches_target(v: Velocity, target: Target) -> bool:
    p = Position(0, 0)
    while True:
        p.x += v.forward
        p.y += v.vertical
        v.forward -= 1 if v.forward else 0
        v.vertical -= 1
        if p.x > target.max_x or p.y < target.min_y:
            return False
        if target.hit(p):
            return True


def calc_highest_vertical_position(v: Velocity) -> int:
    return v.vertical * (v.vertical + 1) // 2

def part1(input):
    #xrange = input[input.find("x=")+2:input.find(",")].split('..')
    #yrange = input[input.find("y=")+2:len(input)].split('..')

    #  9  8  7  6, 5  4  3  2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    #0,9,17,24,30,35,39,42,44,45,45,44,42,39,35,30,24,17, 9, 0,-10

    target = process_input(input)
    v0_max = calc_v0_max(target)
    maxypos = calc_highest_vertical_position(v0_max)

    print ("Part 1: {}".format(maxypos))

def part2(input):
    target = process_input(input)
    v0_min = calc_v0_min(target)
    v0_max = calc_v0_max(target)
    r2 = 0
    for v0_forward in range(v0_min.forward, v0_max.forward + 1):
        for v0_vertical in range(v0_min.vertical, v0_max.vertical + 1):
            r2 += reaches_target(Velocity(v0_forward, v0_vertical), target)

    print ("Part 2: {}".format(r2))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=17)
    #target area: x=235..259, y=-118..-62

    example = "target area: x=20..30, y=-10..-5"
    
    #part1(example)
    part1(puzzle.input_data)
    #part2(example)
    part2(puzzle.input_data)
