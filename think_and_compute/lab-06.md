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
- Transform problems into recursive formulations
- Identify base cases and recursive steps
- Trace the execution of recursive functions step by step
- Understand the recursive thinking pattern
```

---

## Thinking recursively

In {ref}`ch-recursion`, you learned that **recursion** is a technique where a function calls itself to solve smaller instances of the same problem. Every recursive solution needs two essential components:

1. **Base case**: A condition that stops the recursion (the simplest case that can be solved directly)
2. **Recursive step**: A call to the same function with a "smaller" or "simpler" input

In this section, I focus on the practical skill of **transforming a problem into a recursive formulation**. The goal is not to write complex recursive code, but to develop the mental pattern for recognizing and structuring recursive solutions.

### The recursive thinking pattern

When facing a problem, ask yourself these two questions:

1. **Can this problem be expressed in terms of a smaller version of itself?**
2. **What is the simplest case I can solve directly (without recursion)?**

If you can answer both questions, the problem is likely solvable with recursion.

### Example 1: Multiplication as repeated addition

Consider the problem of multiplying two positive integers without using the `*` operator. For example, `3 × 4 = 12`.

**Step 1: Express the problem in terms of a smaller version**

Multiplication can be seen as repeated addition:
- `3 × 4 = 3 + 3 + 3 + 3`

But we can also write:
- `3 × 4 = 3 + (3 × 3)`

This is the key insight! `3 × 4` depends on `3 × 3`, which is a *smaller* instance of the same problem.

**Step 2: Identify the base case**

What is the simplest multiplication? Multiplying by zero:
- `3 × 0 = 0`

Any number multiplied by zero gives zero. This is our base case.

**Step 3: Write the recursive formulation**

```
multiply(a, b):
    if b == 0:           # Base case
        return 0
    else:                # Recursive step
        return a + multiply(a, b - 1)
```

Let's trace through `multiply(3, 4)`:

```{code-cell} python
def multiply(a, b):
    if b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)

print(f"multiply(3, 4) = {multiply(3, 4)}")
```

**Visualizing the execution of `multiply(3, 4)`**:

```
multiply(3, 4)
│
├─▶ multiply(3, 3)
│   │
│   ├─▶ multiply(3, 2)
│   │   │
│   │   ├─▶ multiply(3, 1)
│   │   │   │
│   │   │   ├─▶ multiply(3, 0)
│   │   │   │   │
│   │   │   │   └── returns 0  [base case: b == 0]
│   │   │   │
│   │   │   └── returns 3 + 0 = 3
│   │   │
│   │   └── returns 3 + 3 = 6
│   │
│   └── returns 3 + 6 = 9
│
└── returns 3 + 9 = 12
```

### Example 2: Exponentiation as repeated multiplication

Now consider computing `a^n` (a raised to the power n) without using the `**` operator.

**Step 1: Express the problem in terms of a smaller version**

Exponentiation is repeated multiplication:
- `2^4 = 2 × 2 × 2 × 2`

We can write:
- `2^4 = 2 × (2^3)`

Again, `2^4` depends on `2^3`, a smaller instance.

**Step 2: Identify the base case**

Any number raised to the power 0 equals 1:
- `2^0 = 1`

**Step 3: Write the recursive formulation**

```{code-cell} python
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

