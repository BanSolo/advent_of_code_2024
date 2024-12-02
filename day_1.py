
left_list = []
right_list = []
with open('source\day_1.txt', encoding='utf-8') as f:
    for line in f:
        elements = line.strip().split()
        left_list.append(int(elements[0]))
        right_list.append(int(elements[1]))

# Task 1
distance = 0
left_list = sorted(left_list)
right_list = sorted(right_list)
for left_location, right_location in zip(left_list, right_list):
    distance += abs(left_location - right_location)

print(distance)


# Task 2
similarity_score = 0
for left_location in left_list:
    appearance = 0
    for right_location in right_list:
        if right_location > left_location:
            break
        elif left_location == right_location:
            appearance += 1
    similarity_score += left_location * appearance

print(similarity_score)

