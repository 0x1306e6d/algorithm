import unittest


def multiply(a, b):
    result = 0

    while a > 0:
        if (a % 2) == 1:
            result += b

        a >>= 1
        b <<= 1

    return result


class MultiplyTestCase(unittest.TestCase):
    def test_1x1(self):
        self.assertEqual(multiply(1, 1), 1)

    def test_1x2(self):
        self.assertEqual(multiply(1, 2), 2)

    def test_2x2(self):
        self.assertEqual(multiply(2, 2), 4)

    def test_13x31(self):
        self.assertEqual(multiply(13, 31), 403)

    def test_16x32(self):
        self.assertEqual(multiply(16, 32), 512)

    def test_45x37(self):
        self.assertEqual(multiply(45, 37), 1665)


if __name__ == "__main__":
    unittest.main()
