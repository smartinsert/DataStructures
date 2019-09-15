# Graph

A data structure with a finite set of vertices and a finite set of
edges(ordered pair) represented as (u,v). Order is important in a
directional graph(di-graph)

## Representations
* **Adjacency Matrix**: 2D array of size VxV where V: number of vertices in the graph. It is always symmetric for an undirected graph. It is also used to represent weighted graphs. Removing an edge takes O(1) time and queries to know if there exists an edge takes O(1) time but consumes more space O(V^2). Adding a vertex takes O(V^2) time.
* **Adjacency List**: An array of list is used with size equal to the
  number of vertices. An entry array\[i\] represents the list of
  vertices adjacent to the i-th vertex.
* **Incidence Matrix**:
* **Incidence List**:

## Connectivity
* **Connected Component**: A connected component of an undirected graph
  is a subgraph in which every two vertices are connected to each other
  by a path(s), and which is connected to no other vertices outside the
  subgraph. A directed graph is **strongly connected** if there is a
  path between all pairs of vertices. A ***strongly connected component***
  (SCC) of a directed graph is a maximal strongly connected subgraph.