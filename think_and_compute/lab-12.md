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

(ch-lab-12)=
# Loading data and querying with Blazegraph

```{admonition} Learning objectives
:class: tip
By the end of this lab, you will be able to:
- Set up a Python project with `uv` and manage dependencies
- Convert tabular data (CSV) into RDF triples using `rdflib`
- Upload an RDF graph to a Blazegraph triplestore
- Write SPARQL queries to retrieve and filter data from the triplestore
- Combine SPARQL query results with pandas operations to analyse data
```

This lab puts into practice the concepts introduced in the [Configuring and populating a graph database](20-graph-database.ipynb) and [Interacting with databases using Pandas](21-querying-databases.ipynb) chapters. You will take the Caravaggio dataset from {ref}`ch-lab-09` and represent it as RDF, upload it to Blazegraph, then use SPARQL queries to extract information.

---

## Managing Python projects with uv

In {ref}`ch-lab-01` you installed packages with `pip3 install`. That approach works for quick experiments, but when projects grow it becomes hard to manage. Different projects may need different versions of the same library, and if everything is installed globally, packages from one project can conflict with another. You can track dependencies with a `requirements.txt` file and use virtual environments to isolate them, but you have to create and maintain both by hand.

[uv](https://docs.astral.sh/uv/) is a modern Python project manager that handles all of this automatically. When you add a package with uv, it creates an isolated environment for your project, installs the package into that environment, and records its name in a configuration file called `pyproject.toml`. Anyone who receives your project folder can then recreate the exact same environment with a single command. You do not need to create virtual environments or write requirements files yourself.

### Installing uv

Open a terminal and run the appropriate command for your operating system.

````{tab-set}
```{tab-item} macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```{tab-item} Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
````

After installation, close and reopen your terminal so the `uv` command becomes available. You can verify it works by running:

```
uv --version
```

### Initialising a project

Each project (or lab) should live in its own folder with its own environment. Create a new folder for this lab and initialise it with uv:

````{tab-set}
```{tab-item} macOS / Linux
mkdir ~/Documents/lab-12-blazegraph
cd ~/Documents/lab-12-blazegraph
uv init
```

```{tab-item} Windows
mkdir %USERPROFILE%\Documents\lab-12-blazegraph
cd %USERPROFILE%\Documents\lab-12-blazegraph
uv init
```
````

The `uv init` command creates several files inside your folder:

- `pyproject.toml`: a file that describes your project and lists its dependencies. You do not need to edit this file by hand; uv updates it for you.
- `main.py`: a sample Python script with a simple "Hello world" program. You can replace its content with your own code or create new `.py` files alongside it.
- `README.md`: an empty readme file for describing your project.
- `.python-version`: a file that pins the Python version used by the project.

The first time you run `uv run` or `uv add`, uv also creates:

- `.venv/`: a directory containing the isolated Python environment. You can ignore this folder; uv manages it automatically.
- `uv.lock`: a lockfile that records the exact versions of all installed packages, so the environment can be reproduced identically on another machine.

Then open the folder in VS Code with **File -- Open Folder...**, as you have been doing since {ref}`ch-lab-01`.

```{admonition} One folder per project
:class: tip
It is good practice to keep separate folders for separate projects. Each folder gets its own environment with only the packages it needs, avoiding conflicts and making the project easier to share. From now on, create a new folder for each lab.
```

### Adding packages

To install a library and record it as a project dependency, use `uv add` followed by the package name. For example, to install the two libraries needed in this lab:

```
uv add rdflib SPARQLWrapper
```

This is the uv equivalent of `pip3 install`, with the advantage that the package is automatically recorded in `pyproject.toml`. If you ever need to set up the project on a different machine, running `uv sync` inside the folder will install all recorded packages automatically.

### Running your code

When you use uv, you run your Python scripts through `uv run` so that the isolated environment (with all installed packages) is active:

```
uv run python your_script.py
```

From this point on in the course, I will use `uv add` instead of `pip3 install` and `uv run` instead of calling `python3` directly.

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

Use a dictionary to store the mapping from each `museum_id` to its `URIRef`, so you can reference it when creating artwork triples. After processing all museums, print the number of triples in the graph (it should be 33: three triples per museum, times 11 museums).

```{code-cell} python
:tags: [hide-cell]
from rdflib import Graph, URIRef, Literal, RDF
from pandas import read_csv

my_graph = Graph()
base_url = "https://thinkcompute.github.io/res/"

Museum = URIRef("https://schema.org/Museum")
Church = URIRef("https://schema.org/Church")
name = URIRef("https://schema.org/name")
addressLocality = URIRef("https://schema.org/addressLocality")

df_museums = read_csv("notebook/museums.csv",
                      keep_default_na=False,
                      dtype={
                          "museum_id": "int",
                          "name": "string",
                          "city": "string",
                          "type": "string",
                          "founded": "int"
                      })

museum_resources = {}
for idx, row in df_museums.iterrows():
    subj = URIRef(base_url + "museum-" + str(row["museum_id"]))
    museum_resources[row["museum_id"]] = subj

    if row["type"] == "museum":
        my_graph.add((subj, RDF.type, Museum))
    else:
        my_graph.add((subj, RDF.type, Church))

    my_graph.add((subj, name, Literal(row["name"])))
    my_graph.add((subj, addressLocality, Literal(row["city"])))

print(len(my_graph))
```

### Exercise 1.2: Create resources for artworks

Load `artworks.csv` into a pandas DataFrame and, for each row, create the following RDF triples in the same graph:

- assign the type `schema:Painting`
- add the title using the `schema:name` property
- add the year using the `schema:dateCreated` property (cast the integer to a string, as shown in the [graph database chapter](20-graph-database.ipynb))
- add the genre using the `schema:genre` property
- link the artwork to its museum using the `schema:containedInPlace` property, with the museum `URIRef` retrieved from the dictionary built in the previous exercise

After processing all artworks, print the number of triples in the graph (it should be 108: the 33 museum triples plus 5 triples per artwork times 15 artworks).

```{code-cell} python
:tags: [hide-cell]
Painting = URIRef("https://schema.org/Painting")
dateCreated = URIRef("https://schema.org/dateCreated")
genre = URIRef("https://schema.org/genre")
containedInPlace = URIRef("https://schema.org/containedInPlace")

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

for idx, row in df_artworks.iterrows():
    subj = URIRef(base_url + "artwork-" + str(row["id"]))

    my_graph.add((subj, RDF.type, Painting))
    my_graph.add((subj, name, Literal(row["title"])))
    my_graph.add((subj, dateCreated, Literal(str(row["year"]))))
    my_graph.add((subj, genre, Literal(row["genre"])))
    my_graph.add((subj, containedInPlace, museum_resources[row["museum_id"]]))

print(len(my_graph))
```

---

## Part 2: Uploading data to Blazegraph

With the RDF graph ready in memory, you can now upload it to Blazegraph. As shown in the [graph database chapter](20-graph-database.ipynb), you use `SPARQLUpdateStore` from rdflib to connect to the Blazegraph SPARQL endpoint and add triples one by one.

```{admonition} Important
:class: warning
The exercises in this part and in Parts 3 and 4 require Blazegraph to be running on your machine. The code below will not work unless the database is reachable at `http://127.0.0.1:9999/blazegraph/sparql`.
```

### Exercise 2.1: Upload the graph to Blazegraph

Using `SPARQLUpdateStore`, open a connection to the Blazegraph SPARQL endpoint and upload all the triples from `my_graph`. Iterate over the triples using `my_graph.triples((None, None, None))` and add each one with `store.add()`. Remember to close the connection when done.

````{admonition} Solution
:class: tip, dropdown
```python
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore

store = SPARQLUpdateStore()
endpoint = "http://127.0.0.1:9999/blazegraph/sparql"
store.open((endpoint, endpoint))

for triple in my_graph.triples((None, None, None)):
    store.add(triple)

store.close()
```
````

After running this code, you can verify the upload by opening `http://127.0.0.1:9999/blazegraph/` in your browser and checking the number of triples reported.

---

## Part 3: Querying with SPARQL

With the data stored in Blazegraph, you can use SPARQL to retrieve it. To send a SPARQL query from Python and get the result as a pandas DataFrame, you use the `SPARQLWrapper` library. The workflow is: create a `SPARQLWrapper` object pointing to the endpoint, set the query and the return format (JSON), execute the query, and convert the JSON result into a DataFrame.

The following function wraps these steps. Define it at the top of your code, before the exercises, so you can reuse it throughout the lab:

```python
from SPARQLWrapper import SPARQLWrapper, JSON, POST
from pandas import DataFrame

def sparql_query(endpoint, query):
    sparql = SPARQLWrapper(endpoint)
    sparql.setMethod(POST)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    result = sparql.queryAndConvert()

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

The function sends the query to the endpoint using the HTTP POST method (required by Blazegraph), receives the results in JSON format, and converts each result row into a dictionary. The column names in the returned DataFrame match the variable names in the SPARQL query.

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
- **Querying with SPARQL**: using `SELECT`, triple patterns, `FILTER`, and `ORDER BY` to retrieve data from Blazegraph via `SPARQLWrapper`
- **Comparing approaches**: the same dataset queried with SQL in {ref}`ch-lab-11` and with SPARQL here, showing how different database technologies solve similar problems
- **Combining tools**: using SPARQL to extract data from the triplestore and pandas to process the results further

---

## Additional resources

- [rdflib documentation](https://rdflib.readthedocs.io/en/stable/)
- [SPARQL 1.1 query language specification](https://www.w3.org/TR/sparql11-query/)
- [Blazegraph quick start](https://github.com/blazegraph/database/wiki/Quick_Start)
- [SPARQLWrapper documentation](https://sparqlwrapper.readthedocs.io/en/latest/)
- [schema.org vocabulary](https://schema.org/)
