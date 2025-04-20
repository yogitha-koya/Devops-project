def read_numbers(file_path):
    with open(file_path, 'r') as f:
        return [float(line.strip()) for line in f.readlines()]

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    numbers = read_numbers('data.txt')
    average = calculate_average(numbers)
    print(f"Average: {average}")

