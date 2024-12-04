# PART 1
# Read the data
with open('advent_of_code/day1/data_day1.txt', 'r') as file:
    lines = file.readlines()

# Parse the data into two separate lists
left_list = []
right_list = []

for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

# Sort both lists
left_list.sort()
right_list.sort()

# Calculate the total distance
total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))

print(f'The total distance is: {total_distance}')


# PART 2

amount_of_apperances = {}

# Count the amount of times each number appears in the right list
for i in range(len(right_list)):
    if right_list[i] in amount_of_apperances:
        amount_of_apperances[right_list[i]] += 1
    else:
        amount_of_apperances[right_list[i]] = 1

# Multiply each number in the left list by the amount it appears in the right list
similarity_distance = sum(left * amount_of_apperances.get(left, 0) for left in left_list)

print(f'The similarity distance is: {similarity_distance}')