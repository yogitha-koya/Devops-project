def read_numbers(file_path):
    """Reads numbers from a file and returns them as a list."""
    numbers = []
    with open(file_path, 'r') as f:
        for line in f:
            numbers.append(int(line.strip()))
    return numbers

def process_numbers(numbers):
    """Processes the list of numbers (e.g., summing them)."""
    return sum(numbers)

if __name__ == "__main__":
    # Example usage (you can replace 'Data.txt' with your actual file)
    numbers = read_numbers('Data.txt')
    result = process_numbers(numbers)
    print(f"The sum of the numbers is: {result}")
