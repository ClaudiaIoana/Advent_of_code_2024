def is_safe(report):
    """Checks if a report is safe without any modifications."""
    if sorted(report) == report or sorted(report, reverse=True) == report:
        for i in range(len(report) - 1):
            if not (1 <= abs(report[i] - report[i + 1]) <= 3):
                return False
        return True
    return False

def is_safe_with_dampener(report):
    """Checks if a report can be made safe by removing a single bad level."""
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

if __name__ == '__main__':
    # Read input data
    with open('input_file.txt', 'r') as file:
        data = [list(map(int, line.split())) for line in file]

    safe_count = 0

    for report in data:
        if is_safe(report) or is_safe_with_dampener(report):
            safe_count += 1

    print("Number of safe reports:", safe_count)
