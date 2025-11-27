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

(ch-lab-03)=
# Lists, loops, conditionals, and functions

```{admonition} Learning objectives
:class: tip
By the end of this lab, you will be able to:
- Create and manipulate lists in Python
- Access list elements using indexing and slicing
- Work with nested lists (lists of lists)
- Use for loops to iterate over lists
- Use if-else-elif statements for complex decision-making
- Define your own functions with parameters and return values
- Combine lists, loops, conditionals, and functions to solve problems
```

---

## Part 1: Lists in Python

### What is a list?

A **list** is an ordered, mutable collection of items. Lists are one of the most versatile and widely-used data structures in Python. They can contain items of any type (numbers, strings, even other lists), and items can be repeated.

Think of a list like a bookshelf: books are arranged in a specific order, you can add or remove books, and the same book can appear multiple times.

### Creating lists

There are two main ways to create lists:

```{code-cell} python
# Method 1: Using the list() constructor
empty_list = list()
print(empty_list)  # []
```

```{code-cell} python
# Method 2: Using square brackets (more common)
philosophers = ["Socrates", "Plato", "Aristotle"]
print(philosophers)
```

```{code-cell} python
# Lists can contain different types
mixed_list = ["Kant", 1724, True, 3.14]
print(mixed_list)
```

```{code-cell} python
# Lists can contain duplicates
arguments = ["premise", "premise", "conclusion"]
print(arguments)
```

### Adding elements to lists

```{code-cell} python
# append() adds one item to the end
schools = ["Rationalism", "Empiricism"]
schools.append("Existentialism")
print(schools)  # ['Rationalism', 'Empiricism', 'Existentialism']
```

```{code-cell} python
# extend() adds multiple items from another list
continental = ["Phenomenology", "Hermeneutics"]
schools.extend(continental)
print(schools)
```

```{code-cell} python
# insert() adds an item at a specific position
schools.insert(0, "Pre-Socratic")  # Insert at beginning (position 0)
print(schools)
```

### Removing elements from lists

```{code-cell} python
# remove() removes the first occurrence of a value
arguments = ["premise", "fallacy", "premise", "conclusion"]
arguments.remove("fallacy")
print(arguments)  # ['premise', 'premise', 'conclusion']
```

```{code-cell} python
# pop() removes and returns the last item (or item at index)
thinkers = ["Descartes", "Spinoza", "Leibniz"]
last = thinkers.pop()
print(f"Removed: {last}")
print(f"Remaining: {thinkers}")
```

```{code-cell} python
# pop(index) removes item at specific position
thinkers = ["Descartes", "Spinoza", "Leibniz"]
second = thinkers.pop(1)  # Remove item at index 1
print(f"Removed: {second}")
print(f"Remaining: {thinkers}")
```

### List length

```{code-cell} python
# len() returns the number of items
philosophers = ["Hume", "Berkeley", "Locke"]
count = len(philosophers)
print(f"Number of British Empiricists: {count}")
```

### Accessing list elements (indexing)

Lists are **zero-indexed**, meaning the first element is at position 0:

```{code-cell} python
virtues = ["Wisdom", "Courage", "Temperance", "Justice"]

print(virtues[0])   # First element: Wisdom
print(virtues[1])   # Second element: Courage
print(virtues[3])   # Fourth element: Justice
```

```{code-cell} python
# Negative indices count from the end
print(virtues[-1])  # Last element: Justice
print(virtues[-2])  # Second-to-last: Temperance
```

### List slicing

Slicing extracts a portion of a list using `[start:end]` (end is not included):

```{code-cell} python
philosophers = ["Thales", "Anaximander", "Anaximenes", "Heraclitus", "Parmenides"]

# Get first 3 elements
first_three = philosophers[0:3]
print(first_three)  # ['Thales', 'Anaximander', 'Anaximenes']
```

```{code-cell} python
# Shorthand: omit start to begin from beginning
first_three = philosophers[:3]
print(first_three)
```

```{code-cell} python
# Omit end to go until the end
from_third = philosophers[2:]
print(from_third)  # ['Anaximenes', 'Heraclitus', 'Parmenides']
```

```{code-cell} python
# Get middle elements
middle = philosophers[1:4]
print(middle)  # ['Anaximander', 'Anaximenes', 'Heraclitus']
```

```{code-cell} python
# Use negative indices in slicing
last_two = philosophers[-2:]
print(last_two)  # ['Heraclitus', 'Parmenides']
```

### Other useful list methods

```{code-cell} python
# count() returns how many times a value appears
premises = ["All humans are mortal", "Socrates is human", "All humans are mortal"]
count = premises.count("All humans are mortal")
print(f"This premise appears {count} times")
```

