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

(ch-lab-06)=
# Algorithm exercises: recursion

```{admonition} Learning objectives
:class: tip
By the end of this lab, you will be able to:
- Apply a systematic 3-step method to formulate recursive solutions
- Identify base cases and recursive steps in new problems
- Recognize and fix common recursion errors
- Understand the difference between simple recursion and divide-and-conquer
- Apply divide-and-conquer to solve optimization problems
```

---

## Part 1: A method for thinking recursively

In {ref}`ch-recursion`, you learned that **recursion** is a technique where a function calls itself to solve smaller instances of the same problem. In this lab, I focus on giving you a **systematic method** for approaching any recursive problem. The goal is not to memorize solutions, but to develop a mental framework you can apply to problems you have never seen before.

### The 3-step method

When facing a problem that might be solved recursively, follow these three steps:

**Step 1: Identify the base case**

Ask yourself: *What is the simplest possible input I can solve directly, without recursion?*

- For **lists**: an empty list `[]` or a list with one element `[x]`
- For **numbers**: typically `0` or `1`
- For **strings**: an empty string `""` or a single character `"a"`

The base case is your "exit door" from the recursion. Without it, your function would call itself forever.

**Step 2: Formulate the recursive step**

Ask yourself: *How can I express this problem in terms of a smaller version of itself?*

The key insight is to:
1. Extract a small part of the input (e.g., the first element of a list)
2. Assume you already have a function that solves the problem for the rest
3. Combine the small part with the result from the rest

**Step 3: Verify convergence**

Ask yourself: *Does each recursive call get closer to the base case?*

If the input does not shrink with each call, you will have infinite recursion. Make sure that:
- Lists get shorter (e.g., `items[1:]` removes the first element)
- Numbers decrease (e.g., `n - 1`)
- Strings get shorter (e.g., `s[1:]` or `s[:-1]`)

### A mental template

Here is a thinking template (not code) that works for most recursive problems:

```
To solve PROBLEM(input):
1. If input is the simplest case → return DIRECT_ANSWER
2. Otherwise:
   a. Extract a part of the input (e.g., first element)
   b. Solve PROBLEM(rest of input)  ← recursive call
   c. Combine the partial result with the extracted part
   d. Return the combined result
```

### Example: sum of a list

Let me demonstrate the 3-step method with a concrete example: computing the sum of all numbers in a list.

**Step 1: Identify the base case**

What is the simplest list to sum? An empty list. The sum of no numbers is `0`.

**Step 2: Formulate the recursive step**

For a non-empty list like `[3, 1, 4, 1, 5]`:
- Extract the first element: `3`
- Assume we can already sum the rest: `sum_list([1, 4, 1, 5])` returns `11`
- Combine: `3 + 11 = 14`

So: `sum_list(items) = items[0] + sum_list(items[1:])`

**Step 3: Verify convergence**

Each recursive call uses `items[1:]`, which is one element shorter. Eventually, we reach an empty list (base case).

**Implementation:**

```{code-cell} python
def sum_list(items):
    if len(items) == 0:       # Base case: empty list
        return 0
    else:                     # Recursive step
        first = items[0]
        rest = items[1:]
        return first + sum_list(rest)

print(sum_list([3, 1, 4, 1, 5]))  # 14
print(sum_list([10]))             # 10
print(sum_list([]))               # 0
```

**Execution trace for `sum_list([3, 1, 4])`:**

```
sum_list([3, 1, 4])
│
├─▶ sum_list([1, 4])
│   │
│   ├─▶ sum_list([4])
│   │   │
│   │   ├─▶ sum_list([])
│   │   │   │
│   │   │   └── returns 0  [base case]
│   │   │
│   │   └── returns 4 + 0 = 4
│   │
│   └── returns 1 + 4 = 5
│
└── returns 3 + 5 = 8
```

The calls go **down** until we hit the base case, then the results come back **up**.

---

## Part 2: Guided exercises

Now it is your turn to apply the 3-step method. In these exercises, I guide you through the thinking process.

### Exercise 2.1: Length of a list

Implement a function `length(items)` that returns the number of elements in a list, **without using the built-in `len()` function**.

```python
print(length([1, 2, 3, 4, 5]))  # Expected: 5
print(length(["a", "b"]))       # Expected: 2
print(length([]))               # Expected: 0
```