print(f"2^4 = {power(2, 4)}")
print(f"3^3 = {power(3, 3)}")
print(f"5^0 = {power(5, 0)}")
```

**Visualizing the execution of `power(2, 4)`**:

```
power(2, 4)
│
├─▶ power(2, 3)
│   │
│   ├─▶ power(2, 2)
│   │   │
│   │   ├─▶ power(2, 1)
│   │   │   │
│   │   │   ├─▶ power(2, 0)
│   │   │   │   │
│   │   │   │   └── returns 1  [base case: n == 0]
│   │   │   │
│   │   │   └── returns 2 * 1 = 2
│   │   │
│   │   └── returns 2 * 2 = 4
│   │
│   └── returns 2 * 4 = 8
│
└── returns 2 * 8 = 16
```

### Example 3: Factorial

The factorial of n (written as n!) is the product of all positive integers from 1 to n:
- `5! = 5 × 4 × 3 × 2 × 1 = 120`

**Step 1: Express the problem in terms of a smaller version**

- `5! = 5 × 4!`

The factorial of 5 depends on the factorial of 4.

**Step 2: Identify the base case**

- `0! = 1` (by definition)
- `1! = 1`

**Step 3: Write the recursive formulation**

```{code-cell} python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(f"5! = {factorial(5)}")
print(f"0! = {factorial(0)}")
```

**Visualizing the execution of `factorial(4)`**:

```
factorial(4)
│
├─▶ factorial(3)
│   │
│   ├─▶ factorial(2)
│   │   │
│   │   ├─▶ factorial(1)
│   │   │   │
│   │   │   ├─▶ factorial(0)
│   │   │   │   │
│   │   │   │   └── returns 1  [base case: n == 0]
│   │   │   │
│   │   │   └── returns 1 * 1 = 1
│   │   │
│   │   └── returns 2 * 1 = 2
│   │
│   └── returns 3 * 2 = 6
│
└── returns 4 * 6 = 24
```

The vertical lines connect each recursive call to its return value. Notice how the deepest call (`factorial(0)`) returns first, and then each result propagates back up the chain.

### Summary of recursive thinking

| Problem | Recursive step | Base case |
|---------|---------------|-----------|
| `multiply(a, b)` | `a + multiply(a, b-1)` | `b == 0 → 0` |
| `power(a, n)` | `a * power(a, n-1)` | `n == 0 → 1` |
| `factorial(n)` | `n * factorial(n-1)` | `n == 0 → 1` |

Notice the pattern: each recursive step reduces the problem by 1 until it reaches the base case.

```{admonition} When to use recursion
:class: note
Recursion is elegant for problems that naturally divide into smaller subproblems (like tree structures, mathematical sequences, or divide-and-conquer algorithms). However, for simple loops over data, iteration (for/while) is often clearer and more efficient. In practice, most everyday programming uses iteration. Recursion becomes essential when dealing with hierarchical data structures like trees and graphs.
```

---

## Part 2: Recursion exercises

Now it's your turn to practice recursive thinking. This exercise will help you build confidence with the pattern before we move to more complex algorithms.

### Exercise 2.1: Count occurrences (recursively)

Implement a function `count_occurrences(items, target)` that counts how many times `target` appears in the list `items`, using recursion (no loops).

```python
print(count_occurrences([1, 2, 3, 2, 4, 2], 2))    # Expected: 3
print(count_occurrences(["a", "b", "a"], "a"))      # Expected: 2
print(count_occurrences([1, 2, 3], 5))              # Expected: 0
print(count_occurrences([], 1))                     # Expected: 0
```

````{admonition} Solution
:class: dropdown

**Recursive formulation**:
- **Base case**: An empty list contains 0 occurrences of any target
- **Recursive step**: If the first element matches, add 1 to the count of the rest; otherwise just return the count of the rest

```python
def count_occurrences(items, target):
    if len(items) == 0:
        return 0
    else:
        if items[0] == target:
            return 1 + count_occurrences(items[1:], target)
        else:
            return count_occurrences(items[1:], target)

print(count_occurrences([1, 2, 3, 2, 4, 2], 2))    # 3
print(count_occurrences(["a", "b", "a"], "a"))      # 2
print(count_occurrences([1, 2, 3], 5))              # 0
print(count_occurrences([], 1))                     # 0
```

**Execution trace for `count_occurrences([2, 1, 2], 2)`**:

**Step 1: The calls go DOWN (each call waits for the next one)**

```
count_occurrences([2, 1, 2], 2)    "Is 2 == 2? Yes! I'll return 1 + ..."
         │
         ▼
count_occurrences([1, 2], 2)      "Is 1 == 2? No. I'll just pass along ..."
         │
         ▼
count_occurrences([2], 2)         "Is 2 == 2? Yes! I'll return 1 + ..."
         │
         ▼
count_occurrences([], 2)          "Empty list! Base case: return 0"
```

**Step 2: The results come back UP**

```
count_occurrences([], 2)          returns 0
         │
         ▼
count_occurrences([2], 2)         returns 1 + 0 = 1
         │
         ▼
count_occurrences([1, 2], 2)      returns 1  (just passes the result, no match here)
         │
         ▼
count_occurrences([2, 1, 2], 2)   returns 1 + 1 = 2
```

**Result**: `2` (the value 2 appears twice in the list)
````