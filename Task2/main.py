def read_numbers(file_path):
    """Reads numbers from a file and returns them as a list."""
    with open(file_path, 'r') as f:
        return [float(line.strip()) for line in f.readlines()]

def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    numbers = read_numbers('Task2/Data.txt')
    average = calculate_average(numbers)
    print(f"Average: {average}")