```{admonition} Guided questions
:class: note
Before looking at the solution, answer these questions:
1. **Base case**: What is the length of an empty list?
2. **Recursive step**: If you know the length of `items[1:]`, how do you get the length of `items`?
3. **Convergence**: Does `items[1:]` get shorter with each call?
```

````{admonition} Solution
:class: dropdown

**Applying the 3-step method:**

1. **Base case**: The length of an empty list is `0`
2. **Recursive step**: `length(items) = 1 + length(items[1:])`
3. **Convergence**: Yes, `items[1:]` removes one element each time

```python
def length(items):
    if items == []:      # Base case: compare to empty list
        return 0
    else:
        return 1 + length(items[1:])

print(length([1, 2, 3, 4, 5]))  # 5
print(length(["a", "b"]))       # 2
print(length([]))               # 0
```

**Execution trace for `length([7, 8, 9])`:**

```
length([7, 8, 9])
│
├─▶ length([8, 9])
│   │
│   ├─▶ length([9])
│   │   │
│   │   ├─▶ length([])
│   │   │   │
│   │   │   └── returns 0  [base case]
│   │   │
│   │   └── returns 1 + 0 = 1
│   │
│   └── returns 1 + 1 = 2
│
└── returns 1 + 2 = 3
```
````

---

### Exercise 2.2: Check if element exists

Implement a function `contains(items, target)` that returns `True` if `target` is in the list, `False` otherwise. Do not use the `in` operator.

```python
print(contains([1, 2, 3, 4, 5], 3))   # Expected: True
print(contains([1, 2, 3, 4, 5], 7))   # Expected: False
print(contains([], 1))                 # Expected: False
print(contains(["a", "b", "c"], "b")) # Expected: True
```

```{admonition} Hint
:class: tip dropdown
This exercise has **two** base cases:
1. Empty list → the element is not there
2. First element matches → found it!

The recursive step only happens if neither base case applies.
```

````{admonition} Solution
:class: dropdown

**Applying the 3-step method:**

1. **Base cases**:
   - Empty list → return `False` (nothing to search)
   - First element equals target → return `True` (found it!)
2. **Recursive step**: If not found yet, search in the rest: `contains(items[1:], target)`
3. **Convergence**: Yes, `items[1:]` is shorter each time

```python
def contains(items, target):
    if len(items) == 0:           # Base case 1: empty list
        return False
    elif items[0] == target:      # Base case 2: found it
        return True
    else:                         # Recursive step
        return contains(items[1:], target)

print(contains([1, 2, 3, 4, 5], 3))   # True
print(contains([1, 2, 3, 4, 5], 7))   # False
print(contains([], 1))                 # False
print(contains(["a", "b", "c"], "b")) # True
```

**Execution trace for `contains([5, 8, 3], 8)`:**

```
contains([5, 8, 3], 8)
│
│   5 == 8? No
│
├─▶ contains([8, 3], 8)
│   │
│   │   8 == 8? Yes!
│   │
│   └── returns True  [base case 2]
│
└── returns True
```

**Execution trace for `contains([5, 8, 3], 9)`:**

```
contains([5, 8, 3], 9)
│
│   5 == 9? No
│
├─▶ contains([8, 3], 9)
│   │
│   │   8 == 9? No
│   │
│   ├─▶ contains([3], 9)
│   │   │
│   │   │   3 == 9? No
│   │   │
│   │   ├─▶ contains([], 9)
│   │   │   │
│   │   │   └── returns False  [base case 1: empty]
│   │   │
│   │   └── returns False
│   │
│   └── returns False
│
└── returns False
```
````

---

## Part 3: Finding and fixing recursion bugs

A critical skill in working with recursion is recognizing common mistakes. In this section, you will analyze buggy code and fix it.

### Exercise 3.1: Find the bug

Each of the following functions has a bug. Identify what is wrong and fix it.

**Bug 1:**

```python
def factorial(n):
    return n * factorial(n - 1)
```

**Bug 2:**

```python
def sum_positive(items):
    if len(items) == 0:
        return 0
    if items[0] > 0:
        return items[0] + sum_positive(items)
    else:
        return sum_positive(items)
```

**Bug 3:**

```python
def first_positive(items):
    if items[0] > 0:
        return items[0]
    else:
        return first_positive(items[1:])
```

