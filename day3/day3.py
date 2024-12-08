import re

def process_memory_from_file(file_path):
    # Initialize variables
    total_sum = 0
    enabled = True

    # Define regex patterns
    mul_pattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"do\(\)|don't\(\)"

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Process the line
                memory = line.strip()
                print(f"Processing line: {memory}")

                # Split the input into chunks based on mul and control patterns
                parts = re.split(f"({mul_pattern}|{control_pattern})", memory)

                # Process each part
                for part in parts:
                    if not part:  # Skip empty parts
                        continue

                    # Check for control instructions
                    if part == "do()":
                        enabled = True
                        print("do() encountered: Enabled processing.")
                    elif part == "don't()":
                        enabled = False
                        print("don't() encountered: Disabled processing.")

                    # Check for mul instructions
                    mul_match = re.match(mul_pattern, part)
                    if mul_match:
                        x, y = map(int, mul_match.groups())
                        if enabled:
                            result = x * y
                            total_sum += result
                            print(f"mul({x},{y}) processed: Result = {result} (Sum = {total_sum})")
                        else:
                            print(f"mul({x},{y}) skipped: Disabled.")

        return total_sum

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# Main execution
if __name__ == '__main__':
    file_path = 'input_file.txt'  # Replace with your file path
    result = process_memory_from_file(file_path)

    if result is not None:
        print(f"\nFinal Sum: {result}")
