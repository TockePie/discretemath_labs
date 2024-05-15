import functions
import random
from tkinter import *


# Функції, які генерують множини
def universal_set():
    u.clear()  # Очищає універсальну множину та генерує нову на основі введення користувача
    global left_border
    global right_border
    try:
        left_border = int(left_universal_data.get())
        right_border = int(right_universal_data.get())
        if left_border <= 0 or right_border <= 0:
            raise ValueError("Введені числа повинні бути додатніми.")

        universal_range = range(left_border, right_border + 1, 1)
        for i in universal_range:
            u.add(i)
        print(u)
    except ValueError as e:
        print("Помилка:", e)


def gen_set_A():
    a.clear()  # Очищає множину A та генерує нову заданого розміру
    try:
        print("Генерується множина A")
        power = int(set_a_data.get())
        if power <= 0:
            raise ValueError("Розмір множини повинен бути додатнім числом.")

        while len(a) != power:
            number = random.randint(left_border, right_border)
            if number not in a:
                a.add(number)
        print(a)
    except ValueError as e:
        print("Помилка:", e)


# Інші подібні функції для генерації множин B та C визначаються аналогічно
def gen_set_B():
    b.clear()
    try:
        print("Генерується множина B")
        power = int(set_b_data.get())
        if power <= 0:
            raise ValueError("Розмір множини повинен бути додатнім числом.")

        while len(b) != power:
            number = random.randint(left_border, right_border)
            if number not in b:
                b.add(number)
        print(b)
    except ValueError as e:
        print("Помилка:", e)


def gen_set_C():
    c.clear()
    try:
        print("Генерується множина C")
        power = int(set_c_data.get())
        if power <= 0:
            raise ValueError("Розмір множини повинен бути додатнім числом.")

        while len(c) != power:
            number = random.randint(left_border, right_border)
            if number not in c:
                c.add(number)
        print(c)
    except ValueError as e:
        print("Помилка:", e)


# Функції, які дають можливість ручного вводу
def manual_input_set_a():
    a.clear()  # Ручне введення множини A
    try:
        a_pool = manual_data_set_a.get().split(",")
        for i in a_pool:
            num = int(i)
            if num <= 0:
                raise ValueError("Елементи множини повинні бути додатніми числами.")
            a.add(num)
        print("A: ", a)
    except ValueError as e:
        print("Помилка:", e)


# Інші подібні функції для ручного введення множин B та C визначаються аналогічно
def manual_input_set_b():
    b.clear()
    try:
        b_pool = manual_data_set_b.get().split(",")
        for i in b_pool:
            num = int(i)
            if num <= 0:
                raise ValueError("Елементи множини повинні бути додатніми числами.")
            b.add(num)
        print("B: ", b)
    except ValueError as e:
        print("Помилка:", e)


def manual_input_set_c():
    c.clear()
    try:
        c_pool = manual_data_set_c.get().split(",")
        for i in c_pool:
            num = int(i)
            if num <= 0:
                raise ValueError("Елементи множини повинні бути додатніми числами.")
            c.add(num)
        print("C: ", c)
    except ValueError as e:
        print("Помилка:", e)


