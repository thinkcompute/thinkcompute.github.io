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

(ch-lab-07)=
# Algorithm exercises: divide-and-conquer

```{admonition} Learning objectives
:class: tip
By the end of this lab, you will be able to:
- Understand the difference between simple recursion and divide-and-conquer
- Apply divide-and-conquer to solve optimization problems
```

---

## Part 1: Divide-and-conquer

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

### Exercise 1.1: Find the longest word in a text

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

### Exercise 1.2: Count character appearances in a text

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
