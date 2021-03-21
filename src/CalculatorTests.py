import unittest
from Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(calculator.subtract(2, 2), 0)
        self.assertEqual(calculator.result, 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(calculator.multiply(3, 2), 6)
        self.assertEqual(calculator.result, 6)

    def test_divide_method_calculator(self):
        self.assertEqual(calculator.divide(6, 2), 3)
        self.assertEqual(calculator.result, 3)

if __name__ == '__main__':
    unittest.main()