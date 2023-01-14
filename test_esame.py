import unittest
from esame import *


class MyTestCase(unittest.TestCase):

    def test_init_float(self):
        self.assertRaises(ExamException, MovingAverage, 3.3)

    def test_init_negative_value(self):
        self.assertRaises(ExamException, MovingAverage, -1)

    def test_init_value_zero(self):
        self.assertRaises(ExamException, MovingAverage, 0)

    def test_init_string(self):
        self.assertRaises(ExamException, MovingAverage, 'hello')

    def test_init(self):
        x = MovingAverage(2)
        self.assertEqual(x.n, 2)

    def test_compute_not_list(self):
        x = MovingAverage(3)
        self.assertRaises(ExamException, x.compute, 2)

    def test_compute_list_of_string(self):
        x = MovingAverage(3)
        self.assertRaises(ExamException, x.compute, [2, 'hello', 3.3])

    def test_compute_empty_list(self):
        x = MovingAverage(3)
        self.assertRaises(ExamException, x.compute, [])

    def test_compute(self):
        x = MovingAverage(2)
        self.assertEqual(x.compute([2, 4, 8, 16]), [3.0, 6.0, 12.0])

    def test_compute_one_element_list(self):
        x = MovingAverage(6)
        self.assertRaises(ExamException, x.compute, [2, 4])

    def test_compute_one_element_list_with_unit_window(self):
        x = MovingAverage(1)
        self.assertEqual(x.compute([2]), [2])

    def test_compute_same_data(self):
        x = MovingAverage(3)
        self.assertEqual(x.compute([0, 0, 0, 0, 0, 0]), [0, 0, 0, 0])

    def test_compute_negative_data(self):
        x = MovingAverage(3)
        self.assertEqual(x.compute([-1, -2, -3, -4]), [-2, -3])


if __name__ == '__main__':
    unittest.main()
