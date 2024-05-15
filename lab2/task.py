import data
import os
from tkinter import *
from data import *
from sencitive_data import *


def second_window():
    def set_adder():
        selected_listbox = women_listbox if set_num.get() == 1 else men_listbox
        selected_set = set_a if set_num.get() == 1 else set_b
        print(selected_listbox.get(ANCHOR))
        selected_set.add(selected_listbox.get(ANCHOR))

    def save_set_to_file(set_to_save, file_name):
        with open(file_name, "w") as f:
            f.write("\n".join(set_to_save))

    def read_set_from_file(set_to_update, file_name):
        with open(file_name, "r") as f:
            set_to_update.clear()
            temp = f.read().strip().split("\n")
            set_to_update.update(temp)

            print(temp)
            print(set_to_update)

    def clear_set_and_file(set_to_clear, file_name):
        set_to_clear.clear()
        os.remove(file_name)

    def create_listbox(x_pos, y_pos, items):
        listbox = Listbox(root2)
        listbox.place(x=x_pos, y=y_pos)
        listbox.insert(END, *items)
        return listbox

    root2 = Tk()
    root2.title("Вікно 2")
    root2.geometry("500x350")

    set_num = IntVar(root2)
    women_listbox = create_listbox(50, 10, items=womenlist)
    men_listbox = create_listbox(300, 10, items=menlist)

    Radiobutton(root2, text="Множина А", variable=set_num, value=1).place(x=60, y=180)
    Radiobutton(root2, text="Множина B", variable=set_num, value=2).place(x=320, y=180)
    Button(root2, width=8, text="Додати", font="Arial 10", command=set_adder).place(x=200, y=120)
    Button(root2, width=15, text="Зберегти А у файл", font="Arial 10",
           command=lambda: save_set_to_file(set_a, "Adata.txt")).place(x=0 + 50, y=240)
    Button(root2, width=15, text="Зберегти В у файл", font="Arial 10",
           command=lambda: save_set_to_file(set_b, "Bdata.txt")).place(x=0 + 50, y=270)
    Button(root2, width=10, text="Зчитати А", font="Arial 10",
           command=lambda: read_set_from_file(set_a, "Adata.txt")).place(x=140 + 50, y=240)
    Button(root2, width=10, text="Зчитати В", font="Arial 10",
           command=lambda: read_set_from_file(set_b, "Bdata.txt")).place(x=140 + 50, y=270)
    Button(root2, width=10, text="Очистити А", font="Arial 10",
           command=lambda: clear_set_and_file(set_a, "Adata.txt")).place(x=320, y=240)
    Button(root2, width=10, text="Очистити В", font="Arial 10",
           command=lambda: clear_set_and_file(set_b, "Bdata.txt")).place(x=320, y=270)


def third_window():
    def populate_listbox(listbox, some_set, x_position, y_position):
        listbox.place(x=x_position, y=y_position)
        for item in some_set:
            listbox.insert(END, item)

    def create_labels_and_ovals(title, names, x_offset, y_offset):
        Label(root3, text=title, font='Arial 12').place(x=400 + x_offset, y=y_offset)
        for i, name in enumerate(names):
            y_position = 40 + y_offset if y_offset in [150, 400] else 25 + y_offset
            oval_y = 25 + y_offset if y_offset in [150, 400] else 50 + y_offset
            Label(root3, text=name, font='Arial 10').place(x=401 + i * 100 + x_offset, y=y_position)
            canvas.create_oval(401 + i * 100 + x_offset, oval_y, 410 + i * 100 + x_offset, oval_y + 10, fill="black")

        for i in set_r:
            if i in coord_dict_for_set_r:
                canvas.create_line(coord_dict_for_set_r[i], arrow="last")
        for i in set_s:
            if i in coord_dict_for_set_s:
                canvas.create_line(coord_dict_for_set_s[i], arrow="last")

    def relations(letter, relate):
        for condition, elements in relate.items():
            if elements[0] in set_a and elements[1] in set_b:
                print("added element")
                letter.add(condition)

        print(letter)

    root3 = Tk()
    root3.title("Вікно 3")
    root3.geometry("1000x600")

    canvas = Canvas(root3, width=1000, height=500)
    canvas.place(x=0, y=0)

    relations(letter=set_s, relate=data.relationships_for_granddaughter)
    relations(letter=set_r, relate=data.relationships_for_wife)

    populate_listbox(Listbox(root3), set_a, 50, 100)
    populate_listbox(Listbox(root3), set_b, 200, 100)

    print("test1", set_r)
    print("test2", set_s)

    create_labels_and_ovals('A онука В', womenlist, 0, 0)
    create_labels_and_ovals('A дружина В', womenlist, 0, 250)
    create_labels_and_ovals(None, menlist, 0, 150)
    create_labels_and_ovals(None, menlist, 0, 400)


