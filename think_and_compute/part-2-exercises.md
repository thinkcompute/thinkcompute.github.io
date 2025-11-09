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

## References

```{bibliography}
:filter: docname in docnames
```