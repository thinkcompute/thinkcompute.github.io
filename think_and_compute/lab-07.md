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
# Working with files

```{admonition} Optional material
:class: warning
This lab covers file handling in Python. It is provided as extra material for students who want to learn about reading and writing files independently. This content will not be covered in class.
```

```{admonition} Learning objectives
:class: tip
By the end of this lab, you will be able to:
- Understand the difference between absolute and relative file paths
- Open, read, write, and append to text files
- Work with CSV files using the csv module
- Work with JSON files using the json module
- Choose the appropriate file format for different types of data
```

---

## Part 1: Introduction to files

So far, all the data in our programs has been temporary: variables exist only while the program runs. When the program ends, all data is lost. **Files** allow us to store data permanently on disk, so it persists between program executions.

### Why work with files?

- **Persistence**: Data survives after the program ends
- **Data sharing**: Files can be shared between programs or people
- **Large data**: Files can store more data than would fit in memory
- **Input/Output**: Read configuration, process datasets, generate reports

### File paths: absolute vs relative

Before opening a file, you need to specify its location using a **path**.

```{figure} img/paths.png
---
name: paths-diagram
alt: Diagram showing the difference between absolute and relative paths
---
The difference between absolute and relative paths. An absolute path starts from the root of the filesystem, while a relative path starts from the current working directory.
```

- **Absolute path**: The complete path from the root of the filesystem
  - Windows: `C:\Users\student\Documents\data.txt`
  - macOS/Linux: `/home/student/Documents/data.txt`

- **Relative path**: Path relative to the current working directory
  - `data.txt` (file in current directory)
  - `data/file.txt` (file in a subdirectory)
  - `../other/file.txt` (file in a sibling directory)

For this lab, I recommend keeping all your files in your `python_laboratory` folder and using relative paths.

---

## Part 2: Working with text files

### Opening and closing files

Python uses the `open()` function to access files. The basic syntax is:

```python
file = open("filename.txt", "r")  # Open for reading
# ... do something with the file ...
file.close()
```

The second argument specifies the **mode** (what you want to do with the file):
- `"r"` – Read (default): Open for reading, error if file doesn't exist
- `"w"` – Write: Create new file or overwrite existing
- `"a"` – Append: Add to the end of existing file (or create new)

```{admonition} The context manager: with statement
:class: tip
Always use the `with` statement when working with files. It automatically closes the file when done, even if an error occurs:

```python
with open("filename.txt", "r") as file:
    content = file.read()
# File is automatically closed here
```

This is safer and cleaner than manually calling `file.close()`.
```

### Writing to text files

Let's start by creating a file with some Nietzsche quotes:

```{code-cell} python
quotes = [
    "The devil is God's idleness on the seventh day. - Nietzsche, The Antichrist",
    "Is man merely a mistake of God's? Or God merely a mistake of man's? - Nietzsche, Twilight of the Idols",
    "In heaven, all the interesting people are missing. - Nietzsche, Letter to Franz Overbeck"
]

with open("nietzsche_quotes.txt", "w") as file:
    for quote in quotes:
        file.write(quote + "\n")  # \n adds a newline after each quote
```

```{admonition} The newline character
:class: note
When writing lines to a file, you need to explicitly add `\n` at the end of each line. Unlike `print()`, the `write()` method does not add a newline automatically.
```

### Reading from text files

There are several ways to read a file:

**Method 1: `read()` – Read entire file as a single string**

```{code-cell} python
with open("nietzsche_quotes.txt", "r") as file:
    content = file.read()

print(content)
print(f"Total characters: {len(content)}")
```

**Method 2: `readline()` – Read one line at a time**

```{code-cell} python
with open("nietzsche_quotes.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()

print(f"First line: {first_line}")
print(f"Second line: {second_line}")
```

**Method 3: `readlines()` – Read all lines into a list**

```{code-cell} python
with open("nietzsche_quotes.txt", "r") as file:
    lines = file.readlines()

print(f"Number of lines: {len(lines)}")
print(f"Lines: {lines}")
```

```{admonition} Newline characters in readlines()
:class: note
Notice that each line includes the `\n` character at the end. Use `.strip()` to remove it when processing each line.
```

### Appending to files

Use mode `"a"` to add content to an existing file without overwriting:

```{code-cell} python
new_quote = "A thinker sees his own actions as experiments and questions. - Nietzsche, The Gay Science"

with open("nietzsche_quotes.txt", "a") as file:
    file.write(new_quote + "\n")

# Verify the addition
with open("nietzsche_quotes.txt", "r") as file:
    for line in file:
        print(line.strip())
```