````{admonition} Solution
:class: dropdown

**Bug 1: Missing base case**

The function never stops because there is no base case. When `n` reaches 0 or goes negative, it keeps calling itself.

```python
# Fixed version
def factorial(n):
    if n <= 1:           # Base case added
        return 1
    return n * factorial(n - 1)
```

**Bug 2: Non-convergent recursion**

The recursive calls use `items` instead of `items[1:]`, so the list never gets shorter. This causes infinite recursion.

```python
# Fixed version
def sum_positive(items):
    if len(items) == 0:
        return 0
    if items[0] > 0:
        return items[0] + sum_positive(items[1:])  # Fixed: items[1:]
    else:
        return sum_positive(items[1:])              # Fixed: items[1:]
```

**Bug 3: Missing base case for empty list**

If the list has no positive numbers, the function eventually receives an empty list and tries to access `items[0]`, causing an `IndexError`.

```python
# Fixed version
def first_positive(items):
    if len(items) == 0:      # Base case for empty list
        return None
    if items[0] > 0:
        return items[0]
    else:
        return first_positive(items[1:])
```
````

---

## Part 4: Divide-and-conquer

In {ref}`ch-divide-and-conquer`, you learned about the **divide-and-conquer** (D&C) paradigm. Now it is time to apply it. D&C is a special form of recursion where you:

1. **Divide** the problem into smaller subproblems (usually two halves)
2. **Conquer** each subproblem recursively
3. **Combine** the results of the subproblems

The key difference from simple recursion is that D&C typically divides the input **in half** (or similar proportions), rather than removing one element at a time. This often leads to more efficient algorithms.

### Simple recursion vs divide-and-conquer

With **simple recursion**, we remove one element at a time:

```
Simple recursion:
    f([1,2,3,4,5,6,7,8])
    └─▶ f([2,3,4,5,6,7,8])
        └─▶ f([3,4,5,6,7,8])
            └─▶ f([4,5,6,7,8])
                └─▶ ... and so on

    → 8 elements = 8 recursive calls
```

With **divide-and-conquer**, we split the problem in half each time:

```
Divide-and-conquer:
    f([1,2,3,4,5,6,7,8])         ← Level 1: full list
    │
    ├─▶ f([1,2,3,4])             ← Level 2: two halves
    │   ├─▶ f([1,2])             ← Level 3: quarters
    │   └─▶ f([3,4])
    │
    └─▶ f([5,6,7,8])
        ├─▶ f([5,6])
        └─▶ f([7,8])

    → 8 elements = only 3 levels deep
```

The difference matters for large inputs: processing 1000 elements with simple recursion requires 1000 calls, but D&C only needs about 10 levels (since we keep halving: 1000 → 500 → 250 → 125 → ...).

### Exercise 4.1: Find the longest word in a text

You are analyzing a literary text and want to find the longest word. Using divide-and-conquer, you can split the text, find the longest word in each half, and compare them.

This pattern is useful in text analysis: instead of scanning every word sequentially, D&C lets you process large texts by breaking them into manageable pieces.

```python
print(longest_word_dc("To be or not to be"))
# Expected: "not" (3 letters, first among equals)

print(longest_word_dc("It was the best of times"))
# Expected: "times" (5 letters)

print(longest_word_dc("Nevermore said the raven"))
# Expected: "Nevermore" (9 letters)

print(longest_word_dc("hello"))
# Expected: "hello"

print(longest_word_dc(""))
# Expected: ""
```

```{admonition} Hint
:class: tip dropdown
1. Split the text into a list of words first
2. **Base case**: If the list has 0 words, return "". If 1 word, return that word.
3. **Divide**: Split the word list in half
4. **Conquer**: Find the longest word in each half
5. **Combine**: Compare the two longest words, return the longer one
```

````{admonition} Solution
:class: dropdown

```python
def longest_in_list(words):
    # Base cases
    if len(words) == 0:
        return ""
    if len(words) == 1:
        return words[0]

    # Divide
    mid = len(words) // 2
    left_half = words[:mid]
    right_half = words[mid:]

    # Conquer
    longest_left = longest_in_list(left_half)
    longest_right = longest_in_list(right_half)

    # Combine: return the longer word
    if len(longest_left) >= len(longest_right):
        return longest_left
    else:
        return longest_right


def longest_word_dc(text):
    if text == "":
        return ""
    words = text.split()
    return longest_in_list(words)


print(longest_word_dc("To be or not to be"))
# "not"

print(longest_word_dc("It was the best of times"))
# "times"

print(longest_word_dc("Nevermore said the raven"))
# "Nevermore"

print(longest_word_dc("hello"))
# "hello"

print(longest_word_dc(""))
# ""
```

