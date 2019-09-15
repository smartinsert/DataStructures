# A class to represent the adjacency list of the node


class AdjListNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


# A class to represent a graph. A graph is the list of the adjacency lists.
# Size of the array will be the no. of the vertices "V"


class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.graph = [None] * vertices

    # Add an edge to an undirected graph
    def add_edge(self, source: int, destination: int):
        node = AdjListNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        node = AdjListNode(source)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def print_graph(self):
        for i in range(self.vertices):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


if __name__ == '__main__':
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
