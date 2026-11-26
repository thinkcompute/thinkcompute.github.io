---
# SPDX-FileCopyrightText: 2025 Arcangelo Massari <arcangelo.massari@unibo.it>
# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: CC-BY-4.0

jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(ch-lab-05)=
# Algorithm exercises: brute-force

```{admonition} Learning objectives
:class: tip
By the end of this lab, you will be able to:
- Better understand the insertion sort algorithm
- Implement in-place sorting algorithms using swap and shift techniques
```

---

## Part 1: Brute-force exercises

In {ref}`ch-brute-force`, you learned about brute-force algorithms that solve problems by examining all possible solutions. The two main algorithms introduced were **linear search** and **insertion sort**. In this section, you will implement in-place variants of insertion sort and solve other problems with the brute-force approach.

### Reviewing insertion sort

Do you remember the insertion sort algorithm from {ref}`ch-brute-force`? Here is the implementation presented in the textbook:

```{code-cell} python
def insertion_sort(input_list):
    result = list()  # A new empty list where to store the result

    # iterate all the items on the input list
    for item in input_list:

        # initialise the position where to insert the item
        # at the end of the result list
        insert_position = len(result)

        # iterate, in reverse order, all the positions of all the
        # items already included in the result list
        for prev_position in reversed(range(insert_position)):

            # check if the current item is less than the one in
            # prev_position in the result list
            if item < result[prev_position]:
                # if it is so, then the position where to insert the
                # current item becomes prev_position
                insert_position = prev_position

        # the item is inserted into the position found
        result.insert(insert_position, item)

    return result  # the ordered list is returned

print(insertion_sort([5, 3, 8, 1]))  # [1, 3, 5, 8]
```

This implementation is intuitive and was useful for introducing several Python features: the `insert()` method, the `range()` function, and the `reversed()` function. However, it does more work than it needs to:

1. **Extra memory**: It creates a new list (`result`) to store the sorted elements, using additional memory proportional to the input size.

2. **Unnecessary comparisons**: The inner loop scans every position of `result`, even after it has found where the item belongs. On a list that is already sorted, each item is still compared with all the items before it.

3. **Hidden cost of `insert()`**: The `list.insert()` method looks simple, but internally it must shift all elements after the insertion point to make room for the new element. For example, if we insert an element at position 0 of a list with 100 elements, Python must move all 100 elements one position to the right. This happens "behind the scenes" but still takes time.

In the following exercises, you will write versions that sort the list *in place*, without creating a new list, and stop scanning as soon as the item reaches its position. You will also move the elements yourself instead of calling `insert()`. The shifting no longer happens behind the scenes, which lets you see how much it costs and find a way to keep that cost low.

---

### Exercise 1.1: In-place insertion sort with swap

Implement a function `insertion_sort_swap(items)` that sorts a list in place using element swapping.

**Requirements**:
- Do not use the `list.insert()` method
- Do not create a second list (modify the input list directly)
- Use element swapping to move elements to their correct positions

```python
numbers = [5, 3, 8, 1]
insertion_sort_swap(numbers)
print(numbers)  # Expected: [1, 3, 5, 8]

words = ["banana", "apple", "cherry"]
insertion_sort_swap(words)
print(words)  # Expected: ["apple", "banana", "cherry"]
```

````{admonition} Solution
:class: dropdown

**Solution 1: Using a separate swap function**

```python
def swap(items, first, second):
    temp = items[first]
    items[first] = items[second]
    items[second] = temp

def insertion_sort_swap(items):
    for item_position in range(1, len(items)):
        position = item_position
        # Move the item left while the one before it is greater
        while position > 0 and items[position] < items[position - 1]:
            swap(items, position, position - 1)
            position = position - 1

numbers = [5, 3, 8, 1]
insertion_sort_swap(numbers)
print(numbers)  # [1, 3, 5, 8]
```

`item_position` is where the item to insert starts, and `position` is where that item is as it moves left, one swap at a time.

**Solution 2: Using Python's tuple swap syntax**

Python allows swapping two values in a single line without a temporary variable:

```python
def insertion_sort_swap(items):
    for item_position in range(1, len(items)):
        position = item_position
        while position > 0 and items[position] < items[position - 1]:
            # Swap using tuple unpacking
            items[position], items[position - 1] = items[position - 1], items[position]
            position = position - 1

numbers = [5, 3, 8, 1]
insertion_sort_swap(numbers)
print(numbers)  # [1, 3, 5, 8]
```

**Execution trace for `insertion_sort_swap([5, 3, 8, 1])`**:

```
Initial:        [5, 3, 8, 1]

Pass 1 (item_position=1):
  position=1:   items[1]=3 < items[0]=5? Yes, swap positions 1 and 0
                [3, 5, 8, 1]
  position=0:   reached the start, stop

Pass 2 (item_position=2):
  position=2:   items[2]=8 < items[1]=5? No, stop

Pass 3 (item_position=3):
  position=3:   items[3]=1 < items[2]=8? Yes, swap positions 3 and 2
                [3, 5, 1, 8]
  position=2:   items[2]=1 < items[1]=5? Yes, swap positions 2 and 1
                [3, 1, 5, 8]
  position=1:   items[1]=1 < items[0]=3? Yes, swap positions 1 and 0
                [1, 3, 5, 8]
  position=0:   reached the start, stop

Result:         [1, 3, 5, 8]
```

Note that each swap requires 3 operations.
````

---

### Exercise 1.2: In-place insertion sort with shift

The swap-based approach works, but each swap requires 3 operations. When moving an element several positions, we can do better.

Consider moving the element `1` from position 3 to position 0 in `[3, 5, 8, 1]`:
- **With swap**: 3 swaps, each requiring 3 operations = 9 operations total
- **With shift**: Save `1` once (1 operation), shift 3 elements right (3 operations), place `1` (1 operation) = 5 operations total

Implement a function `insertion_sort_shift(items)` that uses shifting instead of swapping.

**The idea**: Instead of swapping adjacent elements repeatedly, save the current element in a variable, shift all larger elements one position to the right, then place the saved element in the correct position.

````{admonition} Solution
:class: dropdown

```python
def insertion_sort_shift(items):
    for item_position in range(1, len(items)):
        item = items[item_position]
        prev_position = item_position - 1

        # Shift the elements greater than item one position to the right
        while prev_position >= 0 and items[prev_position] > item:
            items[prev_position + 1] = items[prev_position]
            prev_position = prev_position - 1

        # Place the item in the free position
        items[prev_position + 1] = item

numbers = [5, 3, 8, 1]
insertion_sort_shift(numbers)
print(numbers)  # [1, 3, 5, 8]

words = ["banana", "apple", "cherry"]
insertion_sort_shift(words)
print(words)  # ["apple", "banana", "cherry"]
```

**Execution trace for `insertion_sort_shift([5, 3, 8, 1])`**:

```
Initial:            [5, 3, 8, 1]

Pass 1 (item_position=1):
  Save item:        item = 3
  prev_position=0:  items[0]=5 > item=3? Yes
  Shift right:      [5, 5, 8, 1]  (5 copied from position 0 to position 1)
  prev_position=-1: reached the start, stop
  Place item:       [3, 5, 8, 1]  (3 placed at position 0)

Pass 2 (item_position=2):
  Save item:        item = 8
  prev_position=1:  items[1]=5 > item=8? No, stop
  Place item:       [3, 5, 8, 1]  (8 stays at position 2, no shifts needed)

Pass 3 (item_position=3):
  Save item:        item = 1
  prev_position=2:  items[2]=8 > item=1? Yes
  Shift right:      [3, 5, 8, 8]  (8 copied from position 2 to position 3)
  prev_position=1:  items[1]=5 > item=1? Yes
  Shift right:      [3, 5, 5, 8]  (5 copied from position 1 to position 2)
  prev_position=0:  items[0]=3 > item=1? Yes
  Shift right:      [3, 3, 5, 8]  (3 copied from position 0 to position 1)
  prev_position=-1: reached the start, stop
  Place item:       [1, 3, 5, 8]  (1 placed at position 0)

Result:             [1, 3, 5, 8]
```

This is the classic insertion sort algorithm, widely used because it is simple and efficient for small lists or nearly sorted data.

**Understanding the index manipulation**

The shift approach requires careful index management. Looking at the code, you might wonder: why `prev_position = item_position - 1`? Why `prev_position + 1` for both shifting and placing the item? Let's clarify each choice.

**Why `prev_position = item_position - 1`?**

We start `prev_position` at `item_position - 1` because:
- Position `item_position` contains the element we just saved in `item`
- We need to compare against elements in the *already sorted portion* (positions 0 to `item_position - 1`)
- Scanning therefore starts from the last element of the sorted portion

**Why `items[prev_position + 1] = items[prev_position]` for shifting?**

During the while loop, `prev_position` points to the element we're currently checking. If that element is greater than `item`, we need to move it one position to the right to make room. Since `prev_position` is the current position, `prev_position + 1` is the position to the right.

**Why `prev_position = prev_position - 1` after each shift?**

After shifting an element to the right, we need to check the next element to the left. Decrementing `prev_position` moves our "cursor" one position backward through the sorted portion. We keep doing this until either:
- We find an element smaller than or equal to `item` (loop condition becomes false)
- We go past the beginning of the list (`prev_position` becomes -1, and `prev_position >= 0` becomes false)

**Why `items[prev_position + 1] = item` for insertion?**

