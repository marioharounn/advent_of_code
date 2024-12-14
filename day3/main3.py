import re

with open("advent_of_code/day3/mul_data.txt", "r") as file:
    lines = file.readlines()

# PART 1
memory = str(lines)

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, memory)

sum_mul = (sum(int(m[0]) * int(m[1]) for m in matches))

print("The results of the multiplications:", sum_mul)

# PART 2

ex = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

pattern_do = r"do\(\)"
pattern_dont = r"don't\(\)"

def parse_memory(memory_string):
    mul_enabled = True
    total = 0
    i = 0