# Вікно 2
def second_window():
    def save_txt_file():
        f = open(r"D.txt", "w")
        f.write(str(step_eighth_of_calculation))
        f.close()

    # Включає кроки для обчислення множини D за допомогою визначених функцій
    def step1():
        Label(root2, text=f"¬A ∩ B: {step_first_of_calculation}", font='Arial 12').place(x=10, y=60+10)

    def step2():
        Label(root2, text=f"¬B ∩ ¬A: {step_second_of_calculation}", font='Arial 12').place(x=10, y=80+10)

    def step3():
        Label(root2, text=f"¬A ∪ B: {step_third_of_calculation}", font='Arial 12').place(x=10, y=100+10)

    def step4():
        Label(root2, text=f"¬(¬A ∩ B): {step_fourth_of_calculation}", font='Arial 12').place(x=10, y=120+10)

    def step5():
        Label(root2, text=f"¬(¬B ∩ ¬A): {step_fifth_of_calculation}", font='Arial 12').place(x=10, y=140+10)

    def step6():
        Label(root2, text=f"С ∪ ¬(¬A ∩ B): {step_sixth_of_calculation}", font='Arial 12').place(x=10, y=160+10)

    def step7():
        Label(root2, text=f"С ∪ ¬(¬A ∩ B) ∩ ¬(¬B ∩ ¬A): {step_seventh_of_calculation}",
              font='Arial 12').place(x=10, y=180+10)

    def step8():
        Label(root2, text=f"С ∪ ¬(¬A ∩ B) ∩ ¬(¬B ∩ ¬A) ∩ (¬A ∪ B): {step_eighth_of_calculation}",
              font='Arial 12').place(x=10, y=200+10)
        Label(root2, text=f'Результат D: {step_eighth_of_calculation}', font='Arial 12').place(x=500, y=320)

    step_first_of_calculation = functions.step1(a, b, u)
    step_second_of_calculation = functions.step2(a, b, u)
    step_third_of_calculation = functions.step3(a, b, u)
    step_fourth_of_calculation = functions.step4(step_first_of_calculation, u)
    step_fifth_of_calculation = functions.step5(step_second_of_calculation, u)
    step_sixth_of_calculation = functions.step6(c, step_fourth_of_calculation)
    step_seventh_of_calculation = functions.step7(step_sixth_of_calculation, step_fifth_of_calculation)
    step_eighth_of_calculation = functions.step8(step_seventh_of_calculation, step_third_of_calculation)

    # Відображає результати в вікні GUI
    root2 = Tk()
    root2.title("Вікно 2")
    root2.title("Вікно 2")
    root2.geometry("900x400")
    Label(root2, text=f'A: {a}  ¬A: {u - a}', font='Arial 12').place(x=0)
    Label(root2, text=f'B: {b}  ¬B: {u - b}', font='Arial 12').place(x=0, y=20)
    Label(root2, text=f'C: {c}', font='Arial 12').place(x=0, y=40)
    Button(root2, width=8, text="Крок 1", font="Arial 10", command=step1).place(x=0+30, y=320)
    Button(root2, width=8, text="Крок 2", font="Arial 10", command=step2).place(x=80+30, y=320)
    Button(root2, width=8, text="Крок 3", font="Arial 10", command=step3).place(x=160+30, y=320)
    Button(root2, width=8, text="Крок 4", font="Arial 10", command=step4).place(x=240+30, y=320)
    Button(root2, width=8, text="Крок 5", font="Arial 10", command=step5).place(x=0+30, y=350)
    Button(root2, width=8, text="Крок 6", font="Arial 10", command=step6).place(x=80+30, y=350)
    Button(root2, width=8, text="Крок 7", font="Arial 10", command=step7).place(x=160+30, y=350)
    Button(root2, width=8, text="Крок 8", font="Arial 10", command=step8).place(x=240+30, y=350)
    Button(root2, width=24, text="Завантажити D у файл на ПК", font="Arial 10",
           command=save_txt_file).place(x=500, y=350)


# Вікно 3
# Інші функції вікон (third_window, fourth_window, fifth_window) визначаються аналогічно
def third_window():
    step_first_of_calculation = functions.first_short_step(a, c)
    step_second_of_calculation = functions.second_short_step(step_first_of_calculation, b)

    def save_simplified_txt_file():
        f = open(r"D_simplified.txt", "w")
        f.write(str(step_second_of_calculation))
        f.close()

    def step1():
        Label(root3, text=f"C ∪ A: {step_first_of_calculation}", font='Arial 12').place(x=10, y=60+10)

    def step2():
        Label(root3, text=f"C ∪ A ∩ B: {step_second_of_calculation}", font='Arial 12').place(x=10, y=80+10)
        Label(root3, text=f'Результат D: {step_second_of_calculation}', font='Arial 12').place(x=200, y=180)

    root3 = Tk()
    root3.title("Вікно 3")
    root3.geometry("900x300")
    Label(root3, text=f'A: {a}', font='Arial 12').place(x=0)
    Label(root3, text=f'B: {b}', font='Arial 12').place(x=0, y=20)
    Label(root3, text=f'C: {c}', font='Arial 12').place(x=0, y=40)
    Button(root3, width=8, text="Крок 1", font="Arial 10", command=step1).place(x=0 + 30, y=220)
    Button(root3, width=8, text="Крок 2", font="Arial 10", command=step2).place(x=80 + 30, y=220)
    Button(root3, width=24, text="Завантажити D у файл на ПК", font="Arial 10",
           command=save_simplified_txt_file).place(x=200, y=220)


