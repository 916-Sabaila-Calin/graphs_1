class Graph:
    def __init__(self):
        self.__vertices = set()
        self.__outbound_neighbours = dict()
        self.__inbound_neighbours = dict()
        self.__costs = dict()

    def count_vertices(self):
        return len(self.__vertices)

    def count_edges(self):
        return len(self.__costs)

    def vertices_iterator(self):
        for vertex in self.__vertices:
            yield vertex

    def outbound_neighbours_iterator(self, vertex):
        if not self.is_vertex(vertex):
            raise Exception(f"The vertex {vertex} is not a part of the graph.")

        for neighbour in self.__outbound_neighbours[vertex]:
            yield neighbour

    def inbound_neighbours_iterator(self, vertex):
        if not self.is_vertex(vertex):
            raise Exception(f"The vertex {vertex} is not a part of the graph.")

        for neighbour in self.__inbound_neighbours[vertex]:
            yield neighbour

    def is_vertex(self, vertex):
        return vertex in self.__vertices

    def is_edge(self, from_vertex, to_vertex):
        return (from_vertex in self.__outbound_neighbours) and (to_vertex in self.__outbound_neighbours[from_vertex])

    def count_out_deg(self, vertex):
        if not self.is_vertex(vertex):
            raise Exception(f"The vertex {vertex} is not a part of the graph.")

        return len(self.__outbound_neighbours[vertex])

    def count_in_deg(self, vertex):
        if not self.is_vertex(vertex):
            raise Exception(f"The vertex {vertex} is not a part of the graph.")

        return len(self.__inbound_neighbours[vertex])

    def get_edge_cost(self, from_vertex, to_vertex):
        if not self.is_edge(from_vertex, to_vertex):
            raise Exception(f"The edge from {from_vertex} to {to_vertex} is not a part of the graph.")

        return self.__costs[(from_vertex, to_vertex)]

    def set_edge_cost(self, from_vertex, to_vertex, cost):
        if not self.is_edge(from_vertex, to_vertex):
            raise Exception(f"The edge from {from_vertex} to {to_vertex} is not a part of the graph.")

        self.__costs[(from_vertex, to_vertex)] = cost

    def add_vertex(self, vertex):
        if self.is_vertex(vertex):
            raise Exception(f"The vertex {vertex} is already a part of the graph.")

        self.__vertices.add(vertex)
        self.__outbound_neighbours[vertex] = set()
        self.__inbound_neighbours[vertex] = set()

    def erase_vertex(self, vertex):
        if not self.is_vertex(vertex):
            raise Exception(f"The vertex {vertex} is not a part of the graph.")

        edges_to_remove = []
        for elem in self.__outbound_neighbours[vertex]:
            edges_to_remove.append(vertex, elem)
        for elem in self.__inbound_neighbours[vertex]:
            edges_to_remove.append(elem, vertex)
        for edge in edges_to_remove:
            self.erase_edge(edge[0], edge[1])

        del self.__outbound_neighbours[vertex]
        del self.__inbound_neighbours[vertex]
        self.__vertices.remove(vertex)

    def add_edge(self, from_vertex, to_vertex, cost = 0):
        if not self.is_vertex(from_vertex):
            raise Exception(f"The vertex {from_vertex} is not a part of the graph.")
        if not self.is_vertex(to_vertex):
            raise Exception(f"The vertex {to_vertex} is not a part of the graph.")
        if self.is_edge(from_vertex, to_vertex):
            raise Exception(f"The edge from {from_vertex} to {to_vertex} is not a part of the graph.")

        self.__outbound_neighbours[from_vertex].add(to_vertex)
        self.__inbound_neighbours[to_vertex].add(from_vertex)
        self.__costs[(from_vertex, to_vertex)] = cost

    def erase_edge(self, from_vertex, to_vertex):
        if not self.is_vertex(from_vertex):
            raise Exception(f"The vertex {from_vertex} is not a part of the graph.")
        if not self.is_vertex(to_vertex):
            raise Exception(f"The vertex {to_vertex} is not a part of the graph.")
        if self.is_edge(from_vertex, to_vertex):
            raise Exception(f"The edge from {from_vertex} to {to_vertex} is not a part of the graph.")

        self.__outbound_neighbours[from_vertex].remove(to_vertex)
        self.__inbound_neighbours[to_vertex].remove(from_vertex)
        del self.__costs[(from_vertex, to_vertex)]


graph = Graph()
