# -*- coding: utf-8 -*-
# Copyright (c) 2022, Silvio Peroni <essepuntato@gmail.com>
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
def test_euclidean(r, s, expected):
    result = euclidean(r, s)
    
    if result == expected:
        return True
    else:
        return False


# Code of the function
def euclidean(r, s):
    if r == s:
        return r
    elif r < s:
        return euclidean(r, s - r)
    else:
        return euclidean(r - s, s)

        
        
# Tests
print(test_euclidean(1, 1, 1))
print(test_euclidean(1, 2, 1))
print(test_euclidean(1, 3, 1))
print(test_euclidean(3, 2, 1))
print(test_euclidean(3, 3, 3))
print(test_euclidean(3, 9, 3))
print(test_euclidean(15, 6, 3))