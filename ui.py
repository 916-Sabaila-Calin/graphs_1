from graph import *


class UI:
    def __init__(self, graph):
        self.__graph = graph

    @staticmethod
    def print_main_menu():
        print("")
        print("Press 1 to display the vertex operations.")
        print("Press 2 to display the edge operations.")
        print("Press 3 to generate a random graph.")
        print("Press 4 to import a graph from a text file.")
        print("Press 5 to export the graph to a text file.")
        print("Press 6 to print the graph.")
        print("Type \"exit\" to close the program.")

    @staticmethod
    def print_vertex_menu():
        print("")
        print("Press 1 to add a vertex.")
        print("Press 2 to remove a vertex.")
        print("Press 3 to check if a vertex exists.")
        print("Press 4 to print the number of vertices.")
        print("Press 5 to print the vertices.")
        print("Press 6 to print the outdegree of a vertex.")
        print("Press 7 to print the indegree of a vertex.")
        print("Press 8 to print the outbound neighbours of a vertex.")
        print("Press 9 to print the inbound neighbours of a vertex.")

    @staticmethod
    def print_edge_menu():
        pass

    def vertex_menu(self):
        commands = {"1": self.add_vertex,
                    "2": self.remove_vertex,
                    "3": self.check_if_vertex_exists,
                    "4": self.count_vertices,
                    "5": self.print_vertices,
                    "6": self.outdegree,
                    "7": self.indegree,
                    "8": self.outbound_neighbours,
                    "9": self.inbound_neighbours}

        self.print_vertex_menu()
        option = input("> ")

        if option in commands:
            commands[option]()
        else:
            raise Exception("Invalid input.")

    def add_vertex(self):
        vertex = int(input("vertex = "))
        self.__graph.add_vertex(vertex)

    def remove_vertex(self):
        vertex = int(input("vertex = "))
        self.__graph.remove_vertex(vertex)

    def check_if_vertex_exists(self):
        vertex = int(input("vertex = "))
        if self.__graph.is_vertex(vertex):
            print(f"The vertex {vertex} is a part of the graph.")
        else:
            print(f"The vertex {vertex} is not a part of the graph.")

    def count_vertices(self):
        print(f"The graph has {self.__graph.count_vertices()} vertices.")

    def print_vertices(self):
        for vertex in self.__graph.vertices_iterator():
            print(vertex, end = " ")

    def outdegree(self):
        vertex = int(input("vertex = "))
        print(f"The vertex {vertex} has an outdegree of {self.__graph.count_out_deg(vertex)}")

    def indegree(self):
        vertex = int(input("vertex = "))
        print(f"The vertex {vertex} has an indegree of {self.__graph.count_in_deg(vertex)}")

    def outbound_neighbours(self):
        vertex = int(input("vertex = "))
        for neighbour in self.__graph.outbound_neighbours_iterator(vertex):
            print(neighbour, end = " ")

    def inbound_neighbours(self):
        vertex = int(input("vertex = "))
        for neighbour in self.__graph.inbound_neighbours_iterator(vertex):
            print(neighbour, end = " ")

    def run(self):
        commands = {"1": self.vertex_menu,
                    "2": "",
                    "3": self.generate_graph,
                    "4": self.import_graph,
                    "5": self.export_graph,
                    "6": self.print_graph}

        while True:
            self.print_main_menu()
            option = input("> ")

            try:
                if option in commands:
                    commands[option]()
                elif option == "exit":
                    exit(0)
                else:
                    raise Exception("Invalid option.")
            except Exception as exception:
                print(str(exception))

    def import_graph(self):
        self.__graph.empty()
        path = input("path = ")
        self.__graph = import_graph(path)

    def export_graph(self):
        path = input("path = ")
        export_graph(self.__graph, path)

    def generate_graph(self):
        self.__graph.empty()
        vertices = int(input("vertices = "))
        edges = int(input("edges = "))
        self.__graph = generate_random_graph(vertices, edges)

    def print_graph(self):
        print(self.__graph)


if __name__ == "__main__":
    ui = UI(Graph())
    ui.run()
