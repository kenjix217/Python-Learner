"""
Lesson 20: Testing and Code Quality
Golden Source Solution: Unit Testing

This script demonstrates unit testing with the `unittest` framework:
1. Testing simple functions
2. Testing classes
3. Setup and teardown
4. Testing exceptions
""",

# The code to be tested
class ShapeCalculator:
    def rectangle_area(self, length, width):
        if length < 0 or width < 0:
            raise ValueError("Dimensions must be positive")
        return length * width
    
    def circle_area(self, radius):
        import math
        if radius < 0:
            raise ValueError("Radius must be positive")
        return math.pi * (radius ** 2)
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# The Tests
import unittest
import math

class TestShapeCalculator(unittest.TestCase):
    
    def setUp(self):
        """Runs before every test method"""
        self.calc = ShapeCalculator()
        print(f"Setting up test: {self._testMethodName}")

    def tearDown(self):
        """Runs after every test method"""
        print(f"Tearing down test: {self._testMethodName}\n")

    # 1. Test rectangle area
    def test_rectangle_area_normal(self):
        """Test standard rectangle calculation"""
        self.assertEqual(self.calc.rectangle_area(10, 5), 50)
    
    def test_rectangle_area_zero(self):
        """Test with zero dimension"""
        self.assertEqual(self.calc.rectangle_area(10, 0), 0)

    def test_rectangle_area_negative(self):
        """Test that negative inputs raise ValueError"""
        with self.assertRaises(ValueError):
            self.calc.rectangle_area(-5, 10)

    # 2. Test circle area
    def test_circle_area(self):
        """Test circle area calculation"""
        expected = math.pi * 100
        self.assertAlmostEqual(self.calc.circle_area(10), expected, places=5)

    # 3. Test division (General logic)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