# Вікно 4
def fourth_window():
    step_result = functions.custom_calc_union(u - a, c)

    def saver3():
        f = open(r"customZ.txt", "w")
        f.write(str(step_result))
        f.close()

    def step():
        Label(root4, text=f'X ∪ Y: {step_result}', font='Arial 12').place(x=0, y=60)
        Label(root4, text=f'Результат Z: {step_result}', font='Arial 12').place(x=20, y=120)

    root4 = Tk()
    root4.title("Вікно 4")
    root4.geometry("900x300")
    Label(root4, text=f'X: {c}', font='Arial 12').place(x=0)
    Label(root4, text=f'Y: {u - a}', font='Arial 12').place(x=0, y=20)
    Button(root4, width=12, text="Розрахувати", font="Arial 10", command=step).place(x=0 + 30, y=220)
    Button(root4, width=24, text="Завантажити Z у файл на ПК", font="Arial 10", command=saver3).place(x=120 + 30, y=220)


# Вікно 5
def fifth_window():
    def data_read():
        usual_d_file = open(r"D.txt", "r")
        global data_usual_d_file
        data_usual_d_file = usual_d_file.read()
        usual_d_file.close()
        Label(root5, text=f'D: {data_usual_d_file}', font='Arial 12').place(x=10)
        
        simple_d_file = open(r"D_simplified.txt", "r")
        global data_simple_d_file
        data_simple_d_file = simple_d_file.read()
        simple_d_file.close()
        Label(root5, text=f'Спрощене D: {data_simple_d_file}', font='Arial 12').place(x=10, y=20)
        
        z1 = open(r"customZ.txt", "r")
        global z1_data
        z1_data = z1.read()
        z1.close()
        Label(root5, text=f'З використанням функції, яку я сам написав для Z: ', font='Arial 12').place(x=10, y=40)
        Label(root5, text=f'{z1_data}', font='Arial 12').place(x=10, y=60)

    z2_data = str(functions.calc_union(u - a, c))

    def step():
        Label(root5, text=f'Z обчислене функціями Python: ', font='Arial 12').place(x=10, y=80)
        Label(root5, text=f'{z2_data}', font='Arial 12').place(x=10, y=100)

    def compare_d():
        if data_usual_d_file == data_simple_d_file:
            Label(root5, text='Результати D є однаковими', font='Arial 12').place(x=500)
        else:
            Label(root5, text='Результати D є різними', font='Arial 12').place(x=500)

    def compare_z():
        if z1_data == z2_data:
            Label(root5, text='Результати Z є однаковими', font='Arial 12').place(x=500, y=20)
        else:
            Label(root5, text='Результати Z є різними', font='Arial 12').place(x=500, y=20)

    root5 = Tk()
    root5.title("Вікно 5")
    root5.geometry("900x300")
    Button(root5, width=18, text="Зчитати результати", font="Arial 10", command=data_read).place(x=15, y=200)
    Button(root5, width=34, text="Обчислити Z за допомогою функцій Python",
           font="Arial 10", command=step).place(x=15, y=230)
    Button(root5, width=12, text="Порівняти D", font="Arial 10", command=compare_d).place(x=15, y=260)
    Button(root5, width=12, text="Порівняти Z", font="Arial 10", command=compare_z).place(x=125, y=260)


