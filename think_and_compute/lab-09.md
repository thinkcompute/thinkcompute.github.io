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

(ch-lab-09)=
# Working with data in pandas

```{admonition} Learning objectives
:class: tip
By the end of this lab, you will be able to:
- Load CSV files into pandas DataFrames with correct data types
- Query and filter DataFrames using `query()` and `iterrows()`
- Join multiple DataFrames using `merge()`
- Save results to CSV files using `to_csv()`
```

This lab puts into practice the concepts introduced in the [Introduction to Pandas](17-pandas.ipynb) chapter. You will work with a dataset of artworks by Caravaggio held in Italian museums and churches, exploring how to load, query, and combine tabular data using pandas.

---

## The dataset: Caravaggio's artworks in Italy

The dataset for this lab consists of three CSV files stored in the `notebook/` directory:

- **[`artworks.csv`](notebook/artworks.csv)**: a catalogue of 15 paintings by Caravaggio with their title, year, genre, dimensions (height and width in cm), and the museum where they are held
- **[`museums.csv`](notebook/museums.csv)**: a list of 11 Italian museums and churches with their city, type, and founding year
- **[`collections.csv`](notebook/collections.csv)**: a table linking each artwork to its room within the museum and its conservation condition

These three tables are related: each row in `collections.csv` connects an artwork (by its `id`) to a specific room, while each artwork references a museum (by its `museum_id`). This is a common pattern in data management, where information is split across multiple tables to avoid repetition.

---

## Part 1: Loading and exploring the catalogue

In this first part, you will load the artworks dataset and explore its content using basic pandas operations.

### Exercise 1.1: Load the artworks catalogue

Load the file `notebook/artworks.csv` into a pandas DataFrame using `read_csv()`. Make sure to specify `keep_default_na=False` and provide a `dtype` dictionary so that each column is read with the correct data type: `"string"` for text columns and `"int"` for `id`, `year`, `height_cm`, `width_cm`, and `museum_id`. Display the resulting DataFrame.

```{code-cell} python
:tags: [hide-cell]
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
df_artworks
```

### Exercise 1.2: Count artworks by genre

Using `iterrows()`, count how many artworks belong to each genre. Build a dictionary where the keys are genre names and the values are the counts, then print it.

```{code-cell} python
:tags: [hide-cell]
genre_counts = dict()
for idx, row in df_artworks.iterrows():
    genre = row["genre"]
    if genre in genre_counts:
        genre_counts[genre] = genre_counts[genre] + 1
    else:
        genre_counts[genre] = 1

print(genre_counts)
```

---

## Part 2: Querying the catalogue

Now that you are familiar with the dataset, you will practice more advanced queries combining multiple conditions.

### Exercise 2.1: Multi-condition query

Find all artworks that satisfy either of these conditions:
- Genre is "mythological"
- Genre is "religious" **and** year is after 1605

Print the title of each matching artwork.

```{code-cell} python
:tags: [hide-cell]
df_result = df_artworks.query(
    "(genre == 'mythological') or (genre == 'religious' and year > 1605)"
)
for idx, row in df_result.iterrows():
    print(row["title"])
```

---

## Part 3: Working with multiple tables

In real datasets, information is often distributed across multiple tables. In this part, you will load additional CSV files and combine them with the artworks catalogue using `merge()`.

### Exercise 3.1: Load and join artworks with collections

Load `notebook/museums.csv` and `notebook/collections.csv` into two DataFrames, specifying `keep_default_na=False` and appropriate `dtype` dictionaries. Then, use `merge()` to join the artworks DataFrame with the collections DataFrame. The join should match the `id` column in artworks with the `artwork_id` column in collections. Display the resulting DataFrame and observe which columns it contains.

```{code-cell} python
:tags: [hide-cell]
from pandas import merge

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

df_art_collections = merge(df_artworks, df_collections, left_on="id", right_on="artwork_id")
df_art_collections
```

### Exercise 3.2: Chain a second merge and save results

Starting from the result of the previous exercise, perform a second `merge()` to add the museum names. Join on the `museum_id` column (present in both the artworks data and the museums data). Then, find all artworks in "excellent" condition and print their title and museum name. Finally, save the resulting DataFrame of excellent-condition artworks to a new CSV file called `notebook/excellent_artworks.csv`, using `to_csv()` with `index=False` to avoid writing the row index.

```{code-cell} python
:tags: [hide-cell]
df_full = merge(df_art_collections, df_museums, on="museum_id")
df_excellent = df_full.query("condition == 'excellent'")
for idx, row in df_excellent.iterrows():
    print(row["title"], "-", row["name"])

df_excellent.to_csv("notebook/excellent_artworks.csv", index=False)
```

---

## Part 4: Final challenge

### Exercise 4.1: Artworks per museum

Using all three CSV files, produce a dictionary where each key is a museum name and each value is the number of artworks that museum holds. Print the result.

````{admonition} Solution
:class: tip, dropdown
```python
from pandas import read_csv, merge

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

df_full = merge(df_artworks, df_collections, left_on="id", right_on="artwork_id")
df_full = merge(df_full, df_museums, on="museum_id")

museum_counts = dict()
for idx, row in df_full.iterrows():
    museum_name = row["name"]
    if museum_name in museum_counts:
        museum_counts[museum_name] = museum_counts[museum_name] + 1
    else:
        museum_counts[museum_name] = 1

print(museum_counts)
```
````

---

## Summary

In this lab, you practised:

- **Loading data**: using `read_csv()` with `keep_default_na=False` and `dtype` to control how pandas interprets each column
- **Exploring data**: iterating over rows with `iterrows()` and filtering with `query()`
- **Combining tables**: using `merge()` to join DataFrames on shared columns
- **Saving results**: writing DataFrames to CSV files with `to_csv()`

---

## Additional resources

- [Pandas user guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Pandas `read_csv` documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [Pandas `merge` documentation](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)
- [Programming Historian: pandas lessons](https://programminghistorian.org/en/lessons/?search=pandas)

```{admonition} Next lab
:class: seealso
In the next lab, {ref}`ch-lab-10`, you will learn to model data using Python classes, building on the concepts introduced in the [Implementation of data models via Python classes](16-data-models.ipynb) chapter.
```
