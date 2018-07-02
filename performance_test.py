import unittest
import timeit
from collections import Counter
from main import newRandom


class PerformanceTest(unittest.TestCase):
    def testPerformance(self):
        time1 = timeit.timeit("genRandom()", setup="from main import genRandom", number=5)
        time2 = timeit.timeit("newRandom()", setup="from main import newRandom", number=5)
        self.assertGreater(time1, time2)
        self.assertGreater(time1, 2 * time2)

    def testCount(self):
        ret = newRandom()
        self.assertGreaterEqual(len(ret), 0.9 * len(ret))

    def testUnique(self):
        ret = newRandom()
        uniq_ret = Counter(ret).keys()
        self.assertEqual(len(uniq_ret), len(ret))


if __name__ == '__main__':
    unittest.main()
