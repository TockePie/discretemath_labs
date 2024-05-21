import math, networkx, tkinter, tkinter.filedialog, matplotlib.pyplot, matplotlib.backends.backend_tkagg


class GraphApp:
    def __init__(self):
        self.array, self.empty, self.copy_array, self.edges, self.list_of_colors, self.color_of_edge, self.root, self.colored_graph, self.colored_graph_start, self.edges, self.sum, self.size, self.seed = [], [], [], [], ['pink', 'darkorange', 'darkviolet', 'chartreuse', 'cyan', 'crimson', 'brown', 'blueviolet', 'pink'], [], tkinter.Tk(), [], [], {}, 0, 0, 0
        self.root.title("Window 1")
        self.root.geometry("1400x700")
        self.root.configure(bg='white')
        self.root.resizable(False, False)
        widget_data = [{"method": "button", "text": "Побудувати з поля", "width": 20, "height": 2, "command": self.fild_reader, "x": 20, "y": 370}, {"method": "button", "text": "Побудувати з файлу", "width": 20, "height": 2, "command": self.read_file, "x": 238, "y": 370}, {"method": "label", "text": f"Крадожон Максим Романович \nІО-32 \nНомер у списку групи: 16 Варіант: 1", "x": 10, "y": 450}, {"method": "label", "text": "Суміжність", "x": 850, "y": 0}, {"method": "label", "text": "Задайте граф матрицею суміжності", "x": 60, "y": 0}]
        [getattr(self, f'create_{data["method"]}')(*[data[key] for key in ('text', 'width', 'height', 'command', 'x', 'y') if key in data]) for data in widget_data]
        self.labelsym, self.labelinc, self.labeldict = self.create_label("", 750, 30, font=("Garamond", 15)), self.create_label("", 720, 30), self.create_label("", 1220, 30)
        self.text = tkinter.Text(width=45, height=15, bg="white", fg='black', wrap=tkinter.WORD, font=("Garamond", 15))
        self.text.place(x=20, y=30)

    def run(self): self.root.mainloop()

    def create_button(self, text, width, height, command, x, y):
        button = tkinter.Button(self.root, text=text, width=width, height=height, command=command, font=("Inter", 12))
        return button.place(x=x, y=y)

    def create_label(self, text, x, y, font=("Inter", 15)):
        label = tkinter.Label(self.root, text=text, justify=tkinter.LEFT, font=font, background="white")
        label.place(x=x, y=y)
        return label

    def fild_reader(self):
        self.seed += 1
        self.clear()
        s: str = self.text.get('1.0', tkinter.END)
        self.text_converter(s)
        self.initial_work()

    def read_file(self):
        with open(tkinter.filedialog.askopenfilename(), 'r', encoding='cp1251') as file: s = file.read()
        self.seed += 1
        self.clear()
        self.text_converter(s)
        self.initial_work()

    def text_converter(self, s: str):
        s = s.replace(" ", "").replace("\n", "")
        if s:
            split = s.split(",")
            length = int(math.sqrt(len(split)))
            self.array = [[int(split[length * i + j]) for j in range(length)] for i in range(length)]

    def initial_work(self):
        self.size, self.copy_array, self.sum = len(self.array), [list(row) for row in self.array], sum(self.array[i][j] for i in range(self.size) for j in range(i, self.size) if self.array[i][j] > 0)
        self.directed(self.sum, self.size)
        s = "    " + " ".join(f"_v{i+1}" for i in range(self.size)) + "\n"
        s += "\n".join(f"v{i+1}|{'     '.join(str(self.array[i][j]) if i != 9 else ''.join(str(self.array[i][j])) for j in range(self.size))}" for i in range(self.size))
        self.labelsym.configure(text=s)
        self.color_of_edge, self.colored_graph, self.colored_graph_start = [0 for i in range(len(self.array))], [0 for i in range(len(self.array))], ['springgreen' for i in range(len(self.array))]
        for i in range(len(self.array)):
            self.color_of_edge[i] = self.color(i)
            self.colored_graph[i] = self.list_of_colors[self.color_of_edge[i]]
        self.make_canvas(self.build_adjacent(), 450, 270, self.colored_graph_start)
        self.make_canvas(self.build_adjacent(), 900, 270, self.colored_graph)
        self.create_label("Початковий граф", 550, 290)
        self.create_label("Розфарбований граф", 1000, 290)

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
    
    def color(self, i):
        used_colors = {self.color_of_edge[j] for j in range(i) if self.array[j][i] > 0}
        current_color = 1
        while current_color in used_colors: current_color += 1
        return current_color

    def make_canvas(self, G: networkx.Graph, x: int, y: int, c: list):
        size = int(math.sqrt(len(G.nodes)) ** 1.15)
        f = matplotlib.pyplot.Figure(figsize=(size, size), dpi=400 / size)
        networkx.draw(G, ax=f.add_subplot(111), with_labels=True, node_color=c, arrowstyle='-', pos=networkx.spring_layout(G, seed=self.seed))
        matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(f, master=self.root).get_tk_widget().place(x=x, y=y)

    def clear(self):
        for attr in ['array', 'empty', 'copy_array', 'edges']: getattr(self, attr).clear()
        self.sum = self.size = 0


GraphApp().run()