def fourth_window():
    def create_labels_and_ovals(title, x, y):
        Label(root4, text=title, font='Arial 12').place(x=x, y=y)
        for i, name in enumerate(womenlist):
            Label(root4, text=name, font='Arial 10').place(x=x + i * 100, y=y + 20)
            canvas.create_oval(x + 5 + i * 100, y + 45, x + 15 + i * 100, y + 55, fill="black")
        for i, name in enumerate(menlist):
            Label(root4, text=name, font='Arial 10').place(x=x + i * 100, y=y + 190)
            canvas.create_oval(x + 5 + i * 100, y + 175, x + 15 + i * 100, y + 185, fill="black")

    root4 = Tk()
    root4.title("Вікно 4")
    root4.geometry("1000x750")

    canvas = Canvas(root4, bg="white", width=1000, height=1000)
    canvas.place(x=0, y=0)

    set_dict = {
        "rs": (set_r.union(set_s), coord_dict1),
        "rs_intersect": (set_r.intersection(set_s), coord_dict3),
        "r_diff_s": (set_r.difference(set_s), coord_dict2),
        "u_diff_r": (set_u.difference(set_r), coord_dict4),
        "s": (set_s, coord_dict5)
    }

    for key, (s, coord_dict) in set_dict.items():
        for i in s:
            if i in coord_dict:
                if key == "s":
                    canvas.create_line(coord_dict[i], coord_dict[i], arrow="first", arrowshape=(8, 10, 3))
                else:
                    canvas.create_line(coord_dict[i], coord_dict[i], arrow="last", arrowshape=(8, 10, 3))

    create_labels_and_ovals('R ∪ S', 0, 0)
    create_labels_and_ovals('R ∩ S', 0, 250)
    create_labels_and_ovals('R\S', 500, 0)
    create_labels_and_ovals('U\R', 500, 250)
    create_labels_and_ovals('S^-1', 0, 500)


variant = (senc_data['number_in_list'] + senc_data['group'] % 60) % 30 + 1
set_a, set_b, set_s, set_r = set(), set(), set(), set()

root = Tk()
root.title("Вікно 1")
root.geometry("500x200")

Label(root, text=senc_data['name'], font='Arial 14').place(x=110, y=10)
Label(root, text=f"Група {senc_data['group']}", font='Arial 12').place(x=10, y=160)
Label(root, text=f"Номер в списку: {senc_data['number_in_list']}", font='Arial 12').place(x=85, y=160)
Label(root, text=f'Варіант завдання: {variant}', font='Arial 12').place(x=330, y=160)

Button(root, width=8, text="Вікно 2", font="Arial 10", command=second_window).place(x=125, y=110)
Button(root, width=8, text="Вікно 3", font="Arial 10", command=third_window).place(x=205, y=110)
Button(root, width=8, text="Вікно 4", font="Arial 10", command=fourth_window).place(x=285, y=110)

root.mainloop()