```{code-cell} python
# index() returns the position of first occurrence
schools = ["Stoicism", "Epicureanism", "Skepticism"]
position = schools.index("Epicureanism")
print(f"Epicureanism is at index {position}")
```

```{code-cell} python
# sort() arranges items in order (modifies the list)
thinkers = ["Zeno", "Aristotle", "Plato", "Socrates"]
thinkers.sort()
print(thinkers)  # Alphabetically sorted
```

```{code-cell} python
# reverse() reverses the order (modifies the list)
thinkers.reverse()
print(thinkers)
```

### Checking if an item is in a list

```{code-cell} python
# Use 'in' operator
virtues = ["Wisdom", "Courage", "Temperance", "Justice"]

print("Wisdom" in virtues)        # True
print("Prudence" in virtues)      # False
print("Justice" not in virtues)   # False
```

### Nested lists (lists of lists)

Lists can contain other lists as elements. This is useful for representing structured data where each item has multiple related fields.

```{code-cell} python
# Storing film information
# Each film is a list with [title, director, year]
films = [
    ["Blade Runner", "Scott", 1982],
    ["2001: A Space Odyssey", "Kubrick", 1968],
    ["The Elephant Man", "Lynch", 1980],
    ["Den Stygge Stesøsteren", "Blichfeldt", 2025]
]

# Access the first film
print(films[0])  # ['Blade Runner', 'Scott', 1982]

# Access the title of the first film
print(films[0][0])  # Blade Runner

# Access the director of the second film
print(films[1][1])  # Kubrick

# Access the year of the fourth film
print(films[3][2])  # 2025
```

```{admonition} Understanding double indexing
:class: note
When you have a nested list like `films = [["Title", "Director", 2020]]`:
- `films[0]` returns the first film (which is a list): `["Title", "Director", 2020]`
- `films[0][1]` first gets `films[0]` (the first film), then gets index `[1]` (the director): `"Director"`

Think of it as: "go to film 0, then get element 1 of that film"
```

---

## Part 2: Conditional statements (if-else-elif)

### Review: Basic if-else

You learned about `if` and `else` in the lectures. Let's review quickly:

```{code-cell} python
age = 18

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")
```

### Introducing elif

When you have **more than two possibilities**, use `elif` (short for "else if"):

```{code-cell} python
language = "Italian"

if language in ["Latin", "Italian", "French", "Spanish", "Portuguese"]:
    print("Romance language")
elif language in ["English", "German", "Dutch", "Swedish"]:
    print("Germanic language")
elif language in ["Russian", "Polish", "Czech"]:
    print("Slavic language")
elif language in ["Greek", "Armenian"]:
    print("Hellenic language")
else:
    print("Other language family")
```

```{admonition} How elif works
:class: note
Python checks conditions **from top to bottom** and executes the first block where the condition is True. Once a block executes, Python skips all remaining `elif` and `else` blocks.
```

### Conditionals with lists

```{code-cell} python
# Check if a list is empty
arguments = []

if len(arguments) == 0:
    print("No arguments provided")
else:
    print(f"Found {len(arguments)} arguments")
```

```{code-cell} python
# Alternative: empty lists are "falsy" in Python
arguments = []

if arguments:
    print("Arguments found")
else:
    print("No arguments")
```

```{code-cell} python
# Check list length
premises = ["All humans are mortal", "Socrates is human"]

if len(premises) < 2:
    print("Need at least 2 premises for a syllogism")
elif len(premises) == 2:
    print("Valid syllogism structure")
else:
    print("More than 2 premises - complex argument")
```

```{code-cell} python
# Check if item is in list
argument_type = "Ad hominem"
fallacies = ["Ad hominem", "Straw man", "False dilemma"]

if argument_type in fallacies:
    print(f"'{argument_type}' is a logical fallacy")
else:
    print(f"'{argument_type}' is not in the fallacy list")
```

### Nested conditionals

You can put conditionals inside other conditionals:

```{code-cell} python
author = "Moretti, F."
year = 2005
title = "Graphs, Maps, Trees"

if author:
    if year:
        if title:
            print(f"Complete APA reference: {author} ({year}). {title}")
        else:
            print("Missing title")
    else:
        print("Missing publication year")
else:
    print("Missing author")
```

### Combining conditions with logical operators

```{code-cell} python
# AND: both conditions must be True
age = 25
has_degree = True

if age >= 18 and has_degree:
    print("Eligible to apply for graduate program")
else:
    print("Not eligible")
```

```{code-cell} python
# OR: at least one condition must be True
language = "Greek"

if language == "Greek" or language == "Latin":
    print("Classical language")
else:
    print("Modern language")
```

