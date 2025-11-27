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

(ch-lab-02)=
# Variables, types, and operators

```{admonition} Learning objectives
:class: tip
By the end of this lab, you will be able to:
- Follow Python naming conventions for variables
- Work with different data types (int, float, str, bool)
- Convert between data types
- Use arithmetic, comparison, logical, and assignment operators
- Manipulate strings effectively
- Combine these concepts to solve practical problems
```

---

## Part 1: Variables and naming conventions

### What you already know

In Lab 01, you learned that variables store data:

```{code-cell} python
paradox = "Liar Paradox"
```

Now let's dive deeper into **how to name variables properly** and **Python's naming rules**.

### Variable naming rules

```{code-cell} python
# Rule 1: must start with a letter or underscore
argument = "Cogito"
_hidden_premise = "Doubt"
# argument2 is valid
# 2argument is INVALID
```

```{code-cell} python
# Rule 2: can contain letters, numbers, and underscores only
publication_year = 1641
# publication-year is INVALID (hyphens not allowed)
# publication year is INVALID (spaces not allowed)
# publication$year is INVALID (special characters not allowed)
```

```{code-cell} python
# Rule 3: cannot use Python keywords
# Examples of keywords: if, for, while, class, def, return, True, False
name = "Socrates"  # valid
# class = "Ethics"  # INVALID - 'class' is a keyword
```

```{admonition} Don't worry about memorizing keywords
:class: note
You don't need to memorize all Python keywords right now. You'll learn them naturally as you practice writing Python code. If you accidentally try to use a keyword as a variable name, Python will give you an error message, and you'll simply need to choose a different name.
```

```{code-cell} python
# Rule 4: Python is case-sensitive
philosopher = "Socrates"
Philosopher = "Plato"
PHILOSOPHER = "Aristotle"

print(philosopher)   # Socrates
print(Philosopher)   # Plato
print(PHILOSOPHER)   # Aristotle
# These are three DIFFERENT variables!
```

### Python naming conventions (PEP 8)

