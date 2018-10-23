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


def resolve_problem_brute_force():
    '''
    Start the interactions
    The matrix is processed as array, for example:

    276951438
    =
    2 7 6
    9 5 1
    4 3 8
    '''
    perc_completed = 0
    # 123456789
    for x in range(276543801, 987654321):
        array = return_array_if_valid(x)
        if(array):
            if assert_result_array(array):
                print_result(array)
            else:
                perc_current = int(x * 100 / 987654321)
                if perc_completed != perc_current:
                    print(str(perc_current) + "% (" + str(x) + ")")
                perc_completed = perc_current


def return_array_if_valid(number):

    strnu = str(number)
    vl = {}
    for x in range(0, 9):
        ch = strnu[x]
        vl[ch] = ch

    if len(vl) == 9:
        return list(vl.values())
    else:
        return None


def assert_result_array(array):

    # Horizontal
    if not assert_array_pos(array, 0, 1, 2):
        return False

    if not assert_array_pos(array, 3, 4, 5):
        return False

    if not assert_array_pos(array, 6, 7, 8):
        return False

    # Vertical
    if not assert_array_pos(array, 0, 3, 6):
        return False

    if not assert_array_pos(array, 1, 4, 7):
        return False

    if not assert_array_pos(array, 2, 5, 8):
        return False

    # Diagonal
    if not assert_array_pos(array, 0, 4, 8):
        return False

    if not assert_array_pos(array, 2, 4, 6):
        return False

    return True


def assert_three(vl1, vl2, vl3):
    '''
    Sum of the values must be 15
    '''
    return vl1 + vl2 + vl3 == 15


def assert_array_pos(array, p1, p2, p3):
    return assert_three(int(array[p1]), int(array[p2]), int(array[p3]))


def print_result(array):
    print('Result Found:')
    print('{} {} {}'.format(array[0], array[1], array[2]))
    print('{} {} {}'.format(array[3], array[4], array[5]))
    print('{} {} {}'.format(array[6], array[7], array[8]))


if __name__ == '__main__':
    resolve_problem_brute_force()
