(ch-part-2-exercises)=
# Part 2: Exercises

`````{exercise}
:label: part-2-ex-1

What is the boolean value of `not (not True or False and True) or False`?

````{solution} part-2-ex-1
:label: part-2-ex-1-sol
:class: dropdown

```
not (not True or False and True) or False =>
not (False    or False and True) or False =>
not (False    or False         ) or False =>
not False                        or False =>
True                             or False =>
True
```
````
`````

`````{exercise}
:label: part-2-ex-2

What is the boolean value of `"spam" not in "spa span sparql" and not ("egg" > "span")`?

````{solution} part-2-ex-2
:label: part-2-ex-2-sol
:class: dropdown

```
"spam" not in "spa span sparql" and not ("egg" > "span") =>
True                            and not ("egg" > "span") =>
True                            and not False            =>
True                            and True                 =>
True
```
````
`````

`````{exercise}
:label: part-2-ex-3

Following the [Python template](./04-programming-languages.md#tdd-python-template) in Chapter {ref}`ch-programming-languages`, write in Python the algorithm proposed originally in a [figure](./02-algorithms.md#complete-example) of Chapter {ref}`ch-algorithms` as a flowchart (which uses a different approach compared to the one discussed in Chapter {ref}`ch-programming-languages`), and accompany such code with the related test function and some executions with varying values of input.

````{solution} part-2-ex-3
:label: part-2-ex-3-sol
:class: dropdown

```python
# Test case for the algorithm
def test_contains_word(first_word, second_word, bib_entry, expected):
    result = contains_word(first_word, second_word, bib_entry)
    if expected == result:
        return True
    else:
        return False


# Code of the algorithm
def contains_word(first_word, second_word, bib_entry):  # input/output: input two words and a bibliographic entry
    result = 0  # process: initialize the result value to 0

    if first_word in bib_entry:  # decision: the first word is in the bibliographic entry
        result = result + 1  # process: sum 1 to the result value

    if second_word in bib_entry:  # decision: the second word is in the bibliographic entry
        result = result + 1  # process: sum 1 to the result value

    return result  # input/output: return the result value


# Three different test runs
print(test_contains_word("Shotton", "Open",
                         "Shotton, D. (2013). Open Citations. Nature, 502: 295–297. doi:10.1038/502295a", 2))
print(test_contains_word("Citations", "Science",
                         "Shotton, D. (2013). Open Citations. Nature, 502: 295–297. doi:10.1038/502295a", 1))
print(test_contains_word("References", "1983",
                         "Shotton, D. (2013). Open Citations. Nature, 502: 295–297. doi:10.1038/502295a", 0))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-contains_word.py>`.
````
`````