**Execution trace for `longest_word_dc("Call me Ishmael")`:**

```
longest_word_dc("Call me Ishmael")
│
│   text.split() → ["Call", "me", "Ishmael"]
│
└─▶ longest_in_list(["Call", "me", "Ishmael"])
    │
    │   mid = 1
    │   left = ["Call"], right = ["me", "Ishmael"]
    │
    ├─▶ longest_in_list(["Call"])
    │   └── returns "Call"  [base case: 1 word]
    │
    ├─▶ longest_in_list(["me", "Ishmael"])
    │   │
    │   │   mid = 1
    │   │
    │   ├─▶ longest_in_list(["me"])
    │   │   └── returns "me"
    │   │
    │   ├─▶ longest_in_list(["Ishmael"])
    │   │   └── returns "Ishmael"
    │   │
    │   │   len("me")=2 vs len("Ishmael")=7 → "Ishmael" wins
    │   │
    │   └── returns "Ishmael"
    │
    │   len("Call")=4 vs len("Ishmael")=7 → "Ishmael" wins
    │
    └── returns "Ishmael"
```
`````

---

### Exercise 4.2: Count character appearances in a text

You are analyzing a literary text and want to count how many times a specific character (like a letter or punctuation mark) appears. Use divide-and-conquer: split the text in half, count in each half, combine the results.

This mirrors how large-scale text analysis works: divide a massive corpus into chunks, process each chunk, aggregate results.

```python
text = "To be, or not to be, that is the question"

print(count_char_dc(text, "o"))    # Expected: 4
print(count_char_dc(text, "t"))    # Expected: 5
print(count_char_dc(text, ","))    # Expected: 2
print(count_char_dc(text, "z"))    # Expected: 0
print(count_char_dc("", "a"))      # Expected: 0
print(count_char_dc("aaa", "a"))   # Expected: 3
```

`````{admonition} Solution
:class: dropdown

```python
def count_char_dc(text, char):
    # Base cases
    if len(text) == 0:
        return 0
    if len(text) == 1:
        return 1 if text == char else 0

    # Divide
    mid = len(text) // 2
    left_half = text[:mid]
    right_half = text[mid:]

    # Conquer and combine
    left_count = count_char_dc(left_half, char)
    right_count = count_char_dc(right_half, char)

    return left_count + right_count


text = "To be, or not to be, that is the question"

print(count_char_dc(text, "o"))    # 4
print(count_char_dc(text, "t"))    # 5
print(count_char_dc(text, ","))    # 2
print(count_char_dc(text, "z"))    # 0
print(count_char_dc("", "a"))      # 0
print(count_char_dc("aaa", "a"))   # 3
```

**Execution trace for `count_char_dc("Romeo", "o")`:**

```
count_char_dc("Romeo", "o")
│
│   mid = 2
│   left = "Ro", right = "meo"
│
├─▶ count_char_dc("Ro", "o")
│   │
│   │   mid = 1
│   │   left = "R", right = "o"
│   │
│   ├─▶ count_char_dc("R", "o")
│   │   └── returns 0  [base case: "R" != "o"]
│   │
│   ├─▶ count_char_dc("o", "o")
│   │   └── returns 1  [base case: "o" == "o"]
│   │
│   └── returns 0 + 1 = 1
│
├─▶ count_char_dc("meo", "o")
│   │
│   │   mid = 1
│   │   left = "m", right = "eo"
│   │
│   ├─▶ count_char_dc("m", "o")
│   │   └── returns 0
│   │
│   ├─▶ count_char_dc("eo", "o")
│   │   │
│   │   ├─▶ count_char_dc("e", "o") → 0
│   │   ├─▶ count_char_dc("o", "o") → 1
│   │   │
│   │   └── returns 0 + 1 = 1
│   │
│   └── returns 0 + 1 = 1
│
└── returns 1 + 1 = 2
```

"Romeo" contains 2 occurrences of "o".
`````