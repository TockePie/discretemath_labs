import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from itertools import combinations


def generate_combinations():
    text.delete('1.0', tk.END)
    text.insert(tk.END, '\n'.join([', '.join(c) for c in combinations(cities, int(k_entry.get()))]))
    text.configure(state='disabled')


def load_data():
    with open(filedialog.askopenfilename(), 'r', encoding='utf-8') as f:
        global cities
        cities = f.read().splitlines()


def update_cities(*args):
    global cities
    cities = cities_entry.get().split(', ')


root = ctk.CTk()
root.title("Комбінації міст")

ctk.CTkLabel(root, text="ІО-32 Крадожон Максим. Номер у списку 16, варіант: 19").grid(row=0, column=1, columnspan=3, padx=10, pady=10)

ctk.CTkLabel(root, text="Введіть міста або завантажте їх з файлу:").grid(row=1, column=1, padx=10, pady=10)
ctk.CTkLabel(root, text="Введіть кількість елементів у комбінації:").grid(row=2, column=1, padx=10, pady=10)

cities_entry = ctk.CTkEntry(root)
cities_entry.grid(row=1, column=2, pady=10)

cities_entry_var = tk.StringVar()
cities_entry_var.trace('w', update_cities)
cities_entry.configure(textvariable=cities_entry_var)

k_entry = ctk.CTkEntry(root)
k_entry.grid(row=2, column=2, pady=10)

ctk.CTkButton(root, text="Завантажити дані з файлу", command=load_data).grid(row=1, column=3, padx=10, pady=10)
ctk.CTkButton(root, text="Створення комбінацій", command=generate_combinations).grid(row=2, column=3, padx=5, pady=10)

text = ctk.CTkTextbox(root)
text.configure(width=600, height=500)
text.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

root.mainloop()