### Practical example: Counting words in a file

```{code-cell} python
with open("nietzsche_quotes.txt", "r") as file:
    content = file.read()

# Count words
words = content.split()
print(f"Total words: {len(words)}")

# Count lines
lines = content.strip().split("\n")
print(f"Total lines: {len(lines)}")

# Find quotes from a specific work
antichrist_quotes = []
for line in lines:
    if "Antichrist" in line:
        antichrist_quotes.append(line)
print(f"Quotes from The Antichrist: {len(antichrist_quotes)}")
```

---

## Part 3: Working with CSV files

Working with plain text files can become complicated when you need to store structured data. Every time you read or write data, you have to invent your own way to parse it: How do you separate different fields? How do you handle multiple records? What if a value contains your separator character?

To avoid these problems, we use standardized formats that define clear rules for structuring data. One of the simplest and most widely used is **CSV** (Comma-Separated Values).

CSV is a simple format for storing tabular data. Each line represents a row, and values are separated by commas (or other delimiters like semicolons).

### Why use CSV?

- **Simplicity**: Easy to create, read, and edit (even with a text editor)
- **Compatibility**: Opens directly in Excel, Google Sheets, and other spreadsheet software
- **Compact**: Smaller file size than JSON or XML for tabular data
- **Universal**: Supported by virtually every programming language and data tool

Example CSV content:
```
title,year,original_title
Thus Spoke Zarathustra,1883,Also sprach Zarathustra
Beyond Good and Evil,1886,Jenseits von Gut und Böse
The Birth of Tragedy,1872,Die Geburt der Tragödie
The Gay Science,1882,Die fröhliche Wissenschaft
```

### The csv module

Python's built-in `csv` module handles CSV files correctly, including edge cases like commas inside quoted fields.

### Writing CSV files

**Method 1: Using csv.writer()**

```{code-cell} python
import csv

# Data as a list of lists
nietzsche_works = [
    ["title", "year", "original_title"],  # Header
    ["The Birth of Tragedy", 1872, "Die Geburt der Tragödie"],
    ["Human, All Too Human", 1878, "Menschliches, Allzumenschliches"],
    ["The Gay Science", 1882, "Die fröhliche Wissenschaft"],
    ["Thus Spoke Zarathustra", 1883, "Also sprach Zarathustra"],
    ["Beyond Good and Evil", 1886, "Jenseits von Gut und Böse"],
    ["Twilight of the Idols", 1888, "Götzen-Dämmerung"]
]

with open("nietzsche_works.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(nietzsche_works)  # Write all rows at once
```

```{admonition} The newline parameter
:class: note
Always use `newline=""` when opening CSV files. This prevents issues with extra blank lines on Windows.
```

**Method 2: Using csv.DictWriter() (recommended)**

When you have data as dictionaries, `DictWriter` is more convenient:

```{code-cell} python
import csv

more_works = [
    {"title": "The Antichrist", "year": 1888, "original_title": "Der Antichrist"},
    {"title": "Ecce Homo", "year": 1888, "original_title": "Ecce homo"},
    {"title": "The Will to Power", "year": 1901, "original_title": "Der Wille zur Macht"}
]

with open("more_nietzsche_works.csv", "w", newline="") as file:
    fieldnames = ["title", "year", "original_title"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Write the header row
    writer.writerows(more_works)  # Write all data rows
```

### Reading CSV files

**Method 1: Using csv.reader()**

```{code-cell} python
import csv

with open("nietzsche_works.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)  # Read the first row (header)
    print(f"Columns: {header}")

    for row in reader:
        print(row)  # Each row is a list of strings
```

**Method 2: Using csv.DictReader() (recommended)**

`DictReader` reads the CSV file and returns each row as a dictionary, where the keys come from the first row (the header). This means you access values by column name instead of index position:

```{code-cell} python
import csv

with open("nietzsche_works.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"{row['title']} ({row['year']}) - {row['original_title']}")
```

```{admonition} The reader can only be read once
:class: warning
Both `csv.reader()` and `csv.DictReader()` are **iterators**: you can loop through it only once. After iterating, it is "exhausted" and will not produce any more rows. If you need to read the same data multiple times, you can save all rows into a list: `rows = list(reader)`. Then you can iterate over `rows` as many times as you need.

However, if you only need to process the data once, do not save it into a list. With an iterator, each row is discarded from memory after being processed, which is more efficient. Saving into a list means allocating memory (RAM) for all the data at once, which can be a problem with large files.
```

### Practical example: Filtering works by year

