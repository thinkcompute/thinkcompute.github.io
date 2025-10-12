(ch-graphs)=
# Organising information: graphs
This chapter introduces the last data structure presented in this course, i.e. the *graph*. The historic hero introduced in these notes is Leonhard Euler, a great scientist of the 18<sup>th</sup> century who introduced a new mathematical field called graph theory for the very first time.


(sec-euler)=
## Historic hero: Euler

[Leonhard Euler](https://en.wikipedia.org/wiki/Leonhard_Euler) (shown in {numref}`euler`) was one of the most influential men of Science of whole history. His contributions in Mathematics, Physics, Astronomy, Logic, among others, were disruptive and even started pretty new disciplines. He spent most of his life in Saint Petersburg in Russia. Among the mathematical problems he dealt with, one related to a hilarious story that he solved by initiating a new field in mathematics called [graph theory](https://en.wikipedia.org/wiki/Graph_theory).

The (mathematical) story told about the [seven bridges of the city of Königsberg](https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg), illustrated in {numref}`bridges`. We can state the problem as follows: is it possible to walk around the town and cross each bridge once and only once? Several people have tried to propose a solution to this enigma before Euler. Finally, he demonstrated it through purely mathematical (and non-debatable) proof {cite}`euler_solutio_1741`.


```{figure} images/13-euler.png
---
name: euler
---
A portrait of Leonard Euler by Emanuel Handmann. Picture by Oursana, source: [Wikipedia](https://en.wikipedia.org/wiki/File:Leonhard_Euler.jpg).
```

```{figure} images/13-bridges.png
---
name: bridges
---
A representation of the seven bridges in Königsberg. Figure by Bogdan Giuşcă, source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Konigsberg_bridges.png).
```


He abstractly described the four lands in Königsberg divided by the river as *nodes* of a network, where each *edge* between two nodes represents one of the city’s bridges. [Figure 3](#bookmark=id.i6a4ckx7tq4j) shows his abstract representation of the problem. Using this abstract notion, known as *graph*, he demonstrated that there is *no solution* to the problem of the seven bridges of Königsberg.


```{figure} images/13-undirected-graph.png
---
name: undirected
---
An abstract representation of the seven bridges of Königsberg using a graph.
```


He based the solution to the problem on the following intuition. The idea was that each node, excepting the starting node and the final node, should have an even number of edges. It is a practical implication: one should pass through two different bridges (i.e. arts) to enter and then go out from a node. Thus, non-starting and non-ending nodes must have an even number of edges for being satisfactorily traversed one or more times. However, all the nodes in {numref}`undirected` have an odd number of edges, which contradicts the aforementioned requirement.


## Graphs

[Graphs](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)) are one of the principal data structures in Computer Science and Computational Thinking. For example, they describe routes between cities, connections to people in social networks, the organisation of links between Web pages, etc. {cite}`albert_statistical_2002`. Graphs are entirely derived from the mathematical structure invented by Euler, as illustrated in Section {ref}`sec-euler`. In particular, we can distinguish two different kinds of graphs: *undirected graphs* and *directed graphs*. In [undirected graphs](http://mathinsight.org/definition/undirected_graph), used by Euler in the seven bridges problem, one can traverse an edge in one way or the other indifferently. Instead, the edge specifies the direction for crossing it in [directed graphs](http://mathinsight.org/definition/directed_graph).

In Python, as it happens for the trees, there is no built-in class defining this type of object. However, several external libraries implement them. Among the most used and famous there is [NetworkX](https://networkx.github.io/). This library makes available the common constructs for creating and traversing graphs and additional functions for analysing them for different purposes, such as for the analysis of social networks.


### Undirected graphs

We can create an undirected graph using the constructor `Graph()`. Then, we make all the nodes and edges of such a new graph by using its available methods. 


```{code-block} python
---
name: py-graph
linenos: True
caption: |
    A simple undirected graph with four nodes and five edges. The source code of this listing is available {Download}`as part of the material of the course<./python/graph_instructions.py>`.
---
from networkx import Graph

# create a new graph
my_graph = Graph()

# create four nodes
my_graph.add_node(1)
my_graph.add_node(2)
my_graph.add_node(3)
my_graph.add_node(4)

# create five edges
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(1, 4)
my_graph.add_edge(2, 3)
my_graph.add_edge(3, 4)
```


The NetworkX package allows us to associate an **immutable object** as a node. We can connect such a node through one or more edges. In particular, it is possible to execute the following methods on a graph object:

* ​`<graph>.add_node(<node>) `adds `<node>` as a node of the graph – note that, if a node with that value is already present, the method does not affect the graph;
* ​`<graph>.add_edge(<node_1>, <node_2>)` adds an edge between `<node_1>` and `<node_2>` – note that, since we are dealing with undirected graphs, inverting the position of the input nodes does not change the result;
* ​`<graph>.remove_node(<node>)` removes `<node>` from the graph as well as all the edges that involve it directly;
* `​<graph>.remove_edge(<node_1>, <node_2>)` removes the particular edge between the two nodes specified.

{numref}`py-graph` introduces an example of a graph. It creates a structure similar to the one presented in {numref}`undirected`, except it is impossible to make multiple arcs between two nodes. Thus, using this specific constructor, it is impossible to create the same structure requested by Euler for solving the mathematical problem introduced in Section {ref}`sec-euler`.


```{code-block} python
---
name: py-multigraph
linenos: True
caption: |
    Another undirected graph that maps precisely the situation depicted in {numref}`undirected` since it allows the creation of multiple arcs between the same two nodes. The source code of this listing is available {Download}`as part of the material of the course<./python/multigraph_instructions.py>`.
---
from networkx import MultiGraph

# create a new graph
my_graph = MultiGraph()

# create four nodes
my_graph.add_node(1)
my_graph.add_node(2)
my_graph.add_node(3)
my_graph.add_node(4)

# create seven edges
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(1, 4)
my_graph.add_edge(1, 4)
my_graph.add_edge(2, 3)
my_graph.add_edge(3, 4)
```


To enable the creation of multiple edges between two nodes, we have to use a different kind of undirected graph using the constructor `MultiGraph()`. This graph accepts multiple edges between nodes by calling the method ​`<graph>.add_edge(<node_1>, <node_2>)` several times, and the method ​​`<graph>.remove_node(<node>)` will remove all the edges involving that input node, as usual. {numref}`py-multigraph` introduces an example of this kind of graph that maps precisely the one introduced in {numref}`undirected`.

Two additional methods are fundamental to understanding how a graph is composed and which nodes link to the others. They are `<graph>.nodes()` and `<graph>.edges()`, each returning a particular kind of lists (called `NodeView` and `EdgeView` respectively) that can be iterated by means of a *for-each* loop as usual. It is also possible to understand what are the nodes linked by a target node using the adjacency variable `<graph>.adj[<node>]`. This operation returns an `​AtlasView`: a kind of dictionary containing all the nodes reachable from `<node>`, where each dictionary key represents one of these nodes.


```{code-block} python
---
name: py-graph-metadata
linenos: True
caption: |
    The use of additional data for enriching nodes and edges of graphs. The source code of this listing is available {Download}`as part of the material of the course<./python/graph_attribute_instructions.py>`.
---
from networkx import Graph

# create a new graph
my_graph = Graph()  # it works also with MultiGraph

my_graph.add_node(1)  # no additional data
my_graph.add_node(2, name="John", surname="Doe")  # additional data
my_graph.add_node(3)

my_graph.nodes()
# Returns NodeView (tuple) with all the nodes:
# NodeView((1, 2, 3))

my_graph.nodes(data=True)
# Returns a NodeDataView (like a dictionary) with nodes + data:
# NodeDataView({1: {}, 2: {'name': 'John', 'surname': 'Doe'}, 3: {}})

my_graph.add_edge(1, 2)  # no additional data
my_graph.add_edge(1, 3, weight=4)  # additional data

my_graph.edges()
# Returns an EdgeView (of two-item tuples) with all the edges:
# EdgeView([(1, 2), (1, 3)])

my_graph.edges(data=True)
# Returns an EdgeDataView (of three-item tuples) with edges + data:
# EdgeDataView([(1, 2, {}), (1, 3, {'weight': 4})])

my_graph.adj[1]
# This returns an AtlasView (like a dictionary) containing all the 
# nodes that are reachable from an input one + data of edges:
# AtlasView({2: {}, 3: {'weight': 4}})
```


The value associated with each node, in this case, is another dictionary that is initialised empty if one did not specify any additional information explicitly. This information, or *attribute* in NetworkX, can be specified when one builds the edge connecting the two nodes. In particular, we use one or more pairs of a parameter and the value assigned to him via `=`, as shown in {numref}`py-graph-metadata`. We can do the same kind of assignments to nodes. In addition, these information can be also shown by executing the aforementioned methods `nodes()` and `edges()` by specifying the named parameter `data` as *True*, i.e. ​`<graph>.nodes(data=True)` and ​`<graph>.edges(data=True)`. This use of naming the parameters explicitly in Python when one wants to execute a method (or a function) is permissible by Python, as explained in [its documentation](https://docs.python.org/3/glossary.html#term-argument).


### Directed graphs

According to the NetworkX package, we can create a directed graph with the constructor `DiGraph()`. In NetworkX, a direct graph has the same methods of undirected graphs, presented in Section {ref}`sec-euler`. However, in this case, the order between `<node_1>` and `<node_2>` in the methods for adding and removing an edge is meaningful, since an edge specifies a particular direction: `<node_1>` is the source node, while `<node_2>` is the target node.

Also, it is possible to specify more than one edge between two nodes by using the constructor `MultiDiGraph()`. For instance, {numref}`directed` shows the abstract diagram of the graph implemented in {numref}`py-multigraph` if the constructor `MultiDiGraph()` would be used instead of `MultiGraph()`.


```{figure} images/13-directed-graph.png
---
name: directed
---
The diagram of the graph depicted in {numref}`undirected` and implemented in {numref}`py-graph` if we use `MultiDiGraph()` instead of `​MultiGraph()`.
```



## References

```{bibliography}
:filter: docname in docnames
```