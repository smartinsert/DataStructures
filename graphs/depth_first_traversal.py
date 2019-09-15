from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def depth_first_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for i in self.graph[vertex]:
            if not visited[i]:
                self.depth_first_util(i, visited)

    def depth_first_traversal(self, vertex):
        visited = [False] * len(self.graph)
        self.depth_first_util(vertex, visited)

    def depth_first_traversal_for_disconnected_graph(self):
        visited = [False] * len(self.graph)
        for i in range(len(self.graph)):
            if not visited[i]:
                self.depth_first_util(i, visited)


if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    print("Following is a Depth First Traversal of the Graph starting from vertex 2")
    graph.depth_first_traversal(2)
    print("\n Following is a Depth First Traversal of the graph from all vertices")
    graph.depth_first_traversal_for_disconnected_graph()