`````{exercise}
:label: part-2-ex-4

Write down a small function in Python that takes in two booleans as input and returns `True` if both are false, otherwise it returns `False`.

````{solution} part-2-ex-4
:label: part-2-ex-4-sol
:class: dropdown

```python
# Test case for the function
def test_f(b1, b2, expected):
    result = f(b1, b2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(b1, b2):
    return not (b1 or b2)


# Tests
print(test_f(True, True, False))
print(test_f(True, False, False))
print(test_f(False, True, False))
print(test_f(False, False, True))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-neg_or.py>`.
````
`````

`````{exercise}
:label: part-2-ex-5

Write down a small function in Python that takes in two boolean values and implements the *xor* operation, which returns `True` only when one of the input boolean values is `True` and the other is `False`, and returns `False` otherwise.

````{solution} part-2-ex-5
:label: part-2-ex-5-sol
:class: dropdown

```python
# Test case for the function
def test_xor(b1, b2, expected):
    result = xor(b1, b2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def xor(b1, b2):
    return (b1 and not b2) or (not b1 and b2)


# Tests
print(test_xor(True, True, False))
print(test_xor(True, False, True))
print(test_xor(False, True, True))
print(test_xor(False, False, False))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-xor.py>`.
````
`````

`````{exercise}
:label: part-2-ex-6

Write down a small function in Python that takes two positive integers as input and returns the result of the division (Python operator: `/`) of the smaller one over the greater one.

````{solution} part-2-ex-6
:label: part-2-ex-6-sol
:class: dropdown

```python
# Test case for the function
def test_f(i1, i2, expected):
    result = f(i1, i2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(i1, i2):
    if i1 < i2:
        return i1 / i2
    else:
        return i2 / i1


# Tests
print(test_f(2, 4, 0.5))
print(test_f(4, 2, 0.5))
print(test_f(4, 4, 1))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-small_div.py>`.
````
`````

`````{exercise}
:label: part-2-ex-7

Consider the following snippet of Python code:

```python
def t(x, y):
    return x + y - 2

print(t(5, t(3 + 2, 2)))
```

Which value will be printed on the screen if we execute such code?

````{solution} part-2-ex-7
:label: part-2-ex-7-sol
:class: dropdown

`8`

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-plus_minus.py>`. You can run it executing the command `python ex-und-plus_minus.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-8

Consider the following function in Python:

```python
def ni(s1, s2):
    if s1 in s2 and s2 in s1:
        return False
    else:
        return True
```

Write down the value that is returned by the function above when called as follows: 

```python
ni("27", "42")
```

````{solution} part-2-ex-8
:label: part-2-ex-8-sol
:class: dropdown

```python
True
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-strings_in.py>`. You can run it executing the command `python ex-und-strings_in.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-9

Consider the following function in Python:

```python
def xor(b1, b2):
    if b1 or b2:
        return not b1 or not b2
    else:
        return False
```

Write down the value that is returned by the function above when called as follows: 

```python
xor(True, True)
```

````{solution} part-2-ex-9
:label: part-2-ex-9-sol
:class: dropdown

```python
False
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-xor.py>`. You can run it executing the command `python ex-und-xor.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-10

Consider the following Python function:

```python
def f(x, y):
    if x <= 0 and y != 0:
        return x / y 
    else:
        return y / x
```

What is the result of the execution of the following call: 

```python
f(3, 0)
```

````{solution} part-2-ex-10
:label: part-2-ex-10-sol
:class: dropdown

```python
0
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-small_div.py>`. You can run it executing the command `python ex-und-small_div.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-11

Write a sequence of instructions in Python to create a list with the following elements ordered alphabetically: `"​Harry"`​, `"​Draco"`​, `"​Hermione"`​, `​"​Ron"`​, `"​Severus"`​.

````{solution} part-2-ex-11
:label: part-2-ex-11-sol
:class: dropdown

```python
my_list = list()
my_list.append("Draco")
my_list.append("Harry")
my_list.append("Hermione")
my_list.append("Ron")
my_list.append("Severus")
```
````

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-first-list.py>`. You can run it executing the command `python ex-first-list.py` in a shell.
`````

`````{exercise}
:label: part-2-ex-12

Consider to have a stack obtained by processing, one by one, the elements included in the list of the first exercise, i.e. `my_stack = deque(["Draco", "Harry", "Hermione", "Ron", "Severus"])`. Describe the status of my_stack after the execution of each of the following operations: `my_stack.pop()`, `my_stack.pop()`, `my_stack.append("Voldemort")`.

````{solution} part-2-ex-12
:label: part-2-ex-12-sol
:class: dropdown

The stack will contain the items `"Draco"`, `"Harry"`, `"Hermione"`, and  `"Voldemort"`: `deque(["Draco", "Harry", "Hermione", "Voldemort"])`.
````
`````

`````{exercise}
:label: part-2-ex-13

Consider to have a queue obtained by processing, one by one, the elements included in the list of the first exercise, i.e. `my_queue = deque(["Draco", "Harry", "Hermione", "Ron", "Severus"])`. Describe the status of my_queue after the execution of each of the following operations: `my_queue.popleft()`, `my_queue.append("Voldemort")`, `my_queue.popleft()`.

````{solution} part-2-ex-13
:label: part-2-ex-13-sol
:class: dropdown

The queue will contain the items `"Hermione"`, `"Ron"`, `"Severus"`, and  `"Voldemort"`: `deque(["Hermione", "Ron", "Severus", "Voldemort"])`.
````
`````

`````{exercise}
:label: part-2-ex-14

Write down a small function in Python that takes in input two strings and returns `-1` if the first string is longer than the second string, `0` if the strings have the same length, and `1` if the second string is longer than the first string.

````{solution} part-2-ex-14
:label: part-2-ex-14-sol
:class: dropdown

```python
# Test case for the function
def test_f(s1, s2, expected):
    result = f(s1, s2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s1, s2):
    if len(s1) > len(s2):
        return -1
    elif len(s1) < len(s2):
        return 1
    else:
        return 0


# Tests
print(test_f("hello", "hi", -1))
print(test_f("hi", "hello", 1))
print(test_f("hello", "earth", 0))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-greater_string.py>`. You can run it executing the command `python ex-dev-greater_string.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-15

Write down a small function in Python that takes in input two strings and returns `True` if they are identical, `False` if they are not identical but contains the same number of characters, otherwise it returns the shorter one.

````{solution} part-2-ex-15
:label: part-2-ex-15-sol
:class: dropdown

```python
# Test case for the function
def test_f(s, t, expected):
    result = f(s, t)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s, t):
    if s == t:
        return True
    elif len(s) == len(t):
        return False
    elif len(s) < len(t):
        return s
    else:
        return t


# Tests
print(test_f("ciao", "ciao", True))
print(test_f("ciao", "oaic", False))
print(test_f("ciao", "me", "me"))
print(test_f("me", "ciao", "me"))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-check_string.py>`. You can run it executing the command `python ex-dev-check_string.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-16

Write down the execution steps of `linear_search(list(["Coraline", "American Gods", "The Graveyard Book", "Good Omens", "Neverwhere"]), "The Sandman")`, as explained in a [listing](./06-brute-force.md#py-linear-search-execution) of Chapter {ref}`ch-brute-force`. 

````{solution} part-2-ex-16
:label: part-2-ex-16-sol
:class: dropdown

The instructions in the *for-each* loop used in the function will be executed five times (i.e. for all the items in `input_list`), since no item will contain `"The Sandman"` as value. Thus, *None* will be returned. 

The various iterations of the *for-each* loop will be as follows:

1. The variable `position` will be set to `0`, and the variable `item` will be set to `"Coraline"`. The condition defined in the *if* statement will be `False` since `"Coraline"` is not equal to `"The Sandman"`, which is the value to search assigned to the variable `value_to_search`. Thus, the *return* instruction under the *if* block will not be executed.
2. The variable `position` will be set to `1`, and the variable `item` will be set to `"American Gods"`. The condition defined in the *if* statement will be `False` since `"American Gods"` is not equal to `"The Sandman"`, which is the value to search assigned to the variable `value_to_search`. Thus, the *return* instruction under the *if* block will not be executed.
3. The variable `position` will be set to `2`, and the variable `item` will be set to `"The Graveyard Book"`. The condition defined in the *if* statement will be `False` since `"The Graveyard Book"` is not equal to `"The Sandman"`, which is the value to search assigned to the variable `value_to_search`. Thus, the *return* instruction under the *if* block will not be executed.
4. The variable `position` will be set to `3`, and the variable `item` will be set to `"Good Omens"`. The condition defined in the *if* statement will be `False` since `"Good Omens"` is not equal to `"The Sandman"`, which is the value to search assigned to the variable `value_to_search`. Thus, the *return* instruction under the *if* block will not be executed.
5. The variable `position` will be set to `4`, and the variable `item` will be set to `"Neverwhere"`. The condition defined in the *if* statement will be `False` since `"Neverwhere"` is not equal to `"The Sandman"`, which is the value to search assigned to the variable `value_to_search`. Thus, the *return* instruction under the *if* block will not be executed.

Since no *return* instruction will be executed, `None` will be implicitly returned by the function.
````
`````

`````{exercise}
:label: part-2-ex-17

Create a test case for the algorithm introduced in a [listing](./06-brute-force.md#py-foreach-example) of Chapter {ref}`ch-brute-force`.

````{solution} part-2-ex-17
:label: part-2-ex-17-sol
:class: dropdown

```python
from collections import deque


# Test case for the function
def test_stack_from_list(input_list, expected):
    result = stack_from_list(input_list)
    if expected == result:
        return True
    else:
        return False

# Code of the function
def stack_from_list(input_list):
    output_stack = deque()  # the stack to create

    # Iterate each element in the input list and add it to the stack
    for item in input_list:
        output_stack.append(item)

    return output_stack


# Three different test runs
print(test_stack_from_list([], deque()))
print(test_stack_from_list([1, 2, 3, 4, 5], deque([1, 2, 3, 4, 5])))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-test_stack_from_list.py>`. You can run it executing the command `python ex-test_stack_from_list.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-18

Consider the following function in Python:

```python
def ln(inp, val):
    for p, i in enumerate(inp):
        if i != val:
            return p
```

Write down the value that is returned by the function above when called as follows: `ln(["a", "b", "c"], "b")`

````{solution} part-2-ex-18
:label: part-2-ex-18-sol
:class: dropdown

```python
0
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-falsify_linear_search.py>`. You can run it executing the command `python ex-und-falsify_linear_search.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-19

Consider the following Python function:

```python
def f(n):
    result = list()
    while n > 0:
        result.append(n)
        n = n -1
    return len(result)
```

What is the result of the execution of `f(3)`?

````{solution} part-2-ex-19
:label: part-2-ex-19-sol
:class: dropdown

```python
3
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-listing_integers.py>`. You can run it executing the command `python ex-und-listing_integers.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-20

Consider the following Python function:

```python
def f(s1, s2):
    result = True
    for c in s1:
        result = result and (c in s2)
    return result
```

What is the result of the execution of `f("riddle", "dialer")`?

````{solution} part-2-ex-20
:label: part-2-ex-20-sol
:class: dropdown

```python
True
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-chars_in_strings.py>`. You can run it executing the command `python ex-und-chars_in_strings.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-21

Consider the following Python function:

```python
def f(x):
    r = 0
    x_len = len(x)
    while x_len > 0:
        r = r + x_len
        x_len = x_len - 1
    return r
```

What is the result of the execution of `f("me")`?

````{solution} part-2-ex-21
:label: part-2-ex-21-sol
:class: dropdown

```python
3
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-working_with_len.py>`. You can run it executing the command `python ex-und-working_with_len.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-22

Write down a small function in Python that takes in input a number and a list of numbers and returns `True` if the sum of all the numbers in the input list is equal to the input number, otherwise it returns `False`.

````{solution} part-2-ex-22
:label: part-2-ex-22-sol
:class: dropdown

```python
# Test case for the function
def test_f(n, n_list, expected):
    result = f(n, n_list)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(n, n_list):
    result = 0
    for i in n_list:
        result += i
    return result == n


# Tests
print(test_f(10, [1, 2, 3, 4], True))
print(test_f(10, [0, 1, 2, 3, 4], True))
print(test_f(10, [1, 2, 3], False))
print(test_f(10, [1, 2, 3, 4, 5], False))
print(test_f(10, [], False))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-sum-numbers.py>`. You can run it executing the command `python ex-dev-sum-numbers.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-23

Write down a small function in Python that takes in input a string and a boolean and return a list of the *vowel* characters (i.e. those matching with any of the following ones: `"a"`, `"e"`, `"i"`, `"o"`, `"u"`) in the input string if the input boolean is `True`, otherwise (i.e. the input boolean is `False`) it returns a list of the characters that are *not* vowels.

````{solution} part-2-ex-23
:label: part-2-ex-23-sol
:class: dropdown

```python
# Test case for the function
def test_f(s, b, expected):
    result = f(s, b)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s, b):
    result = list()

    for c in s:
        if b and c in "aeiou":
            result.append(c)
        elif not b and c not in "aeiou":
            result.append(c)

    return result


# Tests
print(test_f("john doe", True, ["o", "o", "e"]))
print(test_f("john doe", False, ["j", "h", "n", " ", "d"]))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-check_vowels.py>`. You can run it executing the command `python ex-dev-check_vowels.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-24

Write down a small function in Python that takes in three strings as input and returns a tuple of two items containing the two longest input strings.

````{solution} part-2-ex-24
:label: part-2-ex-24-sol
:class: dropdown

```python
# Test case for the function
def test_f(s1, s2, s3, expected):
    result = f(s1, s2, s3)
    if sorted(expected) == sorted(result):
        return True
    else:
        return False


# Code of the function
def f(s1, s2, s3):
    l_s1 = len(s1)
    l_s2 = len(s2)
    l_s3 = len(s3)

    if l_s1 <= l_s2 and l_s1 <= l_s3:
        return s2, s3
    elif l_s2 <= l_s1 and l_s2 <= l_s3:
        return s1, s3
    else:
        return s1, s2


# Tests
print(test_f("ciao", "hello", "hi", ("ciao", "hello")))
print(test_f("ciao", "hi", "hi", ("ciao", "hi")))
print(test_f("hi", "hi", "hi", ("hi", "hi")))
print(test_f("hi", "hi", "ciao", ("hi", "ciao")))
``` 

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-measuring_strings.py>`. You can run it executing the command `python ex-dev-measuring_strings.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-25

Write in Python the function `def my_enumerate(input_list)` which behaves like the built-in function `enumerate()` introduced in [Section "Linear search"](./06-brute-force.md#linear-search) of Chapter {ref}`ch-brute-force` and returns a proper list, and accompany the function with the related test case. It is not possible to use the built-in function `enumerate()` in the implementation.

````{solution} part-2-ex-25
:label: part-2-ex-25-sol
:class: dropdown

```python
# Test case for the function
def test_my_enumerate(input_list, expected):
    result = my_enumerate(input_list)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def my_enumerate(input_list):
    l = list()
    for i in range(len(input_list)):
        l.append((i, input_list[i]))
    return l


# Tests
print(test_my_enumerate([], []))
print(test_my_enumerate(["a", "b", "c"], [(0, "a"), (1, "b"), (2, "c")]))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-my_enumerate.py>`. You can run it executing the command `python ex-my_enumerate.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-26

Write in Python the function `def my_range(stop_number)` which behaves like the built-in function `range()` introduced in [Section "Insertion sort"](./06-brute-force.md#insertion-sort) of Chapter {ref}`ch-brute-force` and returns a proper list, and accompany the function with the related test case. It is not possible to use the built-in function `range()` in the implementation.

````{solution} part-2-ex-26
:label: part-2-ex-26-sol
:class: dropdown

```python
# Test case for the function
def test_my_range(stop_number, expected):
    result = my_range(stop_number)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def my_range(stop_number):
    l = list()
    while stop_number > 0:
        stop_number = stop_number - 1
        l.insert(0, stop_number)
    return l


# Tests
print(test_my_range(0, []))
print(test_my_range(1, [0]))
print(test_my_range(4, [0, 1, 2, 3]))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-my_range.py>`. You can run it executing the command `python ex-my_range.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-27

Write in Python the function `def my_reversed(input_list)` which behaves like the built-in function `reversed()` introduced in [Section "Insertion sort"](./06-brute-force.md#insertion-sort) of Chapter {ref}`ch-brute-force` and returns a proper list, and accompany the function with the related test case. It is not possible to use the built-in function `reversed()` in the implementation.

````{solution} part-2-ex-27
:label: part-2-ex-27-sol
:class: dropdown

```python
# Test case for the function
def test_my_reversed(input_list, expected):
    result = my_reversed(input_list)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def my_reversed(input_list):
    l = list()
    for item in input_list:
        l.insert(0, item)
    return l


# Tests
print(test_my_reversed([], []))
print(test_my_reversed([1], [1]))
print(test_my_reversed([1, 2, 4, 3, 4, 7, 2], [2, 7, 4, 3, 4, 2, 1]))
print(test_my_reversed(["a", "b", "c", "d"], ["d", "c", "b", "a"]))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-my_reversed.py>`. You can run it executing the command `python ex-my_reversed.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-28

Write a code in Python to create a set of the following elements: `"​Bilbo"`, `"​Frodo"`, `"​Sam"`, `"​Pippin"`, `"​Merry"`. 

````{solution} part-2-ex-28
:label: part-2-ex-28-sol
:class: dropdown

```python
my_set = set()
my_set.add("Bilbo")
my_set.add("Frodo")
my_set.add("Sam")
my_set.add("Pippin")
my_set.add("Merry")
```
````

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-create_set.py>`. You can run it executing the command `python ex-create_set.py` in a shell.
`````

`````{exercise}
:label: part-2-ex-29

Consider the set created in the first exercise, stored in the variable `my_set`. Describe the status of ​`my_set` after the execution of each of the following operations: 

```python
​my_set.remove("Bilbo")
my_set.add("Galadriel")
​my_set.update(set({"Saruman", "Frodo", "Gandalf"}))
```

````{solution} part-2-ex-29
:label: part-2-ex-29-sol
:class: dropdown

The set will contain the elements `"​Frodo"`, `"​Sam"`, `"​Pippin"`, `"​Merry"`, `"Galadriel"`, `"Saruman"`, `"Gandalf"`.
````
`````

`````{exercise}
:label: part-2-ex-30

Suppose to organise some of the elements in the set returned by the second exercise in two different sets: `set_hobbit` that refers to the set `set({"Frodo", "Sam", "Pippin", "Merry"})`, and `set_magician` defined as `set({"Saruman", "Gandalf"})`. Create a dictionary containing two pairs: one that associates the set of hobbits with the key `"hobbit"`, and the other that associates the set of magicians with the key `"magician"`. 

````{solution} part-2-ex-30
:label: part-2-ex-30-sol
:class: dropdown

```python
set_hobbit = set()
set_hobbit.add("Frodo")
set_hobbit.add("Sam")
set_hobbit.add("Pippin")
set_hobbit.add("Merry")

set_magician = set()
set_magician.add("Saruman")
set_magician.add("Gandalf")

my_dict = dict()
my_dict["hobbit"] = set_hobbit
my_dict["magician"] = set_magician
```
````

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-create_dict_of_sets.py>`. You can run it executing the command `python ex-create_dict_of_sets.py` in a shell.
`````

`````{exercise}
:label: part-2-ex-31

Consider the following Python function:

```python
def g(x):
    r = set()
    idx = 0
    for it in x:
        if it not in r:
            r.add(idx)
        idx = idx + 1
    return r
```

What is the result of the execution of `g([5, 7, 7, 2, 5, 7])`?

````{solution} part-2-ex-31
:label: part-2-ex-31-sol
:class: dropdown

```python
{0, 1, 2, 4, 5}
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-set_of_integers.py>`. You can run it executing the command `python ex-und-set_of_integers.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-32

Consider the following Python function:

```python
def g(s):
    result = dict()
    for c in s:
        if c not in result:
            result[c] = 0
        result[c] = result[c] + 1
    return result.get("o")
```

What is the result of the execution of `g("Bologna")`?

````{solution} part-2-ex-32
:label: part-2-ex-32-sol
:class: dropdown

```python
2
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-dict_of_integer_values.py>`. You can run it executing the command `python ex-und-dict_of_integer_values.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-33

Write down a small function in Python that takes in input two strings and returns a set of all the characters they have in common.

````{solution} part-2-ex-33
:label: part-2-ex-33-sol
:class: dropdown

```python
# Test case for the function
def test_f(s1, s2, expected):
    result = f(s1, s2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s1, s2):
    result = set()

    for c in s1:
        if c in s2:
            result.add(c)

    return result


# Tests
print(test_f("anna", "elsa", {"a"}))
print(test_f("ron", "hermione", {"r", "o", "n"}))
print(test_f("", "hello", set()))
print(test_f("dad", "mum", set()))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-set_of_matched_chars.py>`. You can run it executing the command `python ex-dev-set_of_matched_chars.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-34

Write down a small function in Python that takes in input two strings and returns the set of all the digit characters they do not have in common.

````{solution} part-2-ex-34
:label: part-2-ex-34-sol
:class: dropdown

```python
# Test case for the function
def test_f(s, n, expected):
    result = f(s, n)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s1, s2):
    result = set()
    for d in "0123456789":
        if (d in s1 and d not in s2) or (d not in s1 and d in s2):
            result.add(d)
    return result


# Tests
print(test_f("alice", "bob", set()))
print(test_f("2 books and 1 pen", "trees and 2 apples", {"1"}))
print(test_f("odd number: 1, 3, 5, 7, 9", "even number: 2, 4, 6, 8", {"1", "2", "3", "4", "5", "6", "7", "8", "9"}))
print(test_f("odd number: 1, 3, 5, 7, 9", "prime number: 1, 2, 3, 5, 7", {"2", "9"}))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-set_digits.py>`. You can run it executing the command `python ex-dev-set_digits.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-35

Write down a small function in Python that takes in input two strings and returns a set containing the characters that are not contained in both the strings.

````{solution} part-2-ex-35
:label: part-2-ex-35-sol
:class: dropdown

```python
# Test case for the function
def test_f(s1, s2, expected):
    result = f(s1, s2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s1, s2):
    result = set()

    for c in s1 + s2:
        if not (c in s1 and c in s2):
            result.add(c)

    return result


# Tests
print(test_f("", "", set()))
print(test_f("hello", "hello", set()))
print(test_f("hello", "", {"h", "e", "l", "o"}))
print(test_f("", "hello", {"h", "e", "l", "o"}))
print(test_f("hello", "hi", {"i", "e", "l", "o"}))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-chars_not_in_both_strings.py>`. You can run it executing the command `python ex-dev-chars_not_in_both_strings.py` in a shell.
````
`````

`````{exercise}
:label: part-2-ex-36

Write down a small function in Python that takes in input two strings and returns the number of characters the two strings have in common.

````{solution} part-2-ex-36
:label: part-2-ex-36-sol
:class: dropdown

```python
# Test case for the function
def test_f(s1, s2, expected):
    result = f(s1, s2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s1, s2):
    result = set()

    for c in s1:
        if c in s2:
            result.add(c)
    
    return len(result)


# Tests
print(test_f("hello", "loch", 3))
print(test_f("hello", "hi", 1))
print(test_f("hello", "hello", 4))
print(test_f("hello", "try", 0))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-chars_in_both_strings.py>`. You can run it executing the command `python ex-dev-chars_in_both_strings.py` in a shell.
````
`````

## References

```{bibliography}
:filter: docname in docnames
```