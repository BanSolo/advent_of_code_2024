import re

with open('source/day_3.txt') as f:
    sequences = f.readlines()

# Task 1
def mul(a, b):
    return a * b

final_sum = 0
for sequence in sequences:
    valid_operations = re.findall('mul\(\d+,\d+\)', sequence)
    for operation in valid_operations:
        final_sum += eval(operation)

print(final_sum)


# Task 2
current_state = True
final_sum = 0
pattern = r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))"

for sequence in sequences:
    matches = re.finditer(pattern, sequence)
    for match in matches:
        instruction = match.group()

        if instruction == "do()":
            current_state = True
        elif instruction == "don't()":
            current_state = False
        elif instruction.startswith("mul") and current_state:
            numbers = re.findall(r'\d+', instruction)
            if numbers:
                operand1, operand2 = map(int, numbers)
                final_sum += operand1 * operand2

print(final_sum)