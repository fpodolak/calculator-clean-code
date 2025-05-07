import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.evaluate_math_expression("2+3"), 5.0)

    def test_subtraction(self):
        self.assertEqual(self.calc.evaluate_math_expression("5-2"), 3.0)

    def test_multiplication(self):
        self.assertEqual(self.calc.evaluate_math_expression("4*2"), 8.0)

    def test_mixed_operations(self):
        self.assertEqual(self.calc.evaluate_math_expression("2+3*3"), 11.0)

    def test_floats(self):
        self.assertEqual(self.calc.evaluate_math_expression("2.5+2.5"), 5.0)

    def test_negative_number(self):
        self.assertEqual(self.calc.evaluate_math_expression("-1"), -1.0)
        self.assertEqual(self.calc.evaluate_math_expression("-1+2"), 1.0)

    def test_parentheses(self):
        self.assertEqual(self.calc.evaluate_math_expression("(2+3)*3"), 15.0)
        self.assertEqual(self.calc.evaluate_math_expression("((2+3))"), 5.0)
        self.assertEqual(self.calc.evaluate_math_expression("-(2+3)*2"), -10.0)

    def test_nested_parentheses(self):
        self.assertEqual(self.calc.evaluate_math_expression("((1+2)*(3+(4*5)))"), 69.0)

    def test_complex_expression(self):
        self.assertEqual(self.calc.evaluate_math_expression("2 + (3 * (2 + 1)) - 4"), 7.0)

if __name__ == "__main__":
    unittest.main()
