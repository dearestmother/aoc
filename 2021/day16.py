from aocd.models import Puzzle
import math
from dataclasses import dataclass
from typing import Protocol, Sequence

class Packet(Protocol):
    """A generic packet protocol."""

    @property
    def version(self) -> int:
        """Get the packet version."""

    @property
    def type_id(self) -> int:
        """Get the packet type ID."""

    @property
    def value(self) -> int:
        """Get the packet value."""

    @property
    def version_sum(self) -> int:
        """Get the sum the packet version and all its sub-packets' versions."""


@dataclass(frozen=True)
class LiteralPacket:
    version: int
    type_id: int
    value: int

    @property
    def version_sum(self) -> int:
        return self.version


@dataclass(frozen=True)
class OperatorPacket:
    version: int
    type_id: int
    packets: Sequence[Packet]

    @property
    def value(self) -> int:
        values: list[int] = [packet.value for packet in self.packets]
        match self.type_id:
            case 0:
                return sum(values)
            case 1:
                return math.prod(values)
            case 2:
                return min(values)
            case 3:
                return max(values)
            case 5:
                v1, v2 = values
                return int(v1 > v2)
            case 6:
                v1, v2 = values
                return int(v1 < v2)
            case 7:
                v1, v2 = values
                return int(v1 == v2)
            case _:
                raise ValueError(f"Unknown packet type: {self.type_id}")

    @property
    def version_sum(self) -> int:
        return self.version + sum(packet.version_sum for packet in self.packets)


class Bits:
    def __init__(self, data: str) -> None:

        self.bits = "".join(f"{int(c, base=16):04b}" for c in data.strip())
        self.ptr = 0

    def read(self, n: int) -> int:
        ret = int(self.bits[self.ptr : self.ptr + n], base=2)
        self.ptr += n

        return ret

    def read_literal(self) -> int:
        value = 0
        flag = 1
        while flag:
            flag = self.read(1)
            value = (value << 4) | self.read(4)

        return value

    def read_operator(self) -> list[Packet]:
        length_type = self.read(1)
        if length_type == 0:
            total_length = self.read(15)
            start = self.ptr
            packets = []
            while self.ptr - start < total_length:
                packet = self.read_packet()
                packets.append(packet)
        else:
            n_packets = self.read(11)
            packets = [self.read_packet() for _ in range(n_packets)]

        return packets

    def read_packet(self) -> Packet:
        version = self.read(3)
        type_id = self.read(3)
        if type_id == 4:
            return LiteralPacket(version, type_id, self.read_literal())
        else:
            return OperatorPacket(version, type_id, self.read_operator())

    def remainder(self) -> str:
        return self.bits[self.ptr :]



def part1(input):
    bits = Bits(input)
    packet = bits.read_packet()
    if not all(c == "0" for c in bits.remainder()):
        raise RuntimeError(f"A non-zero bit stream remainder: {bits.remainder()}")

    print ("Part 1: {}".format(packet.version_sum))

def part2(input):
    bits = Bits(input)
    packet = bits.read_packet()
    if not all(c == "0" for c in bits.remainder()):
        raise RuntimeError(f"A non-zero bit stream remainder: {bits.remainder()}")

    print ("Part 2: {}".format(packet.value))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=16)

    example = "D2FE28"
    #part1(example)
    part1(puzzle.input_data)
    #part2(example)
    part2(puzzle.input_data)
