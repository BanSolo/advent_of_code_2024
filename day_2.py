
reports = []
with open('source/day_2.txt') as f:
    for line in f:
        line = [int(x) for x in line.strip().split()]
        reports.append(line)

# Task 1
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
safe_counter = 0
for report in reports:
    prev_number = None
    is_correct = False
    order = None
    for number in report:
        if prev_number is None:
            prev_number = number
        else:
            if prev_number < number and order != 'decreasing':
                order = 'increasing'
            elif prev_number > number and order != 'increasing':
                order = 'decreasing'
            else:
                is_correct = False
                break

            # case of increasing
            if (prev_number < number) and (number - prev_number > 0) and (number - prev_number < 4):
                is_correct = True
            # case of decreasing
            elif (prev_number > number) and (prev_number - number > 0) and (prev_number - number < 4):
                is_correct = True
            else:
                is_correct = False
                break
        prev_number = number
    if is_correct:
        safe_counter += 1

print(safe_counter)


# Task 2
# TODO: refact it!!!
tolerated_safe_counter = 0
for report in reports:
    prev_number = None
    is_correct = False
    order = None
    tolerated = False
    for index, number in enumerate(report):
        if prev_number is None:
            prev_number = number
        else:
            if prev_number < number:
                if order != 'decreasing':
                    order = 'increasing'
                elif not tolerated:
                    tolerated = True
                    order = None
                    prev_number = report[index - 2]
                    continue
                else:
                    is_correct = False
                    break
            elif prev_number > number:
                if order != 'increasing':
                    order = 'decreasing'
                elif not tolerated:
                    tolerated = True
                    order = None
                    prev_number = report[index - 2]
                    continue
                else:
                    is_correct = False
                    break
            else:
                if not tolerated:
                    tolerated = True
                    prev_number = report[index - 1]
                    continue
                else:
                    is_correct = False
                    break

            # case of increasing
            if (prev_number < number) and (number - prev_number > 0) and (number - prev_number < 4):
                is_correct = True
            # case of decreasing
            elif (prev_number > number) and (prev_number - number > 0) and (prev_number - number < 4):
                is_correct = True
            elif not tolerated:
                tolerated = True
                continue
            else:
                is_correct = False
                break
        prev_number = number
    if is_correct:
        tolerated_safe_counter += 1

print(tolerated_safe_counter)
