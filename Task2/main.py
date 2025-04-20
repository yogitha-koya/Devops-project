def read_numbers(filename):
    with open(filename, 'r') as f:
        # This will skip empty lines and convert valid lines to floats
        return [float(line.strip()) for line in f.readlines() if line.strip()]

def main():
    # Replace 'Task2/Data.txt' with the correct path to your file
    numbers = read_numbers('Task2/Data.txt')
    print("Read numbers:", numbers)

if __name__ == "__main__":
    main()
