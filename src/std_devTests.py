# This file is part of Calculator_app.
#
# Calculator_app is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Calculator_app is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (c) 2025 Tomáš Kudrna, xkudrnt00

import unittest
import sys
import io
from stddev import StandardDeviation


class TestStandardDeviationStream(unittest.TestCase):

    def run_stream_test(self, input_str, expected_output, places=3):
        # Redirect stdin
        original_stdin = sys.stdin
        sys.stdin = io.StringIO(input_str)

        try:
            result = StandardDeviation.sample_standard_deviation_stream()
            if isinstance(expected_output, float):
                self.assertAlmostEqual(result, expected_output, places=places)
            else:
                self.assertEqual(result, expected_output)
        finally:
            sys.stdin = original_stdin  # Restore original stdin

    def test_two_numbers(self):
        self.run_stream_test("1 2", 0.7071067811865476)

    def test_integers(self):
        self.run_stream_test("1 2 3 4 5", 1.5811388300841898)
        self.run_stream_test("5 5 5 5 5", 0)

    def test_negatives(self):
        self.run_stream_test("-1 -2 -3 -4 -5", 1.5811388300841898)

    def test_mixed_signs(self):
        self.run_stream_test("-2 0 2", 2.0)

    def test_floats(self):
        self.run_stream_test("1.5 2.5 3.5", 1.0)
        self.run_stream_test("0.1 0.2 0.3", 0.1)

    def test_large_numbers(self):
        self.run_stream_test("10000000000 10000000001 10000000002", 1.0)

    def test_invalid_and_valid_mix(self):
        self.run_stream_test("a 1 b 2 c 3", "error")

    def test_too_few_numbers(self):
        with self.assertRaises(ValueError):
            self.run_stream_test("42", None)
        with self.assertRaises(ValueError):
            self.run_stream_test("", None)


if __name__ == "__main__":
    unittest.main()
