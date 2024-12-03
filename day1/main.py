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