---
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
- Trace and modify brute-force algorithms (linear search, insertion sort)
- Implement efficient in-place sorting algorithms using swap and shift techniques
```

---

## Part 1: Brute-force exercises

In {ref}`ch-brute-force`, you learned about brute-force algorithms that solve problems by examining all possible solutions. The two main algorithms introduced were **linear search** and **insertion sort**. In this section, you will first warm up with some linear search exercises, and then tackle the more challenging task of implementing efficient variants of insertion sort.

### Warm-up: Linear search

Before we dive into the more complex stuff, let's warm up a bit. It's 9 AM, the coffee is still kicking in, and we need to get our brains going.

### Exercise 1.1: Tracing linear search

Consider the linear search algorithm:

```{code-cell} python
def linear_search(input_list, value_to_search):
    for position, item in enumerate(input_list):
        if item == value_to_search:
            return position
    return None
```

**Question**: Trace the execution of `linear_search([15, 22, 8, 31, 17], 31)`.

For each iteration, write:
1. The current `position`
2. The current `item`
3. The result of the comparison `item == value_to_search`

````{admonition} Solution
:class: dropdown

**Execution trace**:

| Iteration | position | item | item == 31 | Action |
|-----------|----------|------|------------|--------|
| 1 | 0 | 15 | False | Continue |
| 2 | 1 | 22 | False | Continue |
| 3 | 2 | 8 | False | Continue |
| 4 | 3 | 31 | True | Return 3 |

**Result**: `3`
````

---

### Exercise 1.2: Find elements above threshold

Implement a function `find_above_threshold(values, threshold)` that returns a list of all values greater than the given threshold.

```python
print(find_above_threshold([15, 22, 8, 31, 17], 20))     # Expected: [22, 31]
print(find_above_threshold([1, 2, 3, 4, 5], 10))        # Expected: []
print(find_above_threshold([100, 50, 75, 25], 50))      # Expected: [100, 75]
```

````{admonition} Solution
:class: dropdown

```python
def find_above_threshold(values, threshold):
    result = []
    for value in values:
        if value > threshold:
            result.append(value)
    return result

print(find_above_threshold([15, 22, 8, 31, 17], 20))     # [22, 31]
print(find_above_threshold([1, 2, 3, 4, 5], 10))        # []
print(find_above_threshold([100, 50, 75, 25], 50))      # [100, 75]
```
````

---

### Reviewing insertion sort

Do you remember the insertion sort algorithm from {ref}`ch-brute-force`? Here is the implementation presented in the textbook:

```{code-cell} python
def insertion_sort(input_list):
    result = []
    for item in input_list:
        insert_position = len(result)
        for prev_position in reversed(range(insert_position)):
            if item < result[prev_position]:
                insert_position = prev_position
        result.insert(insert_position, item)
    return result

print(insertion_sort([5, 3, 8, 1]))  # [1, 3, 5, 8]
```

This implementation is intuitive and was useful for introducing several Python features: the `insert()` method, the `range()` function, and the `reversed()` function. However, it has some inefficiencies:

1. **Extra memory**: It creates a new list (`result`) to store the sorted elements, using additional memory proportional to the input size.

2. **Hidden cost of `insert()`**: The `list.insert()` method looks simple, but internally it must shift all elements after the insertion point to make room for the new element. For a list with many elements, this shifting operation can be expensive.

For example, if we insert an element at position 0 of a list with 100 elements, Python must move all 100 elements one position to the right. This happens "behind the scenes" but still takes time.

In the following exercises, you will implement more efficient versions that modify the list *in place* (without creating a new list) and avoid the hidden cost of `insert()`.

---

### Exercise 1.3: In-place insertion sort with swap

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
def swap(items, i, j):
    temp = items[i]
    items[i] = items[j]
    items[j] = temp

def insertion_sort_swap(items):
    for i in range(1, len(items)):
        j = i
        # Move the element left until it's in the correct position
        while j > 0 and items[j] < items[j - 1]:
            swap(items, j, j - 1)
            j = j - 1

numbers = [5, 3, 8, 1]
insertion_sort_swap(numbers)
print(numbers)  # [1, 3, 5, 8]
```

**Solution 2: Using Python's tuple swap syntax**

Python allows swapping two values in a single line without a temporary variable:

