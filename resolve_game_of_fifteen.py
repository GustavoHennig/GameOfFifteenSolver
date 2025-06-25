# MIT License

# Copyright (c) 2018 Gustavo Augusto Hennig

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# The Game of Fifteen (Tic-Tac-Toe) solver


def solve_brute_force():
    """Brute force search for 3x3 magic squares.

    The matrix is represented as a single array. For instance, the number
    ``276951438`` corresponds to the matrix::

        2 7 6
        9 5 1
        4 3 8
    """

    percent_completed = 0
    # 123456789
    for x in range(276543801, 987654321):
        digits = digits_if_valid(x)
        if digits:
            if is_solution(digits):
                print_result(digits)
            else:
                percent_current = int(x * 100 / 987654321)
                if percent_completed != percent_current:
                    print(f"{percent_current}% ({x})")
                percent_completed = percent_current


def digits_if_valid(number):
    """Return a list with the digits of ``number`` if they are all unique."""

    number_str = str(number)
    digits = {}
    for x in range(0, 9):
        ch = number_str[x]
        digits[ch] = ch

    if len(digits) == 9:
        return list(digits.values())
    return None


def is_solution(array):

    # Horizontal
    if not check_positions(array, 0, 1, 2):
        return False

    if not check_positions(array, 3, 4, 5):
        return False

    if not check_positions(array, 6, 7, 8):
        return False

    # Vertical
    if not check_positions(array, 0, 3, 6):
        return False

    if not check_positions(array, 1, 4, 7):
        return False

    if not check_positions(array, 2, 5, 8):
        return False

    # Diagonal
    if not check_positions(array, 0, 4, 8):
        return False

    if not check_positions(array, 2, 4, 6):
        return False

    return True


def sum_is_fifteen(v1, v2, v3):
    """Return ``True`` if the three numbers add up to 15."""
    return v1 + v2 + v3 == 15


def check_positions(array, p1, p2, p3):
    return sum_is_fifteen(int(array[p1]), int(array[p2]), int(array[p3]))


def print_result(array):
    print('Result Found:')
    print('{} {} {}'.format(array[0], array[1], array[2]))
    print('{} {} {}'.format(array[3], array[4], array[5]))
    print('{} {} {}'.format(array[6], array[7], array[8]))


if __name__ == '__main__':
    solve_brute_force()
