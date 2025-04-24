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
    @staticmethod
    def sample_standard_deviation_stream():
        N = 0
        mean = 0.0
        M2 = 0.0

        for line in sys.stdin:
            for token in line.split():
                try:
                    x = float(token)
                except ValueError:
                    return "error"
                    #continue

                N += 1
                delta = MathLib.subtract(x, mean)
                mean = MathLib.add(mean, MathLib.divide(delta, N))
                delta2 = MathLib.subtract(x, mean)
                M2 = MathLib.add(M2, MathLib.multiply(delta, delta2))

        if N < 2:
            raise ValueError("At least two data points are required")

        variance = MathLib.divide(M2, N - 1)
        std_dev = variance ** 0.5
        return std_dev



if __name__ == "__main__":
    try:
        result = StandardDeviation.sample_standard_deviation_stream()
        print(result)
        result = input()
    except Exception as e:
        print(result)
        #result = input()
        sys.exit(1)

