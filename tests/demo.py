# ==============================================================================
#  Copyright (c) 2021. Sergey2006 (Sergey Selivanov)
#  This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see https://www.gnu.org/licenses/.
# ==============================================================================

# ==============================================================================
#  Copyright (c) 2021. Sergey2006 (Sergey Selivanov)
#  This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see https://www.gnu.org/licenses/.
# ==============================================================================

"""
This is a demonstration of Time Profiler power with calculating primes.
"""

from YAPBWD.YAPBWD import *


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False


@memory_profiler
def prime_range(x):
    primes = []
    for i in range(x):
        result = is_prime(i)
        if result:
            pass
        else:
            primes.append(i)
    return primes


print(prime_range(2000))
