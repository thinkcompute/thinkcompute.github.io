# -*- coding: utf-8 -*-
# Copyright (c) 2018, Silvio Peroni <essepuntato@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.


# Test case for the function
def test_quicksort(input_list, start, end, expected):
    result = quicksort(input_list, start, end)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def quicksort(input_list, start, end):
    if start < end:
        pivot_position = partition(input_list, start, end, start)
        quicksort(input_list, start, pivot_position - 1)
        quicksort(input_list, pivot_position + 1, end)
    return input_list

def partition(input_list, start, end, pivot_position):
    pivot_value = input_list[pivot_position]

    swap_index = start - 1
    for index in range(start, end + 1):
        if input_list[index] < pivot_value:
            swap_index += 1
            if swap_index == pivot_position:
                pivot_position = index
            swap(input_list, swap_index, index)

    new_pivot_position = swap_index + 1
    swap(input_list, pivot_position, new_pivot_position)

    return new_pivot_position

def swap(input_list, old_index, new_index):
    cur_value = input_list[old_index]
    input_list[old_index] = input_list[new_index]
    input_list[new_index] = cur_value
    

# Run tests
print(test_quicksort([1], 0, 0, [1]))
print(test_quicksort([1, 2, 3, 4, 5, 6, 7], 0, 6, [1, 2, 3, 4, 5, 6, 7]))
print(test_quicksort([3, 4, 1, 2, 9, 8, 2], 0, 6, [1, 2, 2, 3, 4, 8, 9]))
print(test_quicksort(["Coraline", "American Gods", "The Graveyard Book", "Good Omens", "Neverwhere"], 0, 4,
                     ["American Gods", "Coraline", "Good Omens", "Neverwhere", "The Graveyard Book"]))
