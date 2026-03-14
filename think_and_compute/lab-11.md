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

(ch-lab-11)=
# Storing and querying data with SQLite

```{admonition} Learning objectives
:class: tip
By the end of this lab, you will be able to:
- Create an SQLite database and populate it with pandas DataFrames using `to_sql()`
- Query a database using SQL via `read_sql()`
- Use SQL `SELECT`, `WHERE`, and `JOIN` clauses to extract data
- Combine SQL queries with pandas operations to analyse results
```

This lab puts into practice the concepts introduced in the [Configuring and populating a relational database](19-relational-database.ipynb) and [Interacting with databases using Pandas](21-querying-databases.ipynb) chapters. You will take the Caravaggio dataset from {ref}`ch-lab-09` and store it in an SQLite database, then use SQL queries to extract information from it.

---

## The dataset

This lab uses the same dataset from {ref}`ch-lab-09`. If you no longer have the files, you can download them again by clicking on each name:

- {Download}`artworks.csv <notebook/artworks.csv>`: a catalogue of 15 paintings by Caravaggio with their title, year, genre, dimensions (height and width in cm), and the museum where they are held
- {Download}`museums.csv <notebook/museums.csv>`: a list of 11 Italian museums and churches with their city, type, and founding year
- {Download}`collections.csv <notebook/collections.csv>`: a table linking each artwork to its room within the museum and its conservation condition

Download the three files and place them in the same folder where you will write your Python code.

---

## Part 1: Building the database

In {ref}`ch-lab-09`, you worked with three CSV files about Caravaggio's artworks in Italian museums. All the data lived in CSV files, and you used pandas to load, query, and combine it. Now you will store the same data in an SQLite database. The advantage of a database is that data is stored persistently in a structured format, and you can use SQL, a dedicated query language, to extract exactly the information you need.

### Exercise 1.1: Create the database and populate it

Load the three CSV files (`artworks.csv`, `museums.csv`, `collections.csv`) into pandas DataFrames, using the same `dtype` specifications as in the previous lab. Then, create an SQLite database called `caravaggio.db` and store each DataFrame as a table using `to_sql()`. Use `if_exists="replace"` so the code can be run multiple times without errors, and `index=False` to avoid writing the pandas index as a column.

```{code-cell} python
:tags: [hide-cell]
from sqlite3 import connect
from pandas import read_csv

df_artworks = read_csv("notebook/artworks.csv",
                        keep_default_na=False,
                        dtype={
                            "id": "int",
                            "title": "string",
                            "year": "int",
                            "genre": "string",
                            "height_cm": "int",
                            "width_cm": "int",
                            "museum_id": "int"
                        })

df_museums = read_csv("notebook/museums.csv",
                      keep_default_na=False,
                      dtype={
                          "museum_id": "int",
                          "name": "string",
                          "city": "string",
                          "type": "string",
                          "founded": "int"
                      })

df_collections = read_csv("notebook/collections.csv",
                          keep_default_na=False,
                          dtype={
                              "artwork_id": "int",
                              "room": "string",
                              "condition": "string"
                          })

with connect("notebook/caravaggio.db") as con:
    df_artworks.to_sql("Artwork", con, if_exists="replace", index=False)
    df_museums.to_sql("Museum", con, if_exists="replace", index=False)
    df_collections.to_sql("Collection", con, if_exists="replace", index=False)
```

### Exercise 1.2: Verify the database content

Use `read_sql()` to read the entire `Artwork` table from the database. The SQL query `SELECT * FROM Artwork` retrieves all columns and all rows from the table. Display the resulting DataFrame and verify it matches the original CSV data.

```{code-cell} python
:tags: [hide-cell]
from pandas import read_sql

with connect("notebook/caravaggio.db") as con:
    df_from_db = read_sql("SELECT * FROM Artwork", con)

df_from_db
```

---

## Part 2: Querying the database

With the data stored in the database, you can use SQL to extract exactly what you need. Each query is a string passed to `read_sql()`, and the result is returned as a pandas DataFrame. In this part, you will practice the most common SQL clauses: `SELECT` to choose which columns to retrieve, `WHERE` to filter rows by condition, and `ORDER BY` to sort results.

### Exercise 2.1: Select specific columns

Write an SQL query that retrieves only the `title` and `year` columns from the `Artwork` table. Display the result.

```{code-cell} python
:tags: [hide-cell]
with connect("notebook/caravaggio.db") as con:
    df_titles = read_sql("SELECT title, year FROM Artwork", con)

df_titles
```

### Exercise 2.2: Filter rows with WHERE

Write an SQL query that retrieves the title and year of all artworks painted after 1600. In SQL, conditions are expressed with the `WHERE` clause, using operators like `=`, `>`, `<`, `>=`, `<=`. Display the result.

```{code-cell} python
:tags: [hide-cell]
with connect("notebook/caravaggio.db") as con:
    df_after_1600 = read_sql("SELECT title, year FROM Artwork WHERE year > 1600", con)

df_after_1600
```

### Exercise 2.3: Combine conditions and sort results

Write an SQL query that retrieves the title, year, and genre of artworks that satisfy either of these conditions:
- genre is "mythological"
- genre is "religious" **and** year is after 1605

Order the results by year, from oldest to newest, using the `ORDER BY` clause.

This is the same filter you wrote with `df_artworks.query()` in {ref}`ch-lab-09`, Exercise 2.1, but now expressed in SQL with sorting added.

