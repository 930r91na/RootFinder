import unittest

import bisectionMethod as bM
import newtonMethod as nM
import newtonModifiedMethod as nMM
import secantMethod as sM
import differentiate as diff


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def testBisection(self):
        self.assertAlmostEquals(bM.bisectionMeth(lambda x: x ** 2 - 4, 0, 5, 0.0001), 2, 4)

    def testNewton(self):
        f = lambda x: x ** 2 - 4
        self.assertAlmostEquals(nM.newton(f, diff.differentiate(f), 0, 0.0001, 50), 2, 4)

    def testNewtonModified(self):
        f = lambda x: x ** 2 - 4
        self.assertAlmostEquals(nMM.newtonModified(f,diff.differentiate(f),diff.differentiate(diff.differentiate(f)), 0, 0.0001, 50), 2, 4)

    def testSecant(self):
        f = lambda x: x ** 2 - 4
        self.assertAlmostEquals(sM.secantMethod(lambda x: x ** 2 - 4, 0, 2, 0.0001, 50), 2, 4)


if __name__ == '__main__':
    unittest.main()
