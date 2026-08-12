import unittest

from src.averages import mean


class MeanTests(unittest.TestCase):
    def test_returns_arithmetic_mean(self) -> None:
        self.assertEqual(mean([2, 4, 9]), 5.0)

    def test_preserves_float_precision(self) -> None:
        self.assertAlmostEqual(mean([0.1, 0.2, 0.3]), 0.2)

    def test_rejects_empty_input(self) -> None:
        with self.assertRaisesRegex(ValueError, "at least one value"):
            mean([])


if __name__ == "__main__":
    unittest.main()
