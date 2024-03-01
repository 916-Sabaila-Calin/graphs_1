from graph import *


class UI:
    def __init__(self, graph):
        self.__graph = graph

    def print_main_menu(self):
        print("")
        print("Press 1 to display the vertex operations.")
        print("Press 2 to display the edge operations.")
        print("Press 3 to generate a random graph.")
        print("Press 4 to import a graph from a text file.")
        print("Press 5 to export the graph to a text file.")
        print("Press 6 to print the graph.")
        print("Type \"exit\" to close the program.")

    def run(self):
        commands = {"1": "",
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
