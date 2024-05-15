from tkinter import *
from sencitive_data import *

import networkx as nx
import matplotlib.pyplot as plt


class GraphSolver:
    def __init__(self):
        pass

    def topological_sort(self, graph):
        visited, sorted_vertices = set(), []
        def visit(vertex):
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in graph[vertex]:
                    visit(neighbor)
                sorted_vertices.append(vertex)
        for vertex in graph:
            visit(vertex)
        return sorted_vertices[::-1]

    def shortest_path(self, graph, weights, start, end):
        sorted_vertices = self.topological_sort(graph)
        distances = {vertex: float('inf') for vertex in graph}
        distances[start] = 0
        for vertex in sorted_vertices:
            for neighbor in graph[vertex]:
                new_distance = distances[vertex] + weights[vertex][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
        path = []
        current_vertex = end
        while current_vertex != start:
            path.append(current_vertex)
            current_vertex = min((distances[current_vertex] - weights[v][current_vertex], v) for v in graph if current_vertex in graph[v])[1]
        path.append(start)
        return distances[end], path[::-1]

    def visualize_graph(self, graph, weights, shortest_path_edges):
        G = nx.DiGraph()
        G.add_nodes_from(graph)
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                edge_weight = weights[node][neighbor]
                G.add_edge(node, neighbor, weight=edge_weight)
        pos = nx.spring_layout(G)
        edge_labels = {(u, v): weights[u][v] for u, v in G.edges()}
        nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue', font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_weight='bold')
        red_edges = [(shortest_path_edges[i], shortest_path_edges[i + 1]) for i in range(len(shortest_path_edges) - 1)]
        edge_colors = ["red" if edge in red_edges else "black" for edge in G.edges()]
        nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color=edge_colors, width=2.0)
        plt.show()

    def parse_input(self, graph_input, weights_input, start_vertex_input, end_vertex_input):
        graph = {}
        weights = {}
        for line in graph_input.split("\n"):
            if line.strip():
                vertex, neighbors = line.split(":")
                vertex = int(vertex.strip()) if vertex.strip() else None
                neighbors = list(map(int, neighbors.split(",")))
                if vertex is not None:
                    graph[vertex] = neighbors
        for line in weights_input.split("\n"):
            if line.strip():
                vertex, weight_list = line.split(":")
                vertex = int(vertex.strip())
                weight_list = weight_list.split(",")
                weights[vertex] = {graph[vertex][i]: int(weight_list[i].strip()) for i in range(len(graph[vertex]))}
        start_vertex = int(start_vertex_input)
        end_vertex = int(end_vertex_input)
        return graph, weights, start_vertex, end_vertex


class GraphSolverGUI:
    def __init__(self, root):
        self.root = root
        self.solver = GraphSolver()

        self.graph_label = self.create_and_place_widget(Label, 50, 10, text="Введіть граф (формат: вершина: сусіди через кому):")
        self.graph_text = self.create_and_place_widget(Text, 50, 30, height=10, width=40)

        self.weights_label = self.create_and_place_widget(Label, 400, 10, text="Введіть матрицю ваг (формат: вершина: ваги через кому):")
        self.weights_text = self.create_and_place_widget(Text, 400, 30, height=10, width=40)

        self.start_vertex_label = self.create_and_place_widget(Label, 50, 230, text="Початкова вершина:")
        self.start_vertex_entry = self.create_and_place_widget(Entry, 180, 231)

        self.end_vertex_label = self.create_and_place_widget(Label, 400, 230, text="Кінцева вершина:")
        self.end_vertex_entry = self.create_and_place_widget(Entry, 530, 231)

        self.submit_button = self.create_and_place_widget(Button, 300, 270, text="Знайти найкоротший шлях", command=self.on_submit)
        self.result_label = self.create_and_place_widget(Label, 50, 300, text="")

    def create_and_place_widget(self, widget_type, x, y, **kwargs):
        widget = widget_type(self.root, **kwargs)
        widget.place(x=x, y=y)
        return widget

    def on_submit(self):
        graph_input = self.graph_text.get("1.0", END)
        weights_input = self.weights_text.get("1.0", END)
        start_vertex_input = self.start_vertex_entry.get()
        end_vertex_input = self.end_vertex_entry.get()

        graph, weights, start_vertex, end_vertex = self.solver.parse_input(graph_input, weights_input, start_vertex_input, end_vertex_input)
        shortest_path_length, shortest_path_edges = self.solver.shortest_path(graph, weights, start_vertex, end_vertex)

        self.result_label.config(text=f"Найкоротший шлях між вершинами {start_vertex} та {end_vertex} має відстань {shortest_path_length} і проходить через вершини {shortest_path_edges}")
        self.solver.visualize_graph(graph, weights, shortest_path_edges)


root = Tk()
root.title("Пошук найкоротшого шляху")
root.geometry("780x420")

Label(root, text=senc_data['name'], font='Arial 14').place(x=250, y=310+20)
Label(root, text=f"Група {senc_data['group']}", font='Arial 12').place(x=10+100, y=350+20)
Label(root, text=f"Номер в списку: {senc_data['number_in_list']}", font='Arial 12').place(x=85+100, y=350+20)
Label(root, text=f'Варіант завдання: 7', font='Arial 12').place(x=330+100, y=350+20)

gui = GraphSolverGUI(root)
root.mainloop()
