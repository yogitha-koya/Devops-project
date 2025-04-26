# Task2/main.py
#main.py

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Example of how the function could be used (if you want to include a sample usage)
if __name__ == "__main__":
    numbers = [10.0, 20.0, 30.0, 40.0, 50.0]
    print(f"Average of numbers: {calculate_average(numbers)}")