When the while loop ends, `prev_position` has one of two values:
- **Case A**: `prev_position` points to an element that is ≤ `item` (the loop stopped because `items[prev_position] > item` became false). Since that element is smaller or equal, `item` must go in the position immediately after it.
- **Case B**: `prev_position = -1` because we decremented past the start of the list (all elements were greater than `item`). `item` is the smallest, and it belongs at position 0. And indeed, `-1 + 1 = 0 = prev_position + 1`.

In both cases, `prev_position + 1` gives the correct insertion position.
````

---

### Exercise 1.3: Sort by string length

Modify the insertion sort algorithm to sort strings by their **length** (shortest first) instead of alphabetically.

Implement `sort_by_length(strings)`.

```python
print(sort_by_length(["cat", "elephant", "dog", "a"]))  # Expected: ["a", "cat", "dog", "elephant"]
print(sort_by_length(["ab", "abc", "a"]))              # Expected: ["a", "ab", "abc"]
print(sort_by_length(["same", "size", "word"]))        # Expected: ["same", "size", "word"] (same length, original order)
```

````{admonition} Solution
:class: dropdown

```python
def sort_by_length(strings):
    for item_position in range(1, len(strings)):
        item = strings[item_position]
        prev_position = item_position - 1

        # Shift the strings longer than item one position to the right
        while prev_position >= 0 and len(strings[prev_position]) > len(item):
            strings[prev_position + 1] = strings[prev_position]
            prev_position = prev_position - 1

        strings[prev_position + 1] = item
    return strings

print(sort_by_length(["cat", "elephant", "dog", "a"]))  # ["a", "cat", "dog", "elephant"]
print(sort_by_length(["ab", "abc", "a"]))              # ["a", "ab", "abc"]
print(sort_by_length(["same", "size", "word"]))        # ["same", "size", "word"]
```

**Execution trace for `sort_by_length(["cat", "a", "elephant"])`**:

```
Initial:            ["cat", "a", "elephant"]

Pass 1 (item_position=1):
  Save item:        item = "a" (len=1)
  prev_position=0:  len(strings[0])=3 > len(item)=1? Yes
  Shift right:      ["cat", "cat", "elephant"]
  prev_position=-1: reached the start, stop
  Place item:       ["a", "cat", "elephant"]

Pass 2 (item_position=2):
  Save item:        item = "elephant" (len=8)
  prev_position=1:  len(strings[1])=3 > len(item)=8? No, stop
  Place item:       ["a", "cat", "elephant"]  (no shifts needed)

Result:             ["a", "cat", "elephant"]
```
````

---

### Exercise 1.4: Find second largest

Implement a function `find_second_largest(numbers)` that returns the second largest value in a list with at least two distinct elements.

```python
print(find_second_largest([3, 1, 4, 1, 5, 9, 2, 6]))  # Expected: 6
print(find_second_largest([10, 20]))                   # Expected: 10
print(find_second_largest([5, 5, 5, 3, 3]))           # Expected: 3
```

```{admonition} Hint
:class: tip dropdown
Keep track of both the largest and second largest values as you iterate through the list. Update them appropriately when you find a new largest value.
```

````{admonition} Solution
:class: dropdown

```python
def find_second_largest(numbers):
    largest = numbers[0]
    second = None

    for item in numbers[1:]:
        if item > largest:
            second = largest
            largest = item
        elif item != largest and (second is None or item > second):
            second = item

    return second

print(find_second_largest([3, 1, 4, 1, 5, 9, 2, 6]))  # 6
print(find_second_largest([10, 20]))                   # 10
print(find_second_largest([5, 5, 5, 3, 3]))           # 3
```

`second` starts as `None` because the second largest value is unknown until the function meets a value different from `largest`.

**Execution trace for `find_second_largest([3, 7, 2, 5, 9])`**:

| Item | largest | second | Action |
|------|---------|--------|--------|
| (init) | 3 | None | First element |
| 7 | 7 | 3 | 7 > largest, update both |
| 2 | 7 | 3 | 2 < second, no change |
| 5 | 7 | 5 | 5 > second and 5 != largest, update second |
| 9 | 9 | 7 | 9 > largest, update both |

**Result**: `7`

**Execution trace for `find_second_largest([5, 5, 5, 3, 3])`** (with duplicates):

| Item | largest | second | Action |
|------|---------|--------|--------|
| (init) | 5 | None | First element |
| 5 | 5 | None | 5 == largest, no change |
| 5 | 5 | None | 5 == largest, no change |
| 3 | 5 | 3 | 3 != largest and second is None, update second |
| 3 | 5 | 3 | 3 == second, no change |

**Result**: `3`

The condition `item != largest` prevents duplicates of the largest value from becoming the second largest.
````

---

```{admonition} Next lab
:class: tip
The next lab, {ref}`ch-lab-04`, explains when to choose a list, a set or a dictionary.
```
