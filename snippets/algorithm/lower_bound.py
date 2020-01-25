import unittest


def lower_bound(arr, n):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < n:
            low = mid + 1
        else:
            high = mid

    return low


class LowerBoundTestCase(unittest.TestCase):
    def test_found(self):
        self.assertEqual(lower_bound([1, 3, 5, 7, 7, 8], 7), 3)

    def test_not_found(self):
        self.assertEqual(lower_bound([1, 2, 3, 5, 7, 9, 11, 15], 6), 4)

    def test_too_small_input(self):
        self.assertEqual(lower_bound([1, 2, 3, 4, 5], 0), 0)

    def test_too_big_input(self):
        self.assertEqual(lower_bound([1, 2, 3, 4, 5], 7), 5)


if __name__ == "__main__":
    unittest.main()
