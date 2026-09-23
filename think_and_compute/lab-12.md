---
# SPDX-FileCopyrightText: 2026 Arcangelo Massari <arcangelo.massari@unibo.it>
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

(ch-lab-12)=
# Loading data and querying with Blazegraph

```{admonition} Learning objectives
:class: tip
By the end of this lab, you will be able to:
- Create the Blazegraph project with `uv init` and add its dependencies with `uv add`
- Convert tabular data (CSV) into RDF triples using `rdflib`
- Upload an RDF graph to a Blazegraph triplestore
- Write SPARQL queries to retrieve and filter data from the triplestore
- Combine SPARQL query results with pandas operations to analyse data
```

This lab puts into practice the concepts introduced in the [Configuring and populating a graph database](20-graph-database.ipynb) and [Interacting with databases using Pandas](21-querying-databases.ipynb) chapters. You will take the Caravaggio dataset from {ref}`ch-lab-09` and represent it as RDF, upload it to Blazegraph, then use SPARQL queries to extract information.

---

## Set up the Blazegraph project

Because you installed uv and learned its main commands in {ref}`ch-lab-01`, you can now set up the Blazegraph project. Create a `lab-12-blazegraph` folder, open it in VSCodium, and run these commands in the integrated terminal:

```bash
uv init --bare
uv add pandas rdflib sparqlite
```

Keep the Python files and downloaded CSV files in this folder, and run each script through the project environment:

```bash
uv run your_script.py
```

---

## Prerequisites: Blazegraph

Before starting the exercises, make sure Blazegraph is running on your machine. If you have not set it up yet, follow the instructions in the [Configuring and populating a graph database](20-graph-database.ipynb) chapter. In short:

1. Download the [Blazegraph JAR file](https://github.com/blazegraph/database/releases/download/BLAZEGRAPH_2_1_6_RC/blazegraph.jar) and place it in a folder of your choice
2. Open a terminal, navigate to that folder, and run:

```
java -server -Xmx1g -jar blazegraph.jar
```

The parts of this command are:
- `java`: runs the Java runtime (Blazegraph is written in Java)
- `-server`: optimises the Java virtual machine for long-running applications
- `-Xmx1g`: sets the maximum memory allocation to 1 gigabyte
- `-jar blazegraph.jar`: tells Java to execute the Blazegraph application packaged in the JAR file

3. Verify that Blazegraph is reachable at `http://127.0.0.1:9999/blazegraph/`

Leave the terminal open for the duration of the lab. Closing it will stop the database.

---

## The dataset

This lab uses the same dataset from {ref}`ch-lab-09`. If you no longer have the files, you can download them again by clicking on each name:

- {Download}`artworks.csv <notebook/artworks.csv>`: a catalogue of 15 paintings by Caravaggio with their title, year, genre, dimensions (height and width in cm), and the museum where they are held
- {Download}`museums.csv <notebook/museums.csv>`: a list of 11 Italian museums and churches with their city, type, and founding year

Download the two files and place them in the same folder where you will write your Python code.

---

## Part 1: Building the RDF graph

In {ref}`ch-lab-11`, you stored the Caravaggio data in a relational database using tables, columns, and SQL. A graph database works differently: data is represented as a set of triples (subject-predicate-object), and each entity is identified by a URL. In this part, you will convert the CSV data into RDF triples using `rdflib`, following the same approach shown in the [Configuring and populating a graph database](20-graph-database.ipynb) chapter.

The mapping from CSV columns to RDF uses existing classes and properties from [schema.org](https://schema.org):

| CSV concept | RDF class / property |
|---|---|
| A museum | [`https://schema.org/Museum`](https://schema.org/Museum) |
| A church | [`https://schema.org/Church`](https://schema.org/Church) |
| A painting | [`https://schema.org/Painting`](https://schema.org/Painting) |
| Name / title | [`https://schema.org/name`](https://schema.org/name) |
| City | [`https://schema.org/addressLocality`](https://schema.org/addressLocality) |
| Year of creation | [`https://schema.org/dateCreated`](https://schema.org/dateCreated) |
| Genre | [`https://schema.org/genre`](https://schema.org/genre) |
| Artwork held in museum | [`https://schema.org/containedInPlace`](https://schema.org/containedInPlace) |

Each resource will be identified by a URL built from the base `https://thinkcompute.github.io/res/` followed by a local identifier (e.g. `museum-1`, `artwork-5`).

### Exercise 1.1: Create resources for museums

Create an empty RDF graph using `Graph()`. Then load `museums.csv` into a pandas DataFrame and, for each row, create the following RDF triples:

- assign the type `schema:Museum` or `schema:Church` depending on the value in the `type` column
- add the museum name using the `schema:name` property
- add the city using the `schema:addressLocality` property

After processing all museums, iterate over the graph and print each triple to verify the result.

```{code-cell} python
:tags: [hide-cell]
from rdflib import Graph, URIRef, Literal, RDF
from pandas import read_csv

graph = Graph()
BASE_IRI = "https://thinkcompute.github.io/res/"

MUSEUM = URIRef("https://schema.org/Museum")
CHURCH = URIRef("https://schema.org/Church")
NAME = URIRef("https://schema.org/name")
LOCALITY = URIRef("https://schema.org/addressLocality")

df_museums = read_csv("notebook/museums.csv",
                      keep_default_na=False,
                      dtype={
                          "museum_id": "int",
                          "name": "string",
                          "city": "string",
                          "type": "string",
                          "founded": "int"
                      })

for idx, row in df_museums.iterrows():
    subject = URIRef(BASE_IRI + "museum-" + str(row["museum_id"]))

    if row["type"] == "museum":
        graph.add((subject, RDF.type, MUSEUM))
    elif row["type"] == "church":
        graph.add((subject, RDF.type, CHURCH))

    graph.add((subject, NAME, Literal(row["name"])))
    graph.add((subject, LOCALITY, Literal(row["city"])))

for triple in graph:
    print(triple)
```

### Exercise 1.2: Create resources for artworks

Load `artworks.csv` into a pandas DataFrame and, for each row, create the following RDF triples in the same graph:

- assign the type `schema:Painting`
- add the title using the `schema:name` property
- add the year using the `schema:dateCreated` property (cast the integer to a string, as shown in the [graph database chapter](20-graph-database.ipynb))
- add the genre using the `schema:genre` property
- link the artwork to its museum using the `schema:containedInPlace` property. Use a dictionary to store the mapping from each `museum_id` to its `URIRef`, so you can look up the correct museum resource for each artwork

After processing all artworks, print the number of triples in the graph (it should be 108: the 33 museum triples plus 5 triples per artwork times 15 artworks).

```{code-cell} python
:tags: [hide-cell]
PAINTING = URIRef("https://schema.org/Painting")
DATE_CREATED = URIRef("https://schema.org/dateCreated")
GENRE = URIRef("https://schema.org/genre")
CONTAINED_IN = URIRef("https://schema.org/containedInPlace")

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

museum_resources = {}
for idx, row in df_museums.iterrows():
    museum_resources[row["museum_id"]] = URIRef(BASE_IRI + "museum-" + str(row["museum_id"]))

for idx, row in df_artworks.iterrows():
    subject = URIRef(BASE_IRI + "artwork-" + str(row["id"]))

    graph.add((subject, RDF.type, PAINTING))
    graph.add((subject, NAME, Literal(row["title"])))
    graph.add((subject, DATE_CREATED, Literal(str(row["year"]))))
    graph.add((subject, GENRE, Literal(row["genre"])))
    graph.add((subject, CONTAINED_IN, museum_resources[row["museum_id"]]))

print(len(graph))
```

---

## Part 2: Uploading data to Blazegraph

With the RDF graph ready in memory, you can now upload it to Blazegraph. As shown in the [graph database chapter](20-graph-database.ipynb), you use `SPARQLUpdateStore` from rdflib to connect to the Blazegraph SPARQL endpoint and add triples one by one.

```{admonition} Important
:class: warning
The exercises in this part and in Parts 3 and 4 require Blazegraph to be running on your machine. The code below will not work unless the database is reachable at `http://127.0.0.1:9999/blazegraph/sparql`.
```

### Exercise 2.1: Upload the graph to Blazegraph

Using `SPARQLUpdateStore`, open a connection to the Blazegraph SPARQL endpoint and upload all the triples from `graph`. Iterate over the graph and add each triple with `store.add()`. Remember to close the connection when done.

````{admonition} Solution
:class: tip, dropdown
```python
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore

store = SPARQLUpdateStore()
endpoint = "http://127.0.0.1:9999/blazegraph/sparql"
store.open((endpoint, endpoint))

for triple in graph:
    store.add(triple)

store.close()
```
````

After running this code, you can verify the upload by opening `http://127.0.0.1:9999/blazegraph/` in your browser and checking the number of triples reported.

---

## Part 3: Querying with SPARQL

With the data stored in Blazegraph, you can use SPARQL to retrieve it. The most commonly used Python library for querying SPARQL endpoints is [SPARQLWrapper](https://sparqlwrapper.readthedocs.io/en/latest/). However, SPARQLWrapper has two known issues: it relies on [rdflib](https://rdflib.readthedocs.io/) internally for RDF representation, which adds parsing overhead, and it has a bug where HTTP connections are opened but never properly closed. In simple scripts these issues are rarely noticeable, but [SPARQLite](https://github.com/opencitations/sparqlite) is a lighter alternative that solves both problems.

The workflow is: create a `SPARQLClient` pointing to the endpoint, send the query, and convert the JSON result into a DataFrame. The following function wraps these steps. Define it at the top of your code, before the exercises, so you can reuse it throughout the lab:

```python
from sparqlite import SPARQLClient
from pandas import DataFrame

def sparql_query(endpoint, query):
    with SPARQLClient(endpoint) as client:
        result = client.query(query)

    variables = result["head"]["vars"]
    rows = list()
    for binding in result["results"]["bindings"]:
        row = dict()
        for var in variables:
            if var in binding:
                row[var] = binding[var]["value"]
            else:
                row[var] = ""
        rows.append(row)

    return DataFrame(rows)
```

The function sends the query to the endpoint, receives the results in JSON format, and converts each result row into a dictionary. The `SPARQLClient` is used within a context manager (`with`), which guarantees that the HTTP connection is properly closed after the query completes. The column names in the returned DataFrame match the variable names in the SPARQL query.

The general structure of a SPARQL query is:

```sparql
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>

SELECT ?variable1 ?variable2
WHERE {
    ?subject rdf:type schema:SomeClass .
    ?subject schema:someProperty ?variable1 .
}
```

Each line inside `WHERE { ... }` is a triple pattern. Variables (prefixed with `?`) match any value, while fixed terms (like `schema:Painting`) match only that specific resource. Blazegraph finds all combinations of values that satisfy every pattern simultaneously.

### Exercise 3.1: List all paintings with their titles

Write a SPARQL query that retrieves the title of every painting in the triplestore. Use two triple patterns: one to match resources of type `schema:Painting`, and another to get their `schema:name`. Pass the query to `sparql_query()` and display the resulting DataFrame.

````{admonition} Solution
:class: tip, dropdown
```python
endpoint = "http://127.0.0.1:9999/blazegraph/sparql"
query = """
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>

SELECT ?title
WHERE {
    ?painting rdf:type schema:Painting .
    ?painting schema:name ?title .
}
"""
df_paintings = sparql_query(endpoint, query)
df_paintings
```
````

### Exercise 3.2: Filter paintings by year

Write a SPARQL query that retrieves the title and year of all paintings created after 1600. Use a `FILTER` clause to test the year value. Since the year was stored as a string literal, you need to cast it to an integer inside the filter using the `xsd:integer()` function. To use `xsd:` as a prefix in your query, you need to know the full URL of the XML Schema namespace and declare it with a `PREFIX` line.

When you need to find the URL behind a well-known prefix, go to [prefix.cc](http://prefix.cc/). Type the prefix name (e.g. `xsd`) in the search box and the site will show you the corresponding URL. In this case, searching for `xsd` returns `http://www.w3.org/2001/XMLSchema#`, so the declaration to add at the top of your query is:

```sparql
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
```

Display the result.

````{admonition} Solution
:class: tip, dropdown
```python
query = """
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?title ?year
WHERE {
    ?painting rdf:type schema:Painting .
    ?painting schema:name ?title .
    ?painting schema:dateCreated ?year .
    FILTER (xsd:integer(?year) > 1600)
}
"""
df_after_1600 = sparql_query(endpoint, query)
df_after_1600
```
````

### Exercise 3.3: Retrieve artworks with their museum and city

Write a SPARQL query that retrieves the title, year, museum name, and city for each painting. This requires triple patterns that follow the link from painting to museum (via `schema:containedInPlace`) and then retrieve the museum's `schema:name` and `schema:addressLocality`. Display the result.

This is the SPARQL equivalent of the SQL `JOIN` you wrote in {ref}`ch-lab-11`, Exercise 3.1. In SPARQL, the join happens implicitly: the variable `?museum` appears both as the object of the artwork's `containedInPlace` pattern and as the subject of the museum's `name` and `addressLocality` patterns.

````{admonition} Solution
:class: tip, dropdown
```python
query = """
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>

SELECT ?title ?year ?museum_name ?city
WHERE {
    ?painting rdf:type schema:Painting .
    ?painting schema:name ?title .
    ?painting schema:dateCreated ?year .
    ?painting schema:containedInPlace ?museum .
    ?museum schema:name ?museum_name .
    ?museum schema:addressLocality ?city .
}
"""
df_joined = sparql_query(endpoint, query)
df_joined
```
````

### Exercise 3.4: Combine conditions and sort results

Write a SPARQL query that retrieves the title, year, and genre of paintings that satisfy either of these conditions:

- genre is "mythological"
- genre is "religious" **and** year is after 1605

Order the results by year (oldest first) using the `ORDER BY` clause.

This is the same filter you wrote in SQL in {ref}`ch-lab-11`, Exercise 2.3, now expressed in SPARQL.

````{admonition} Solution
:class: tip, dropdown
```python
query = """
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?title ?year ?genre
WHERE {
    ?painting rdf:type schema:Painting .
    ?painting schema:name ?title .
    ?painting schema:dateCreated ?year .
    ?painting schema:genre ?genre .
    FILTER (
        ?genre = "mythological"
        || (?genre = "religious" && xsd:integer(?year) > 1605)
    )
}
ORDER BY ?year
"""
df_filtered = sparql_query(endpoint, query)
df_filtered
```
````

---

## Part 4: Final challenge

### Exercise 4.1: City report from SPARQL

Using a SPARQL query and pandas operations, produce a summary report as a new DataFrame with one row per city and the following columns:

- `city`: the city name
- `num_museums`: the number of distinct museums in that city that hold Caravaggio artworks
- `num_artworks`: the total number of artworks held in that city
- `earliest`: the year of the earliest artwork in that city
- `latest`: the year of the latest artwork in that city

Save the result to a CSV file called `city_report_sparql.csv` (without the row index) and display the DataFrame.

This is the same report you built in {ref}`ch-lab-11`, Exercise 4.1, but the data now comes from a SPARQL query instead of an SQL query.

````{admonition} Hint
:class: tip, dropdown
Start by writing a SPARQL query that retrieves the title, year, museum URL, and city for every painting. Then iterate over the resulting DataFrame with `iterrows()` to aggregate information by city into a dictionary. Use a `set` to track distinct museum URLs per city. Remember to convert the year column to integers since `sparql_query()` returns all values as strings.
````

````{admonition} Solution
:class: tip, dropdown
```python
from pandas import DataFrame, Series

endpoint = "http://127.0.0.1:9999/blazegraph/sparql"
query = """
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>

SELECT ?title ?year ?museum ?city
WHERE {
    ?painting rdf:type schema:Painting .
    ?painting schema:name ?title .
    ?painting schema:dateCreated ?year .
    ?painting schema:containedInPlace ?museum .
    ?museum schema:addressLocality ?city .
}
"""
df_full = sparql_query(endpoint, query)
df_full["year"] = df_full["year"].astype("int")

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

    report[city]["museums"].add(row["museum"])
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
df_report.to_csv("city_report_sparql.csv", index=False)
df_report
```
````

---

## Summary

In this lab, you practised:

- **Creating an RDF graph**: using `Graph()`, `URIRef`, `Literal`, and `RDF.type` from rdflib to convert tabular data into RDF triples
- **Uploading to a triplestore**: using `SPARQLUpdateStore` to send triples to Blazegraph
- **Querying with SPARQL**: using `SELECT`, triple patterns, `FILTER`, and `ORDER BY` to retrieve data from Blazegraph via SPARQLite
- **Comparing approaches**: the same dataset queried with SQL in {ref}`ch-lab-11` and with SPARQL here, showing how different database technologies solve similar problems
- **Combining tools**: using SPARQL to extract data from the triplestore and pandas to process the results further

---

## Additional resources

- [rdflib documentation](https://rdflib.readthedocs.io/en/stable/)
- [SPARQL 1.1 query language specification](https://www.w3.org/TR/sparql11-query/)
- [Blazegraph quick start](https://github.com/blazegraph/database/wiki/Quick_Start)
- [SPARQLite documentation](https://opencitations.github.io/sparqlite/)
- [schema.org vocabulary](https://schema.org/)