```python
def insertion_sort_swap(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j - 1]:
            # Swap using tuple unpacking
            items[j], items[j - 1] = items[j - 1], items[j]
            j = j - 1

numbers = [5, 3, 8, 1]
insertion_sort_swap(numbers)
print(numbers)  # [1, 3, 5, 8]
```

**Execution trace for `insertion_sort_swap([5, 3, 8, 1])`**:

```
Initial:     [5, 3, 8, 1]

Pass 1 (i=1, current_element=3):
  Compare:   [5, 3, 8, 1]   items[1]=3 < items[0]=5? Yes, swap positions 0 and 1
              ↓  ↓
  After:     [3, 5, 8, 1]   j=0, reached start, done

Pass 2 (i=2, current_element=8):
  Compare:   [3, 5, 8, 1]   items[2]=8 < items[1]=5? No, already in place

Pass 3 (i=3, current_element=1):
  Compare:   [3, 5, 8, 1]   items[3]=1 < items[2]=8? Yes, swap positions 2 and 3
                    ↓  ↓
  After:     [3, 5, 1, 8]   Continue checking

  Compare:   [3, 5, 1, 8]   items[2]=1 < items[1]=5? Yes, swap positions 1 and 2
                 ↓  ↓
  After:     [3, 1, 5, 8]   Continue checking

  Compare:   [3, 1, 5, 8]   items[1]=1 < items[0]=3? Yes, swap positions 0 and 1
              ↓  ↓
  After:     [1, 3, 5, 8]   j=0, reached start, done

Result:      [1, 3, 5, 8]
```

Note that each swap requires 3 operations.
````

---

### Exercise 1.4: In-place insertion sort with shift

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
    for i in range(1, len(items)):
        key_to_insert = items[i]
        j = i - 1

        # Shift elements that are greater than key_to_insert
        while j >= 0 and items[j] > key_to_insert:
            items[j + 1] = items[j]  # Shift element to the right
            j = j - 1

        # Place the key in its correct position
        items[j + 1] = key_to_insert

numbers = [5, 3, 8, 1]
insertion_sort_shift(numbers)
print(numbers)  # [1, 3, 5, 8]

words = ["banana", "apple", "cherry"]
insertion_sort_shift(words)
print(words)  # ["apple", "banana", "cherry"]
```

**Execution trace for `insertion_sort_shift([5, 3, 8, 1])`**:

```
Initial:        [5, 3, 8, 1]

Pass 1 (i=1):
  Save key:     key_to_insert = 3
  Current:      [5, 3, 8, 1]
                    ^
                    position to fill

  j=0: items[0]=5 > key_to_insert=3? Yes
  Shift right:  [5, 5, 8, 1]  (5 copied from position 0 to position 1)
                 ^
                 now position 0 is available

  j=-1: Stop (reached start of list)
  Insert key:   [3, 5, 8, 1]  (key_to_insert=3 placed at position 0)

Pass 2 (i=2):
  Save key:     key_to_insert = 8
  Current:      [3, 5, 8, 1]

  j=1: items[1]=5 > key_to_insert=8? No
  Insert key:   [3, 5, 8, 1]  (key stays at position 2, no shifts needed)

Pass 3 (i=3):
  Save key:     key_to_insert = 1
  Current:      [3, 5, 8, 1]
                          ^
                          position to fill

  j=2: items[2]=8 > key_to_insert=1? Yes
  Shift right:  [3, 5, 8, 8]  (8 copied from position 2 to position 3)

  j=1: items[1]=5 > key_to_insert=1? Yes
  Shift right:  [3, 5, 5, 8]  (5 copied from position 1 to position 2)

  j=0: items[0]=3 > key_to_insert=1? Yes
  Shift right:  [3, 3, 5, 8]  (3 copied from position 0 to position 1)

  j=-1: Stop (reached start of list)
  Insert key:   [1, 3, 5, 8]  (key_to_insert=1 placed at position 0)

