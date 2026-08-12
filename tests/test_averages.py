import unittest

from src.averages import mean, median


class MeanTests(unittest.TestCase):
    def test_returns_arithmetic_mean(self) -> None:
        self.assertEqual(mean([2, 4, 9]), 5.0)

    def test_preserves_float_precision(self) -> None:
        self.assertAlmostEqual(mean([0.1, 0.2, 0.3]), 0.2)

    def test_rejects_empty_input(self) -> None:
        with self.assertRaisesRegex(ValueError, "at least one value"):
            mean([])


class MedianTests(unittest.TestCase):
    def test_returns_middle_value_for_odd_input(self) -> None:
        self.assertEqual(median([9, 1, 5]), 5.0)

    def test_averages_middle_values_for_even_input(self) -> None:
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_does_not_mutate_input(self) -> None:
        values = [3, 1, 2]
        median(values)
        self.assertEqual(values, [3, 1, 2])

    def test_rejects_empty_input(self) -> None:
        with self.assertRaisesRegex(ValueError, "at least one value"):
            median([])


if __name__ == "__main__":
    unittest.main()