```{code-cell} python
# Complex combinations
argument_length = 5
has_premises = True
has_conclusion = True

if argument_length >= 3 and has_premises and has_conclusion:
    print("Argument structure is complete")
elif not has_premises:
    print("Missing premises")
elif not has_conclusion:
    print("Missing conclusion")
else:
    print("Argument too short")
```

---

## Part 3: Iterating with for loops

### What is a for loop?

A `for` loop allows you to go through each element in a list and perform an action with it.

```{code-cell} python
# Basic for loop
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

```{admonition} How for loops work
:class: note
The `for` loop takes each element from the list, one at a time, and assigns it to the variable after `for`. Then it executes the indented code block:
1. `fruit = "apple"`, prints "apple"
2. `fruit = "banana"`, prints "banana"
3. `fruit = "orange"`, prints "orange"
```

### For loops with conditionals

```{code-cell} python
# Search for an item
authors = ["Austen", "Dickens", "Woolf", "Orwell"]

for author in authors:
    if author == "Woolf":
        print(f"Found {author}!")
```

### Building new lists with loops

```{code-cell} python
# Create a new list with uppercase names
names = ["alice", "bob", "charlie"]
uppercase_names = []

for name in names:
    uppercase_names.append(name.upper())

print(uppercase_names)  # ['ALICE', 'BOB', 'CHARLIE']
```

### For loops with nested lists

```{code-cell} python
# Iterate over a list of films
films = [
    ["Blade Runner", "Scott", 1982],
    ["2001: A Space Odyssey", "Kubrick", 1968],
    ["The Elephant Man", "Lynch", 1980],
    ["Den Stygge Stesøsteren", "Blichfeldt", 2025]
]

for film in films:
    title = film[0]
    director = film[1]
    year = film[2]
    print(f"{title} by {director} ({year})")
```

---

## Part 4: Defining functions

### What are functions?

**Functions** are reusable blocks of code that perform a specific task. They help you:
- Organize code into logical units
- Avoid repeating the same code
- Make code easier to read and maintain

### Basic function syntax

```{code-cell} python
# Define a function with def keyword
def greet():
    print("Hello, World!")

# Call the function
greet()
```

```{admonition} Important: Defining vs calling a function
:class: warning
**Defining a function does NOT execute it!** When you write `def greet():`, Python simply remembers the function exists. Nothing happens until you **call** (invoke) the function by writing `greet()` with parentheses.

Think of it like writing a recipe: defining the function is writing down the recipe, calling the function is actually cooking the dish.
```

### Functions with parameters

Parameters allow you to pass data into functions:

```{code-cell} python
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Silvio")
greet_person("Ivan")
```

```{code-cell} python
# Multiple parameters
def describe_book(title, author, year):
    print(f"'{title}' by {author} was published in {year}")

describe_book("Pride and Prejudice", "Jane Austen", 1813)
describe_book("1984", "George Orwell", 1949)
```

```{admonition} Parameter order matters!
:class: note
When calling a function, **the order of arguments matters**. Python matches arguments to parameters by position:
- `describe_book("1984", "George Orwell", 1949)` ✅ Correct
- `describe_book(1949, "1984", "George Orwell")` ❌ Wrong order!

You can avoid order issues by using **named arguments**:
```python
describe_book(year=1949, title="1984", author="George Orwell")
```
With named arguments, order doesn't matter because you explicitly specify which value goes to which parameter.

### Functions with return values

Use `return` to send a value back to the caller:

```{code-cell} python
def add_one(n):
    return n + 1

result = add_one(41)
print(result)
```

```{admonition} Functions always return something
:class: note
**Every function returns a value**, even if you don't specify `return`. If you don't use `return`, the function automatically returns `None`.

```python
def greet():
    print("Hello!")

result = greet()  # Prints "Hello!" but returns None
print(result)     # None
```

When you want to use the result of a function elsewhere in your code, you must explicitly `return` a value.

```{code-cell} python
def calculate_years(start_year, end_year):
    return end_year - start_year

years = calculate_years(1800, 1850)
print(f"Period duration: {years} years")
```

### Functions with conditionals

```{code-cell} python
def classify_argument(premise_count):
    if premise_count == 1:
        return "Simple argument"
    elif premise_count == 2:
        return "Syllogism"
    else:
        return "Complex argument"

result = classify_argument(2)
print(result)
```

### Functions with lists

```{code-cell} python
def count_items(items):
    return len(items)

authors = ["Austen", "Dickens", "Woolf"]
count = count_items(authors)
print(f"Number of authors: {count}")
```

### Function with list and conditionals

```{code-cell} python
def find_item(items, item):
    if item in items:
        position = items.index(item)
        return f"{item} found at position {position}"
    else:
        return f"{item} not found in the list"

