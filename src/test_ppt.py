import unittest

# A simple calculator class to be tested
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

# Test class
class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Set up resources before each test
        print("Setting up resources before test...")  # Print setup message
        self.calculator = Calculator()

    def tearDown(self):
        # Clean up after each test
        print("Cleaning up resources after test...")  # Print teardown message
        self.calculator = None

    # Test case 1: Test addition
    def test_addition(self):
        result = self.calculator.add(5, 3)
        print(f"Test result - Addition: {result}")  # Print test result
        self.assertEqual(result, 8)

    # Test case 2: Test subtraction
    def test_subtraction(self):
        result = self.calculator.subtract(10, 2)
        print(f"Test result - Subtraction: {result}")  # Print test result
        self.assertEqual(result, 8)

    # Test case 3: Test multiplication
    def test_multiplication(self):
        result = self.calculator.multiply(4, 3)
        print(f"Test result - Multiplication: {result}")  # Print test result
        self.assertEqual(result, 12)

    # Test case 4: Test division
    def test_division(self):
        result = self.calculator.divide(15, 5)
        print(f"Test result - Division: {result}")  # Print test result
        self.assertEqual(result, 3)




if __name__ == '__main__':
    unittest.main()



    
# To run individual test cases, use the following format:
#unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromName("TestMathOperations.test_subtraction"))
    
# To run all test cases in the test class, use the following:
#unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMathOperations))
    
#To run a specific test case within the test class, use the following:
# suite = unittest.TestSuite()
# suite.addTest(TestMathOperations('test_subtraction'))
# unittest.TextTestRunner().run(suite)