```{code-cell} python
import csv

works_after_1880 = []

with open("nietzsche_works.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["year"]) > 1880:
            works_after_1880.append(row["title"])

print(f"Works published after 1880: {works_after_1880}")
```

---

## Part 4: Working with JSON files

**JSON** (JavaScript Object Notation) is a format for storing structured data. Unlike CSV, JSON can represent nested and hierarchical data.

Example JSON content:
```json
{
    "title": "Blade Runner",
    "year": 1982,
    "director": "Ridley Scott",
    "cast": [
        {"actor": "Harrison Ford", "role": "Rick Deckard"},
        {"actor": "Rutger Hauer", "role": "Roy Batty"}
    ],
    "genres": ["sci-fi", "noir"],
    "based_on": {
        "title": "Do Androids Dream of Electric Sheep?",
        "author": "Philip K. Dick",
        "year": 1968
    }
}
```

### Why use JSON?

- **Hierarchical data**: Perfect for nested structures (objects inside objects)
- **Data types**: Preserves numbers, strings, booleans, lists, and objects
- **Web standard**: The most common format for web APIs
- **Human-readable**: Easy to read and edit

### JSON vs Python dictionaries

JSON and Python dictionaries are almost identical:

| JSON | Python |
|------|--------|
| `{}` object | `{}` dictionary |
| `[]` array | `[]` list |
| `"string"` | `"string"` |
| `123` / `3.14` | `123` / `3.14` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

### The json module

Python's `json` module converts between JSON strings and Python objects.

### Writing JSON files

```{code-cell} python
import json

film = {
    "title": "Blade Runner",
    "year": 1982,
    "director": "Ridley Scott",
    "cast": [
        {"actor": "Harrison Ford", "role": "Rick Deckard"},
        {"actor": "Rutger Hauer", "role": "Roy Batty"},
        {"actor": "Sean Young", "role": "Rachael"}
    ],
    "genres": ["sci-fi", "noir"],
    "based_on": {
        "title": "Do Androids Dream of Electric Sheep?",
        "author": "Philip K. Dick",
        "year": 1968
    },
    "is_cult_classic": True
}

with open("blade_runner.json", "w") as file:
    json.dump(film, file, indent=2)  # indent for pretty printing
```

```{admonition} The indent parameter
:class: tip
Use `indent=2` or `indent=4` to create human-readable JSON with proper indentation. Without it, the entire JSON is written on a single line.
```

### Reading JSON files

```{code-cell} python
import json

with open("blade_runner.json", "r") as file:
    data = json.load(file)

print(f"Film: {data['title']} ({data['year']})")
print(f"Director: {data['director']}")
print(f"Genres: {', '.join(data['genres'])}")
print(f"Based on: {data['based_on']['title']} by {data['based_on']['author']}")
```

### Working with lists of objects

JSON files often contain lists of objects:

```{code-cell} python
import json

sci_fi_films = [
    {
        "title": "Blade Runner",
        "year": 1982,
        "director": "Ridley Scott",
        "themes": ["identity", "humanity", "memory"]
    },
    {
        "title": "2001: A Space Odyssey",
        "year": 1968,
        "director": "Stanley Kubrick",
        "themes": ["evolution", "artificial intelligence", "exploration"]
    },
    {
        "title": "The Matrix",
        "year": 1999,
        "director": "The Wachowskis",
        "themes": ["simulation", "reality", "free will"]
    }
]

# Write
with open("sci_fi_films.json", "w") as file:
    json.dump(sci_fi_films, file, indent=2)

# Read
with open("sci_fi_films.json", "r") as file:
    data = json.load(file)

for film in data:
    themes = ", ".join(film["themes"])
    print(f"{film['title']} ({film['year']}): {themes}")
```

### Converting between JSON strings and Python objects

Sometimes you need to work with JSON as strings (e.g., from web APIs):

```{code-cell} python
import json

# Python object to JSON string
data = {"title": "Alien", "year": 1979, "director": "Ridley Scott"}
json_string = json.dumps(data)
print(f"JSON string: {json_string}")
print(f"Type: {type(json_string)}")

# JSON string to Python object
json_text = '{"title": "Stalker", "year": 1979, "director": "Andrei Tarkovsky"}'
python_obj = json.loads(json_text)
print(f"Python object: {python_obj}")
print(f"Type: {type(python_obj)}")
```

Note the difference:
- `json.dump()` / `json.load()` – work with **files**
- `json.dumps()` / `json.loads()` – work with **strings**

---

## Part 5: Choosing the right file format

Different file formats serve different purposes:

| Format | Best for | Limitations |
|--------|----------|-------------|
| **TXT** | Simple text, logs, notes | No structure, just text |
| **CSV** | Tabular data (rows and columns) | No nested data, all values are strings |
| **JSON** | Structured/nested data, configuration | Larger file size than CSV |

### Decision guide

- Use **TXT** when you just need to store plain text (logs, notes, simple lists)
- Use **CSV** when your data fits in a table (like a spreadsheet)
- Use **JSON** when your data has nested structures (objects inside objects)

### Example: Same data in different formats

**Film data:**

```python
{"title": "Blade Runner", "year": 1982, "genres": ["sci-fi", "noir"]}
```

**As TXT:**
```
Blade Runner
Year: 1982
Genres: sci-fi, noir
```

**As CSV:**
```
title,year,genres
Blade Runner,1982,"sci-fi, noir"
```

**As JSON:**
```json
{
  "title": "Blade Runner",
  "year": 1982,
  "genres": ["sci-fi", "noir"]
}
```

Notice that CSV requires quoting the genres field to handle the comma, and it loses the list structure (it becomes a single string). JSON preserves the list as a proper array.

---

## Part 6: Hands-on exercise

### Building a film collection manager

Create a program that manages a personal film collection stored in a JSON file.

**Setup:**

1. Create a file called `films.json` with the following content:

```json
[
  {
    "title": "Blade Runner",
    "year": 1982,
    "director": "Ridley Scott",
    "genres": ["sci-fi", "noir"]
  },
  {
    "title": "2001: A Space Odyssey",
    "year": 1968,
    "director": "Stanley Kubrick",
    "genres": ["sci-fi"]
  },
  {
    "title": "The Elephant Man",
    "year": 1980,
    "director": "David Lynch",
    "genres": ["biography", "drama"]
  },
  {
    "title": "The Fly",
    "year": 1986,
    "director": "David Cronenberg",
    "genres": ["horror", "sci-fi"]
  },
  {
    "title": "The Substance",
    "year": 2024,
    "director": "Coralie Fargeat",
    "genres": ["horror", "sci-fi"]
  },
  {
    "title": "Bugonia",
    "year": 2025,
    "director": "Yorgos Lanthimos",
    "genres": ["comedy", "sci-fi"]
  }
]
```

2. Create a new file: `film_collection.py`

**Requirements:**

1. Define `load_films(filename)` that:
   - Reads films from a JSON file
   - Returns a list of film dictionaries

2. Define `find_by_director(films, director)` that:
   - Searches for all films by a director (case-insensitive)
   - Returns a list of matching films

3. Define `films_by_decade(films)` that:
   - Groups films by decade (1960s, 1970s, 1980s, etc.)
   - Returns a dictionary where keys are decade strings and values are lists of film titles

4. Define `add_film(films, title, year, director, genres)` that:
   - Adds a new film dictionary to the list
   - Returns the updated list

5. Define `save_films(filename, films)` that:
   - Saves the list of films to a JSON file
   - Uses indentation for readability

````{admonition} Solution
:class: dropdown

```python
import json


def load_films(filename):
    with open(filename, "r") as file:
        return json.load(file)


def find_by_director(films, director):
    director_lower = director.lower()
    results = []
    for film in films:
        if film["director"].lower() == director_lower:
            results.append(film)
    return results


def films_by_decade(films):
    decades = {}
    for film in films:
        decade = (film["year"] // 10) * 10
        decade_str = f"{decade}s"
        if decade_str not in decades:
            decades[decade_str] = []
        decades[decade_str].append(film["title"])
    return decades


def add_film(films, title, year, director, genres):
    new_film = {
        "title": title,
        "year": year,
        "director": director,
        "genres": genres
    }
    films.append(new_film)
    return films


def save_films(filename, films):
    with open(filename, "w") as file:
        json.dump(films, file, indent=2)
```
````

---

## Summary

In this lab, you learned:

- **File paths**: The difference between absolute and relative paths
- **Text files**: How to open, read, write, and append to text files using `open()` and the `with` statement
- **CSV files**: How to use the `csv` module to read and write tabular data
- **JSON files**: How to use the `json` module to work with structured and nested data
- **Format selection**: When to use TXT, CSV, or JSON based on your data structure

---

## Additional resources

- [Python file handling documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python csv module documentation](https://docs.python.org/3/library/csv.html)
- [Python json module documentation](https://docs.python.org/3/library/json.html)
- [Real Python: Reading and writing files](https://realpython.com/read-write-files-python/)
- [Real Python: Working with JSON](https://realpython.com/python-json/)