Python has official style guidelines called [PEP 8](https://peps.python.org/pep-0008/). Here are the key naming conventions:

````{list-table}
:header-rows: 1

* - Type
  - Convention
  - Example
* - Variables
  - `snake_case` (lowercase with underscores)
  - `student_name`, `total_score`
* - Constants
  - `UPPER_CASE` (all caps with underscores)
  - `MAX_STUDENTS`, `PI`
* - Functions
  - `snake_case`
  - `calculate_average()`, `get_name()`
* - Classes
  - `CamelCase` (capitalize each word)
  - `Student`, `PhilosophicalSchool`
````

### Descriptive names matter

```{code-cell} python
# Bad: unclear what these mean
a = 365
b = 24
c = 60
result = a * b * c

# Good: clear and self-documenting
days_in_year = 365
hours_per_day = 24
minutes_per_hour = 60
minutes_in_year = days_in_year * hours_per_day * minutes_per_hour

print(f"There are {minutes_in_year:,} minutes in a year")
```

```{admonition} About the :, syntax
:class: note
The `:,` inside the f-string adds comma separators to make large numbers more readable (e.g., `525600` becomes `525,600`). We'll explore f-string formatting in detail later in Part 4.
```

### Interactive exercise 1: Variable naming

Fix the following code by correcting invalid variable names and improving unclear names:

```{code-cell} python
:tags: [hide-output]

# Fix this code (it has errors!)
# 1st-philosopher = "Friedrich Nietzsche"
# philosopher name = "Arthur Schopenhauer"
# class = "Ethics"
# s = "Existentialism"

# Your corrected code here:





```

````{admonition} Solution
:class: dropdown

```python
# Corrected and improved
first_philosopher = "Friedrich Nietzsche"  # Changed from 1st-philosopher
philosopher_name = "Arthur Schopenhauer"  # Added underscore
subject = "Ethics"  # Changed from 'class'
school = "Existentialism"  # More descriptive than 's'

print(f"{first_philosopher} and {philosopher_name}")
print(f"School: {school}")
print(f"Subject: {subject}")
```
````

---

## Part 2: Data types and type conversion

### Python's basic data types

Python has four fundamental data types:

#### 1. Integers (int)

Whole numbers without decimals:

```{code-cell} python
age = 17
year = 2025
points = -10

print(type(age))  # <class 'int'>
```

```{admonition} Note: the type() function
:class: note
The `type()` function shows what data type a variable contains. You'll see it used throughout this lab to verify data types. It's useful for debugging, but you won't use it much in real programs.
```

#### 2. Floating Point Numbers (float)

Numbers with decimals:

```{code-cell} python
temperature = 36.6
grade = 8.5
pi = 3.14159

print(type(pi))  # <class 'float'>
```

#### 3. Strings (str)

Text enclosed in quotes:

```{code-cell} python
name = "Baruch Spinoza"
quote = 'To think what one wills and to say what one thinks'
multiline = """This is a
multiline string"""

print(type(name))  # <class 'str'>
```

#### 4. Booleans (bool)

True or False values:

```{code-cell} python
is_valid = True
is_fallacy = False
is_sound = True

print(type(is_valid))  # <class 'bool'>
```

### Type conversion functions

You can convert between types:

```{code-cell} python
# String to Integer
age_str = "17"
age_int = int(age_str)
print(age_int + 3)  # 20
```

```{code-cell} python
# String to Float
price_str = "19.99"
price_float = float(price_str)
print(price_float * 2)  # 39.98
```

```{code-cell} python
# Number to String
year = 2025
year_str = str(year)
message = "The year is " + year_str
print(message)  # The year is 2025
```

```{code-cell} python
# Number to Boolean (0 is False, any other number is True)
print(bool(0))   # False
print(bool(1))   # True
print(bool(42))  # True
print(bool(-5))  # True
```

```{code-cell} python
# Boolean to Integer
print(int(True))   # 1
print(int(False))  # 0
```

### Common type conversion errors

```{code-cell} python
:tags: [raises-exception]

# This will cause an error!
# You cannot convert a non-numeric string to int
concept = "Epistemology"
# number = int(concept)  # ValueError!
```

```{code-cell} python
# Be careful with input()! It always returns a string
# Uncomment to try:
# user_age = input("Enter your age: ")
# next_year_age = user_age + 1  # Error! Can't add string + int

# Correct way:
# user_age = int(input("Enter your age: "))
# next_year_age = user_age + 1
```

---

## Part 3: Operators

### Arithmetic operators

```{code-cell} python
x = 10
y = 3

print(f"x + y = {x + y}")   # Addition: 13
print(f"x - y = {x - y}")   # Subtraction: 7
print(f"x * y = {x * y}")   # Multiplication: 30
print(f"x / y = {x / y}")   # Division: 3.333...
print(f"x // y = {x // y}") # Floor division: 3
print(f"x % y = {x % y}")   # Modulus (remainder): 1
print(f"x ** y = {x ** y}") # Exponentiation: 1000
```

### Practical example: Floor division vs. regular division

```{code-cell} python
# How many complete weeks in 50 days?
days = 50
days_per_week = 7

complete_weeks = days // days_per_week
remaining_days = days % days_per_week

print(f"{days} days = {complete_weeks} weeks and {remaining_days} days")
```

### Comparison operators

These return boolean values (True/False):

```{code-cell} python
socrates_lifespan = 71  # ~470-399 BCE
plato_lifespan = 80  # ~428-348 BCE
aristotle_lifespan = 62  # 384-322 BCE

print(f"Socrates and Plato same lifespan? {socrates_lifespan == plato_lifespan}")  # False
print(f"Aristotle lived shorter than Socrates? {aristotle_lifespan < socrates_lifespan}")  # True
print(f"Socrates lived longer than Plato? {socrates_lifespan > plato_lifespan}")  # False
print(f"Plato lived at least 80 years? {plato_lifespan >= 80}")  # True
print(f"Socrates and Aristotle had different lifespans? {socrates_lifespan != aristotle_lifespan}")  # True
```

````{admonition} Important: = vs ==
:class: warning
- `=` is **assignment**: `x = 5` (give x the value 5)
- `==` is **comparison**: `x == 5` (is x equal to 5?)

```python
age = 18     # Assignment: set age to 18
age == 18    # Comparison: check if age equals 18 (returns True)
```
````

### Logical operators

Combine boolean expressions:

```{code-cell} python
# Evaluating a philosophical argument
premises_are_true = True
logic_is_valid = True
widely_accepted = False

# AND: both must be True
print(f"Sound argument? {premises_are_true and logic_is_valid}")  # True
print(f"Valid but unsound? {logic_is_valid and not premises_are_true}")  # False

# OR: at least one must be True
print(f"Persuasive or valid? {widely_accepted or logic_is_valid}")  # True

# NOT: reverses the boolean
print(f"Contains logical fallacy? {not logic_is_valid}")  # False
print(f"Not widely accepted? {not widely_accepted}")  # True
```

### Assignment operators (shortcuts)

```{code-cell} python
points = 100

# Instead of: points = points + 10
points += 10  # Add and assign
print(f"After gaining 10: {points}")

# Instead of: points = points - 5
points -= 5   # Subtract and assign
print(f"After losing 5: {points}")

# Similarly:
points *= 2   # Multiply and assign
print(f"After doubling: {points}")

points //= 3  # Floor divide and assign
print(f"After floor division by 3: {points}")
```

---

## Part 4: String manipulation

### String methods

Strings have many useful built-in methods:

```{code-cell} python
concept = "Categorical Imperative"

print(concept.upper())        # CATEGORICAL IMPERATIVE
print(concept.lower())        # categorical imperative
print(concept.capitalize())   # Categorical imperative
print(concept.title())        # Categorical Imperative
```

```{code-cell} python
# Cleaning strings
messy_name = "  René Descartes  "
clean_name = messy_name.strip()
print(f"'{messy_name}' → '{clean_name}'")
```

```{code-cell} python
# Replacing text
quote = "I think, therefore I am"
new_quote = quote.replace("think", "doubt")
print(new_quote)  # I doubt, therefore I am
```

```{code-cell} python
# Splitting strings into lists
concept_words = "A priori knowledge".split(" ")
print(concept_words)  # ['A', 'priori', 'knowledge']
```

```{code-cell} python
# Checking string content
term = "Epistemology"
print(term.startswith("Epi"))  # True
print(term.endswith("logy"))   # True
print(term.isalpha())          # True (all letters)
print(term.isupper())          # False
```

### String concatenation

```{code-cell} python
# Using + operator
first_name = "Thomas"
last_name = "Aquinas"
full_name = first_name + " " + last_name
print(full_name)
```

```{code-cell} python
# Repeating strings with *
laugh = "ha" * 5
print(laugh)  # hahahahahaha
```

### String formatting (f-strings)

The modern and preferred way to format strings:

```{code-cell} python
name = "Spinoza"
excommunication_age = 23
principle = "Deus sive Natura"

# Old way (not recommended)
message1 = name + " was excommunicated at age " + str(excommunication_age) + " for arguing " + principle

# Modern way with f-strings (recommended!)
message2 = f"{name} was excommunicated at age {excommunication_age} for arguing '{principle}' (God equals Nature)"

print(message2)
```

```{admonition} What does the "f" in f-strings mean?
:class: note
The "f" stands for **"formatted"**. These are officially called **formatted string literals** and were introduced in Python 3.6 ([PEP 498](https://peps.python.org/pep-0498/)).
```

```{code-cell} python
# F-strings can include expressions
philosopher = "Giordano Bruno"
birth_year = 1548
death_year = 1600

message = f"{philosopher} lived {death_year - birth_year} years (from {birth_year} to {death_year})"
print(message)
```

```{code-cell} python
# Format numbers in f-strings
price = 19.99567
print(f"Price: ${price:.2f}")  # Round to 2 decimals: $19.00

large_number = 1234567
print(f"Population: {large_number:,}")  # Add commas: 1,234,567
```

### Other string formatting methods

```{code-cell} python
# Using .format() method
philosopher = "Hume"
faculty = "reason"
master = "the passions"

message1 = "{} argued that {} is merely a slave to {}".format(philosopher, faculty, master)
print(message1)

# Using % operator (old style, less common now)
thinker = "Hume"
observations = 1000

message2 = "%s noted that even after %d observations, we cannot prove causation" % (thinker, observations)
print(message2)

# But f-strings are the best!
name = "Hume"
source = "impressions"
derived = "ideas"

message3 = f"{name} claimed that all {derived} are ultimately derived from {source}"
print(message3)
```
---

## Exercise: Zeno's paradox

In Zeno's paradox, to reach a destination, you must first travel half the distance, then half of the remaining distance, then half of what's left, and so on infinitely. Zeno argued this makes motion impossible, since you'd need to complete an infinite number of steps.

Let's use Python to calculate the first few steps and see what happens to the remaining distance.

### Setup: Create a new file in VS Code

1. Open Visual Studio Code
2. Open your `python_laboratory` folder (the one you created in Lab 01):
   - **File → Open Folder...**
   - Navigate to and select your `python_laboratory` folder
3. Create a new file:
   - Click the **New File...** icon in the Explorer sidebar
   - Name it `zeno_paradox.py`

````{admonition} Requirements
:class: tip

1. Create a variable for the total distance: 100 meters

2. Calculate the remaining distance after each step:
   - Step 1: travel half the distance (50 m)
   - Step 2: travel half of the remaining distance
   - Step 3: travel half of what remains
   - Step 4: travel half of what remains

3. For each step, display:
   - The distance traveled in that step
   - The total distance covered so far
   - The remaining distance

4. Use f-strings to format the output clearly

5. Run your script by clicking the **Play button** (▶) in the top-right corner of VS Code

````

````{admonition} Solution
:class: dropdown

```python
# Initial setup
total_distance = 100
remaining_distance = total_distance
distance_covered = 0

print(f"Total distance to cover: {total_distance} meters")

# Step 1
step_distance = remaining_distance / 2
distance_covered += step_distance
remaining_distance -= step_distance
print(f"Step 1: travel {step_distance} m → covered {distance_covered} m → remaining {remaining_distance} m")

# Step 2
step_distance = remaining_distance / 2
distance_covered += step_distance
remaining_distance -= step_distance
print(f"Step 2: travel {step_distance} m → covered {distance_covered} m → remaining {remaining_distance} m")

# Step 3
step_distance = remaining_distance / 2
distance_covered += step_distance
remaining_distance -= step_distance
print(f"Step 3: travel {step_distance} m → covered {distance_covered} m → remaining {remaining_distance} m")

# Step 4
step_distance = remaining_distance / 2
distance_covered += step_distance
remaining_distance -= step_distance
print(f"Step 4: travel {step_distance} m → covered {distance_covered} m → remaining {remaining_distance} m")

print(f"After 4 steps, we've covered {distance_covered} m ({(distance_covered/total_distance)*100}% of the distance)")
print(f"Remaining: only {remaining_distance} m!")
```
````

---

## Summary

In this lab, you learned:

- **Variable naming rules and conventions** (snake_case, PEP 8)
- **Four basic data types**: int, float, str, bool
- **Type conversion** functions: `int()`, `float()`, `str()`, `bool()`
- **Arithmetic operators**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparison operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical operators**: `and`, `or`, `not`
- **Assignment operators**: `+=`, `-=`, `*=`, `/=`
- **String methods**: `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`
- **String formatting**: f-strings, `.format()`, `%`

```{admonition} Next lab
:class: tip
In **Lab 03**, you'll learn about lists, nested lists, for loops, conditional statements (if-else-elif), and how to define your own functions. You'll combine these concepts to build more complex programs.
```