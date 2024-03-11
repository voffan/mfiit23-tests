import unittest
import factor
from ddt import ddt, data, unpack
from deepdiff import DeepDiff

@ddt
class TestF(unittest.TestCase):

    @data([12, {2:2, 3:2}], [2, {2:1}])
    @unpack
    def test_f1(self, value, exp_result):
        result = factor.factor(value)
        self.assertEqual(isinstance(result, dict), True, "Result is not Dict!")
        self.assertEqual(DeepDiff(exp_result, result), {}, "Expected:" + str(exp_result) + " got " + str(result))

    @data([-5, Exception], [1, Exception], 
         [0, Exception], [12.5, TypeError])
    @unpack
    def test_f5(self, value, exc):
        with self.assertRaises(exc):
            factor.factor(value)