Result:         [1, 3, 5, 8]
```

This is the classic insertion sort algorithm, widely used because it is simple and efficient for small lists or nearly sorted data.

**Understanding the index manipulation**

The shift approach requires careful index management. Looking at the code, you might wonder: why `j = i - 1`? Why `j + 1` for both shifting and inserting? Let's clarify each choice.

**Why `j = i - 1`?**

We start `j` at position `i - 1` because:
- Position `i` contains the element we just saved in `key_to_insert`
- We need to compare against elements in the *already sorted portion* (positions 0 to `i-1`)
- So we start scanning from the last element of the sorted portion

**Why `items[j + 1] = items[j]` for shifting?**

During the while loop, `j` points to the element we're currently checking. If that element is greater than our key, we need to move it one position to the right to make room. Since `j` is the current position, `j + 1` is the position to the right.

**Why `j = j - 1` after each shift?**

After shifting an element to the right, we need to check the next element to the left. Decrementing `j` moves our "cursor" one position backward through the sorted portion. We keep doing this until either:
- We find an element that is NOT greater than our key (loop condition becomes false)
- We go past the beginning of the list (`j` becomes -1, so `j >= 0` becomes false)

**Why `items[j + 1] = key_to_insert` for insertion?**

When the while loop ends, `j` has one of two values:
- **Case A**: `j` points to an element that is ≤ our key (the loop stopped because `items[j] > key_to_insert` became false). Since `items[j]` is smaller or equal, our key must go in the position immediately after it.
- **Case B**: `j = -1` because we decremented past the start of the list (all elements were greater than the key). The key is the smallest, so it belongs at position 0. And indeed, `-1 + 1 = 0 = j + 1`.

In both cases, `j + 1` gives the correct insertion position.
````

---

### Exercise 1.5: Sort by string length

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
    for i in range(1, len(strings)):
        key_to_insert = strings[i]
        j = i - 1

        # Shift elements that are longer than key_to_insert
        while j >= 0 and len(strings[j]) > len(key_to_insert):
            strings[j + 1] = strings[j]
            j = j - 1

        strings[j + 1] = key_to_insert
    return strings

print(sort_by_length(["cat", "elephant", "dog", "a"]))  # ["a", "cat", "dog", "elephant"]
print(sort_by_length(["ab", "abc", "a"]))              # ["a", "ab", "abc"]
print(sort_by_length(["same", "size", "word"]))        # ["same", "size", "word"]
```

**Execution trace for `sort_by_length(["cat", "a", "elephant"])`**:

```
Initial:        ["cat", "a", "elephant"]

Pass 1 (i=1):
  Save key:     key_to_insert = "a" (len=1)
  Current:      ["cat", "a", "elephant"]

  j=0: len(strings[0])=3 > len("a")=1? Yes
  Shift right:  ["cat", "cat", "elephant"]

  j=-1: Stop (reached start of list)
  Insert key:   ["a", "cat", "elephant"]

Pass 2 (i=2):
  Save key:     key_to_insert = "elephant" (len=8)
  Current:      ["a", "cat", "elephant"]

  j=1: len(strings[1])=3 > len("elephant")=8? No
  Insert key:   ["a", "cat", "elephant"]  (no shifts needed)

Result:         ["a", "cat", "elephant"]
```
````

---

### Exercise 1.6: Find second largest

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
    # Initialize with first two elements in correct order
    if numbers[0] > numbers[1]:
        largest = numbers[0]
        second = numbers[1]
    else:
        largest = numbers[1]
        second = numbers[0]

    # Check remaining elements
    for item in numbers[2:]:
        if item > largest:
            second = largest
            largest = item
        elif item > second and item != largest:
            second = item

    return second

print(find_second_largest([3, 1, 4, 1, 5, 9, 2, 6]))  # 6
print(find_second_largest([10, 20]))                   # 10
print(find_second_largest([5, 5, 5, 3, 3]))           # 3
```

**Execution trace for `find_second_largest([3, 7, 2, 5, 9])`**:

| Item | largest | second | Action |
|------|---------|--------|--------|
| (init) | 7 | 3 | First two elements |
| 2 | 7 | 3 | 2 < second, no change |
| 5 | 7 | 5 | 5 > second and 5 != largest, update second |
| 9 | 9 | 7 | 9 > largest, update both |

**Result**: `7`

**Execution trace for `find_second_largest([5, 9, 9, 3])`** (with duplicates):

| Item | largest | second | Action |
|------|---------|--------|--------|
| (init) | 9 | 5 | First two elements |
| 9 | 9 | 5 | 9 > second but 9 == largest, no change |
| 3 | 9 | 5 | 3 < second, no change |

**Result**: `5`

The condition `item != largest` prevents duplicates of the largest value from incorrectly becoming the second largest.
````

---