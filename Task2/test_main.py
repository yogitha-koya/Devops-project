#test_main.py

# Import the function to test
from main import calculate_average

# Test case to check the average of a list of numbers
def test_calculate_average():
    # Test data
    numbers = [10.0, 20.0, 30.0, 40.0, 50.0]
    
    # Expected result
    expected = 30.0
    
    # Assert that the function returns the correct average
    assert calculate_average(numbers) == expected
