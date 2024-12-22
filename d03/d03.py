#%%
import re
from operator import mul

def read(filename: str) -> str:
    with open("d3_input.txt", "r", encoding="utf8") as f:
        return f.read()
    
def get_multiply_sum(text: str) -> int:
    muls = re.findall(r"mul\(\d*,\d*\)", text)
    return sum(map(eval, muls))

def process_instructions(text: str) -> str:
    first, *rest = text.split("don't()")
    activated = [first] + ["".join(x.split("do()")[1:]) for x in rest]
    return "".join(activated)

if __name__ == "__main__":
    text = read("d3_input.txt")

    print(f"part1 = {get_multiply_sum(text)}")
    print(f"part2 = {get_multiply_sum(process_instructions(text))}")
