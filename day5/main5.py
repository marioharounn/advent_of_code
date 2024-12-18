import math
from collections import defaultdict

with open("advent_of_code/day5/data.txt", "r") as file:
    lines = file.readlines()


def parse_input(lines: list):
    rules = []
    pages = []

    parsing_rules = True
    for line in lines:
        line = line.strip()
        
        if not line:
            parsing_rules = False
            continue

        if parsing_rules:
            rules.append(tuple(map(int, line.split("|"))))
        else:
            pages.append(list(map(int, line.split(","))))

    return rules, pages

rules, updates = parse_input(lines)


def vlaidate_updates(rules: list, updates: list):
    valid_updates = []
    not_valid_updates = []

    for a in range(len(updates)):
        is_valid = True  # Assume the page is valid initially
        for num_in_page in updates[a]:
            nums_from_rule = []
            # Collect all rules where num_in_page is the source
            for i in range(len(rules)):
                if num_in_page == rules[i][0]:
                    nums_from_rule.append(rules[i][1])
            
            # Check if any target number is incorrectly placed before the source number
            for num_from_rule in nums_from_rule:
                if num_from_rule in updates[a][:updates[a].index(num_in_page)]:
                    not_valid_updates.append(updates[a])
                    is_valid = False  # Mark as invalid
                    break  # Stop checking further rules for this page
            if not is_valid:
                break  # Stop checking further numbers in this page
        
        if is_valid:
            valid_updates.append(updates[a])
    
    return valid_updates, not_valid_updates

valid_updates, not_valid_updates = vlaidate_updates(rules, updates)

# PART 1
sum_middle_numbers_valid = sum([update[math.floor(len(update)/2)] for update in valid_updates])
print("Middle page number from those correctly-ordered updates is:", sum_middle_numbers_valid)
print("")

# PART 2

def reorder_update(rules: list, update: list):
    # Build graph and in-degrees
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree[x] += 0  # Ensure x exists in in_degree

    # Topological Sort using a list instead of deque
    queue = [node for node in update if in_degree[node] == 0]
    sorted_order = []

    while queue:
        current = queue.pop(0)  # Pop the first element (FIFO)
        sorted_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

reordered_updates = []
for update in not_valid_updates:
    reordered = reorder_update(rules, update)
    reordered_updates.append(reordered)

sum_middle_reordered = sum([update[len(update) // 2] for update in reordered_updates])
print("Middle page number from reordered updates is:", sum_middle_reordered)
