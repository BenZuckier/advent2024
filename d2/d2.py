#%%
from typing import List
import functools
import operator
import itertools

def parse(filename: str) -> List[List]:
    with open(filename, "r", encoding="utf8") as f:
        lines = [list(map(int, x.split())) for x in f.readlines()]
    return lines

take_diff = lambda x: functools.reduce(operator.sub, x)

is_kosher = lambda row: all((x > 0 and x <= 3 for x in row)) or all((x < 0 and x >= -3 for x in row))

def row_test(row: list, strict=True) -> bool:
    rows = [row] if strict else [row[:i] + row[i+1:] for i, _ in enumerate(row)] + [row] # generate row options

    pairwises = [list(itertools.pairwise(x)) for x in rows]
    diffs =  [list(map(take_diff, list(row))) for row in pairwises]

    return any(is_kosher(x) for x in diffs)

loose_row_test = functools.partial(row_test, strict=False) 


if __name__ == "__main__":
    lines = parse("d2_input.txt")

    ans1 = sum(map(row_test, lines))
    ans2 = sum(map(loose_row_test, lines))

    print(f"{ans1=}")
    print(f"{ans2=}")
# %%
