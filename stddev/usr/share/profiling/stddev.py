#!/usr/bin/env python3
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

from mathLib import MathLib
import sys

result = 0

class StandardDeviation:
    """
    Class for computing sample standard deviation from a stream of numeric input.
    """

    @staticmethod
    def sample_standard_deviation_stream():
        """
        Computes the sample standard deviation from numbers read from standard input.
        Uses Welford's algorithm for numerical stability.

        The input should consist of numeric values separated by whitespace, provided via stdin.
        Non-numeric input will return the string "error".

        Returns:
            float: The computed sample standard deviation.
            str: "error" if any input value is not a valid float.

        Raises:
            ValueError: If fewer than two valid numeric values are provided.
        """
        N = 0              # Number of valid inputs
        mean = 0.0         # Running mean
        M2 = 0.0           # Sum of squares of differences from the current mean

        for line in sys.stdin:
            for token in line.split():
                try:
                    x = float(token)
                except ValueError:
                    return "error"  # Return error on invalid input

                N += 1
                # Update mean and M2 using Welford's online algorithm
                delta = MathLib.subtract(x, mean)
                mean = MathLib.add(mean, MathLib.divide(delta, N))
                delta2 = MathLib.subtract(x, mean)
                M2 = MathLib.add(M2, MathLib.multiply(delta, delta2))

        if N < 2:
            raise ValueError("At least two data points are required")

        variance = MathLib.divide(M2, N - 1)  # Sample variance
        std_dev = MathLib.sqrt(variance)     # Sample standard deviation
        return std_dev


def main():
    """
    Main entry point for the program. Computes and prints the sample standard deviation
    of numbers read from standard input. Prints 'error' if an exception occurs.
    """
    try:
        result = StandardDeviation.sample_standard_deviation_stream()
        print(result)
    except Exception as e:
        print("error")
        sys.exit(1)


if __name__ == "__main__":
    main()