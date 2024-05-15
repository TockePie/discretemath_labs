# Обчислення другої логічної операції за допомогою вбудованих функцій Python
def calc_union(not_a, c):  # Знаходить об'єднання комплемента множини A та множини C
    return not_a | c


# Обчислення другої логічної операції власною функцією
def custom_calc_union(not_a, c):  # Знаходить об'єднання комплемента множини A та множини C власною функцією
    for i in c:
        if i not in not_a:
            not_a.add(i)
    return not_a


# Обчислення даного виразу
def step1(a, b, u):  # Обчислення першого кроку виразу: ¬A ∩ B
    not_a = u - a
    result_of_calc = not_a & b
    return result_of_calc


def step2(a, b, u):  # Обчислення другого кроку виразу: ¬B ∩ ¬A
    not_a = u - a
    not_b = u - b
    result_of_calc = not_a & not_b
    return result_of_calc


def step3(a, b, u):  # Обчислення третього кроку виразу: ¬A ∪ B
    not_a = u - a
    result_of_calc = calc_union(not_a, b)
    return result_of_calc


def step4(var, u):  # Обчислення четвертого кроку виразу: ¬(¬A ∩ B)
    result_of_calc = u - var
    return result_of_calc


def step5(var2, u):  # Обчислення п'ятого кроку виразу: ¬(¬B ∩ ¬A)
    result_of_calc = u - var2
    return result_of_calc


def step6(c, var4):  # Обчислення шостого кроку виразу: C ∪ ¬(¬A ∩ B)
    result_of_calc = calc_union(c, var4)
    return result_of_calc


def step7(var6, var5):  # Обчислення сьомого кроку виразу: C ∪ ¬(¬A ∩ B) ∩ ¬(¬B ∩ ¬A)
    result_of_calc = var6 & var5
    return result_of_calc


def step8(var7, var3):  # Обчислення восьмого кроку виразу: C ∪ ¬(¬A ∩ B) ∩ ¬(¬B ∩ ¬A) ∩ (¬A ∪ B)
    result_of_calc = var7 & var3
    return result_of_calc


# Обчислення спрощеного виразу
def first_short_step(a, c):  # Знаходить об'єднання множин C та A
    return calc_union(c, a)


def second_short_step(var, b):  # Обчислення спрощеного виразу: (C ∪ A) ∩ B
    return var & b
