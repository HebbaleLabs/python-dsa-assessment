import unittest
import timeit
from collections import Counter
from main import new_random


class PerformanceTest(unittest.TestCase):
    def testPerformance(self):
        time1 = timeit.timeit("gen_random()", setup="from main import gen_random", number=5)
        time2 = timeit.timeit("new_random()", setup="from main import new_random", number=5)
        self.assertGreater(time1, time2)
        self.assertGreater(time1, 2 * time2)

    def testCount(self):
        ret = new_random()
        self.assertGreaterEqual(len(ret), 0.9 * len(ret))

    def testUnique(self):
        ret = new_random()
        uniq_ret = Counter(ret).keys()
        self.assertEqual(len(uniq_ret), len(ret))


if __name__ == '__main__':
    unittest.main()
