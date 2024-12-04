# Read data
with open('advent_of_code/day2/puzzle_input.txt', 'r') as file:
    lines = file.readlines()

reports = [[int(a) for a in line.split()] for line in lines]

safe_reports_count = 0

for report in reports:
    # First, check if the report is already safe
    is_increasing = is_decreasing = True
    for level in range(len(report) - 1):
        next_level = report[level+1]
        if not ((next_level > report[level]) and (0 < abs(next_level - report[level]) < 4)):
            is_increasing = False
        if not ((next_level < report[level]) and (0 < abs(next_level - report[level]) < 4)):
            is_decreasing = False
    
    if is_increasing or is_decreasing:
        safe_reports_count += 1
        continue

    # If not safe, try removing each level
    for remove_index in range(len(report)):
        # Create a new report without the current level
        modified_report = report[:remove_index] + report[remove_index+1:]
        
        # Check if modified report is increasing
        is_increasing = True
        for level in range(len(modified_report) - 1):
            if not ((modified_report[level+1] > modified_report[level]) and 
                    (0 < abs(modified_report[level+1] - modified_report[level]) < 4)):
                is_increasing = False
                break
        
        # Check if modified report is decreasing
        is_decreasing = True
        for level in range(len(modified_report) - 1):
            if not ((modified_report[level+1] < modified_report[level]) and 
                    (0 < abs(modified_report[level+1] - modified_report[level]) < 4)):
                is_decreasing = False
                break
        
        # If either increasing or decreasing, count as safe and move to next report
        if is_increasing or is_decreasing:
            safe_reports_count += 1
            break

print(safe_reports_count)