u = set()
a = set()
b = set()
c = set()

# Інформація про мене
academic_group = 32
number_of_list = 16
variant = (number_of_list + academic_group % 60) % 30 + 1

# Вікно 1
root = Tk()
root.title("Вікно 1")
root.geometry("700x500")

Label(root, text='Крадожон Максим Романович', font='Arial 14').place(x=50)
Label(root, text=f'Група {academic_group}', font='Arial 12').place(x=400, y=5)
Label(root, text=f'Номер в списку: {number_of_list}', font='Arial 12').place(x=500, y=5)
Label(root, text=f'Варіант завдання: {variant}', font='Arial 12').place(x=420, y=25)

Label(root, text='Задайте границі універсальної множини:', font='Arial 12').place(x=5, y=70)  # Універсальна множина
Label(root, text='(', font='Arial 12').place(x=300, y=70)
left_universal_data = Entry(root, width=3, font="Arial 12")
left_universal_data.place(x=309, y=70)
Label(root, text=',', font='Arial 12').place(x=350, y=70)
right_universal_data = Entry(root, width=3, font="Arial 12")
right_universal_data.place(x=365, y=70)
Label(root, text=')', font='Arial 12').place(x=395, y=70)
Button(root, width=24, text="Задати універсальну множину", font="Arial 10", command=universal_set).place(x=450, y=65)

Label(root, text='Введіть потужність множин:', font='Arial 12').place(x=5, y=100)
Label(root, text='A:', font='Arial 12').place(x=10+140, y=140)  # Множина А
set_a_data = Entry(root, width=6, font="Arial 12")
set_a_data.place(x=30+140, y=140)
Button(root, width=11, text="Згенерувати А", font="Arial 10", command=gen_set_A).place(x=10+140, y=180)

Label(root, text='B:', font='Arial 12').place(x=140+140, y=140)  # Множина В
set_b_data = Entry(root, width=6, font="Arial 12")
set_b_data.place(x=160+140, y=140)
Button(root, width=11, text="Згенерувати B", font="Arial 10", command=gen_set_B).place(x=140+140, y=180)

Label(root, text='C:', font='Arial 12').place(x=280+140, y=140)  # Множина С
set_c_data = Entry(root, width=6, font="Arial 12")
set_c_data.place(x=300+140, y=140)
Button(root, width=11, text="Згенерувати C", font="Arial 10", command=gen_set_C).place(x=280+140, y=180)

Label(root, text='Ручний ввід А:', font='Arial 12').place(x=10+141, y=260)  # Ручний ввід А
manual_data_set_a = Entry(root, width=12, font="Arial 12")
manual_data_set_a.place(x=2+141, y=280)
Button(root, width=8, text="Задати А", font="Arial 10", command=manual_input_set_a).place(x=0+141, y=310)

Label(root, text='Ручний ввід B:', font='Arial 12').place(x=140+141, y=260)  # Ручний ввід В
manual_data_set_b = Entry(root, width=12, font="Arial 12")
manual_data_set_b.place(x=140+141, y=280)
Button(root, width=8, text="Задати B", font="Arial 10", command=manual_input_set_b).place(x=140+141, y=310)

Label(root, text='Ручний ввід C:', font='Arial 12').place(x=280+141, y=260)  # Ручний ввід С
manual_data_set_c = Entry(root, width=12, font="Arial 12")
manual_data_set_c.place(x=280+141, y=280)
Button(root, width=8, text="Задати C", font="Arial 10", command=manual_input_set_c).place(x=280+141, y=310)

Button(root, width=8, text="Вікно 2", font="Arial 10", command=second_window).place(x=200-50, y=450)
Button(root, width=8, text="Вікно 3", font="Arial 10", command=third_window).place(x=300-50, y=450)
Button(root, width=8, text="Вікно 4", font="Arial 10", command=fourth_window).place(x=400-50, y=450)
Button(root, width=8, text="Вікно 5", font="Arial 10", command=fifth_window).place(x=500-50, y=450)
root.mainloop()
