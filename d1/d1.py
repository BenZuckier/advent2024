#%%
from typing import List
import operator
import collections

def parse(filename: str) -> List[List]:
    """returns list of list of the l,r pairs"""
    with open(filename, "r", encoding="utf8") as f:
        lines = [list(map(int, l.split())) for l in f.readlines()]
    return lines

def get_sorted(lines: List[List]) -> List[List]:
    return [sorted(x) for x in zip(*lines)]

def part1(sorted_lines: List[List]) -> int:
    """assumes lines is already sorted"""
    return sum(map(lambda tup: operator.abs(tup[0]-tup[1]), zip(*sorted_lines)))

def part2(lines: List[List]) -> int:
    right = collections.Counter(lines[1])
    return sum(right[x] * x for x in lines[0])

if __name__ == "__main__":
    lines = parse("d1_input.txt")
    sorteds = get_sorted(lines)

    ans1 = part1(sorteds)
    print(f"part1 = {ans1}")

    ans2 = part2(sorteds)
    print(f"part2 = {ans2}")