import math
import networkx
import matplotlib.pyplot as plt

from tkinter import *
from matplotlib.backends.backend_tkagg import *
from sencitive_data import senc_data


class GraphApp:
    def __init__(self):
        self.array, self.empty, self.copy_array, self.edges, self.list_of_colors, self.color_of_edge, self.root, self.colored_graph, self.colored_graph_start, self.edges, self.sum, self.size, self.seed = [], [], [], [], ['pink', 'darkorange', 'darkviolet', 'chartreuse', 'cyan', 'crimson', 'brown', 'blueviolet', 'pink'], [], Tk(), [], [], {}, 0, 0, 0
        self.root.title("Window 1")
        self.root.geometry("1400x700")
        self.root.configure(bg='white')
        self.root.resizable(False, False)
        self.create_button("Побудувати з поля", 20, 2, self.read_fild, 20, 370)
        self.create_button("Побудувати з файлу", 20, 2, self.read_file, 238, 370)
        self.create_label(f"{senc_data['name']} \nІО-{senc_data['group']} \nНомер у списку групи: {senc_data['number_in_list']} Варіант: 1", 10, 450)
        self.create_label("Суміжність", 850, 0)
        self.create_label("Задайте граф матрицею суміжності", 60, 0)
        self.labelsym, self.labelinc, self.labeldict = self.create_label("", 750, 30), self.create_label("", 720, 30), self.create_label("", 1220, 30)
        self.text = Text(width=45, height=15, bg="white", fg='black', wrap=WORD, font=("Garamond", 15))
        self.text.place(x=20, y=30)

    def run(self): self.root.mainloop()

    def create_button(self, text, width, height, command, x, y):
        button = Button(self.root, text=text, width=width, height=height, command=command, font=("Garamond", 12))
        button.place(x=x, y=y)
        return button

    def create_label(self, text, x, y):
        label = Label(self.root, text=text, justify=LEFT, font=("Garamond", 15), background="white")
        label.place(x=x, y=y)
        return label

    def read_fild(self):
        self.seed += 1
        self.clear()
        s: str = self.text.get('1.0', END)
        self.convert_text(s)
        self.start_work()

    def read_file(self):
        try:
            with open("file1.txt", "r", encoding="cp1251") as file: s = file.read()
            self.seed += 1
            self.clear()
            self.convert_text(s)
            self.start_work()
        except FileNotFoundError: print("File not found.")

    def convert_text(self, s: str):
        s = s.replace(" ", "").replace("\n", "")
        if s:
            split = s.split(",")
            length = int(math.sqrt(len(split)))
            self.array = [[int(split[length * i + j]) for j in range(length)] for i in range(length)]

    def start_work(self):
        self.make_array()
        self.print_matrix()
        self.set_colors()
        self.make_canvas(self.build_adjacent(), 450, 270, self.colored_graph_start)
        self.make_canvas(self.build_adjacent(), 900, 270, self.colored_graph)
        self.create_label("Початковий граф", 550, 290)
        self.create_label("Розфарбований граф", 1000, 290)

    def make_array(self):
        self.size, self.copy_array, self.sum = len(self.array), [list(row) for row in self.array], sum(self.array[i][j] for i in range(self.size) for j in range(i, self.size) if self.array[i][j] > 0)
        self.directed(self.sum, self.size)

    def directed(self, weight: int, height: int):
        empty, a = [[0 for _ in range(weight)] for _ in range(height)], 0
        for i in range(height):
            for j in range(height):
                while self.copy_array[i][j] > 0 and a < weight:
                    if i != j:
                        empty[i][a] += 1
                        empty[j][a] -= 1
                    else: empty[i][a] += 2
                    a += 1
                    self.copy_array[i][j] -= 1

    def build_adjacent(self) -> networkx.Graph: return networkx.DiGraph([(i + 1, j + 1) for i in range(self.size) for j in range(i, self.size) if self.array[i][j] == 1])

    def set_colors(self):
        self.color_of_edge, self.colored_graph, self.colored_graph_start = [0 for i in range(len(self.array))], [0 for i in range(len(self.array))], ['springgreen' for i in range(len(self.array))]
        for i in range(len(self.array)):
            self.color_of_edge[i] = self.color(i)
            self.colored_graph[i] = self.list_of_colors[self.color_of_edge[i]]
    
    def color(self, i):
        w, current_color = {0}, 0
        w.update(self.color_of_edge[j] for j in range(i) if self.array[j][i] > 0)
        while True:
            current_color += 1
            if current_color not in w: break
        return current_color

    def make_canvas(self, G: networkx.Graph, x: int, y: int, c: list):
        size = int(math.sqrt(len(G.nodes)) ** 1.15)
        f = plt.Figure(figsize=(size, size), dpi=400 / size)
        a = f.add_subplot(111)
        networkx.draw(G, ax=a, with_labels=True, node_color=c, arrowstyle='-', pos=networkx.spring_layout(G, seed=self.seed))
        canvas = FigureCanvasTkAgg(f, master=self.root)
        canvas.get_tk_widget().place(x=x, y=y)

    def print_matrix(self):
        s = "    " + " ".join(f"_v{i+1}" for i in range(self.size)) + "\n"
        s += "\n".join(f"v{i+1}| {'     '.join(str(self.array[i][j]) for j in range(self.size))}" for i in range(self.size))
        self.labelsym.configure(text=s)

    def clear(self):
        for attr in ['array', 'empty', 'copy_array', 'edges']: getattr(self, attr).clear()
        self.sum = self.size = 0


app = GraphApp()
app.run()