```{code-cell} python
:tags: [hide-cell]
with connect("notebook/caravaggio.db") as con:
    query = """
        SELECT title, year, genre
        FROM Artwork
        WHERE genre = 'mythological'
           OR (genre = 'religious' AND year > 1605)
        ORDER BY year
    """
    df_filtered = read_sql(query, con)

df_filtered
```

---

## Part 3: Working with multiple tables

In {ref}`ch-lab-09`, you used `merge()` to combine DataFrames from different CSV files. SQL provides a similar operation called `JOIN`, which combines rows from two tables based on a shared column. The syntax is:

```sql
SELECT columns
FROM TableA
JOIN TableB ON TableA.column = TableB.column
```

This produces a result where each row from `TableA` is matched with the corresponding row from `TableB` wherever the specified columns have the same value, just like `merge()` in pandas.

### Exercise 3.1: Join artworks with museums

Write an SQL query that joins the `Artwork` table with the `Museum` table, matching `Artwork.museum_id` with `Museum.museum_id`. Retrieve the artwork title, year, museum name, and city. Display the result.

```{code-cell} python
:tags: [hide-cell]
with connect("notebook/caravaggio.db") as con:
    query = """
        SELECT Artwork.title, Artwork.year, Museum.name, Museum.city
        FROM Artwork
        JOIN Museum ON Artwork.museum_id = Museum.museum_id
    """
    df_joined = read_sql(query, con)

df_joined
```

### Exercise 3.2: Join three tables and filter

Write an SQL query that joins all three tables (`Artwork`, `Collection`, and `Museum`) to retrieve the title, museum name, room, and condition of each artwork. Then, use pandas `query()` on the resulting DataFrame to find all artworks in "excellent" condition. Print the title and museum name of each one.

```{code-cell} python
:tags: [hide-cell]
with connect("notebook/caravaggio.db") as con:
    query = """
        SELECT Artwork.title, Museum.name, Collection.room, Collection.condition
        FROM Artwork
        JOIN Collection ON Artwork.id = Collection.artwork_id
        JOIN Museum ON Artwork.museum_id = Museum.museum_id
    """
    df_full = read_sql(query, con)

df_excellent = df_full.query("condition == 'excellent'")
for idx, row in df_excellent.iterrows():
    print(row["title"], "-", row["name"])
```

---

## Part 4: Final challenge

### Exercise 4.1: City report from the database

Using SQL queries and pandas operations, produce a summary report as a new DataFrame with one row per city and the following columns:

- `city`: the city name
- `num_museums`: the number of distinct museums in that city that hold Caravaggio artworks
- `num_artworks`: the total number of artworks held in that city
- `earliest`: the year of the earliest artwork in that city
- `latest`: the year of the latest artwork in that city

Save the result to a CSV file called `city_report.csv` (without the row index) and display the DataFrame.

````{admonition} Hint
:class: tip, dropdown
Start by writing an SQL query with `JOIN` to combine `Artwork` and `Museum`. Then iterate over the resulting DataFrame with `iterrows()` to aggregate information by city into a dictionary. Use a `set` to track distinct museum identifiers per city.
````

````{admonition} Solution
:class: tip, dropdown
```python
from sqlite3 import connect
from pandas import read_sql, DataFrame, Series

with connect("caravaggio.db") as con:
    query = """
        SELECT Artwork.title, Artwork.year, Museum.museum_id, Museum.name, Museum.city
        FROM Artwork
        JOIN Museum ON Artwork.museum_id = Museum.museum_id
    """
    df_full = read_sql(query, con)

report = dict()
for idx, row in df_full.iterrows():
    city = row["city"]

    if city not in report:
        report[city] = {
            "museums": set(),
            "num_artworks": 0,
            "earliest": row["year"],
            "latest": row["year"]
        }

    report[city]["museums"].add(row["museum_id"])
    report[city]["num_artworks"] = report[city]["num_artworks"] + 1

    if row["year"] < report[city]["earliest"]:
        report[city]["earliest"] = row["year"]

    if row["year"] > report[city]["latest"]:
        report[city]["latest"] = row["year"]

rows = list()
for city in report:
    row = Series({
        "city": city,
        "num_museums": len(report[city]["museums"]),
        "num_artworks": report[city]["num_artworks"],
        "earliest": report[city]["earliest"],
        "latest": report[city]["latest"]
    })
    rows.append(row)

df_report = DataFrame(rows)
df_report.to_csv("city_report.csv", index=False)
df_report
```
````

---

## Summary

In this lab, you practised:

- **Creating a database**: using `connect()` to create an SQLite database file and `to_sql()` to populate it with pandas DataFrames
- **Reading from a database**: using `read_sql()` to execute SQL queries and receive results as DataFrames
- **SQL syntax**: `SELECT` to choose columns, `WHERE` to filter rows with conditions, `JOIN` to combine tables on shared columns, `ORDER BY` to sort results
- **Combining tools**: using SQL to extract data from the database and pandas to process the results further

---

## Additional resources

- [Python sqlite3 documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQL tutorial on W3Schools](https://www.w3schools.com/sql/)
- [Pandas `to_sql` documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)
- [Pandas `read_sql` documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)

```{admonition} Next lab
:class: seealso
In the next lab, {ref}`ch-lab-12`, you will learn to represent the same dataset as RDF triples and query it using SPARQL on a Blazegraph triplestore, building on the concepts introduced in the [Configuring and populating a graph database](20-graph-database.ipynb) and [Interacting with databases using Pandas](21-querying-databases.ipynb) chapters.
```