fruits = ["apple", "banana", "orange"]
print(find_item(fruits, "banana"))
print(find_item(fruits, "grape"))
```

### Documenting functions with docstrings

```{code-cell} python
def calculate_average(numbers):
    """
    Calculate the arithmetic mean of a list of numbers.

    Parameters:
    numbers (list): A list of numeric values

    Returns:
    float: The average of the numbers
    """
    total = sum(numbers)
    count = len(numbers)
    return total / count

scores = [85, 90, 78, 92]
average = calculate_average(scores)
print(f"Average score: {average}")
```

```{admonition} Why use docstrings?
:class: note
Docstrings (triple-quoted strings right after `def`) document what your function does, what parameters it expects, and what it returns. This helps others (and your future self) understand your code.
```

---

## Part 5: Hands-on exercise

### Library manager

Create a program that manages a personal library of books.

**Setup:**
Create a new file: `library_manager.py`

**Requirements:**
1. Create an empty list `library`
2. Define `add_book(library, title, author, year)` that creates a book as a list `[title, author, year]` and adds it to the library
   - Each book is stored as a list with 3 elements
3. Define `find_by_author(library, author)` that returns all books by a specific author
4. Define `find_by_decade(library, year)` that returns all books from the same decade as the given year
   - For example, if you pass 1945, it finds books from 1940-1949
5. Define `print_library(library)` that displays all books with numbers

**Example usage:**
```python
add_book(library, "La Bufera e altro", "Montale", 1956)
add_book(library, "Il Nome della Rosa", "Eco", 1980)
add_book(library, "Se questo è un uomo", "Levi", 1947)

print_library(library)
# Should print numbered list

books_1940s = find_by_decade(library, 1945)  # Finds books from 1940-1949
# Should return books from the 1940s decade
```

````{admonition} Solution
:class: dropdown

```python
# Create empty library
library = []

def add_book(library, title, author, year):
    """Add a book to the library."""
    book = [title, author, year]
    library.append(book)
    return library

def find_by_author(library, author):
    """Find all books by a specific author."""
    found_books = []
    for book in library:
        if book[1] == author:  # book[1] is the author
            found_books.append(book)
    return found_books

def find_by_decade(library, year):
    """Find all books from the same decade as the given year."""
    # Calculate the start of the decade
    start_year = (year // 10) * 10
    end_year = start_year + 9

    found_books = []
    for book in library:
        book_year = book[2]  # book[2] is the year
        if start_year <= book_year <= end_year:
            found_books.append(book)

    return found_books

def print_library(library):
    """Print all books with numbers."""
    print("=== Library Contents ===")
    counter = 1
    for book in library:
        print(f"{counter}. {book[0]} by {book[1]} ({book[2]})")
        counter += 1

# Add books
add_book(library, "Le Comte de Monte-Cristo", "Dumas", 1844)
add_book(library, "Il Fu Mattia Pascal", "Pirandello", 1904)
add_book(library, "Cristo si è fermato a Eboli", "Levi", 1945)
add_book(library, "Se questo è un uomo", "Levi", 1947)
add_book(library, "La Bufera e altro", "Montale", 1956)
add_book(library, "La Bufera e altro", "Montale", 1956)
add_book(library, "Il Nome della Rosa", "Eco", 1980)

# Display full library
print_library(library)

# Find books by author
print("\n=== Books by Levi ===")
levi_books = find_by_author(library, "Levi")
for book in levi_books:
    print(f"{book[0]} by {book[1]} ({book[2]})")

# Find books from 1940s
print("\n=== Books from 1940s ===")
books_1940s = find_by_decade(library, 1945)  # Any year in the 1940s
for book in books_1940s:
    print(f"{book[0]} by {book[1]} ({book[2]})")
```
````

---

## Summary

In this lab, you learned:

- **Creating and manipulating lists**: `list()`, `[]`, `append()`, `extend()`, `insert()`, `remove()`, `pop()`
- **Accessing list elements**: indexing `[0]`, negative indices `[-1]`, slicing `[start:end]`
- **List methods**: `len()`, `count()`, `index()`, `sort()`, `reverse()`
- **Nested lists**: creating and accessing lists of lists with double indexing `list[0][1]`
- **Conditional statements**: `if`, `elif`, `else`
- **Combining conditions**: `and`, `or`, `not`, `in`
- **For loops**: iterating over lists with `for item in list:`
- **Loops with conditionals**: combining `for` and `if` to filter and process data
- **Defining functions**: `def`, parameters, `return`
- **Functions with lists and loops**: passing lists, iterating, creating new lists
- **Documentation**: docstrings for function documentation

```{admonition} Next lab
:class: tip
In **Lab 04**, you will learn about sets and dictionaries.
```

## Additional resources

- [Python lists documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python for loops documentation](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python functions documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python conditionals documentation](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
