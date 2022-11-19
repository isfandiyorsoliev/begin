# def begin_1(a):
#     p = 4 * a
#     print(p)
# begin_1(int(input("Введите число:")))

# def begin_2(a):
#     S = a**2
#     print(S)
# begin_2(int(input("Введите число:")))

# def begin_3(a, b):
#     S = a * b
#     P = 2 * (a + b)
#     print("Площадь = ",S)
#     print("Периметр = ", P)
# begin_3(int(input("Введите число:")), int(input("Введите число:")))

# def begin_4(d):
#     p = 3.14
#     L = p * d
#     print(L)
# begin_4(int(input("Введите число:")))

# def begin_5(a):
#     V = a**3
#     S = 6 * a**2
#     print("Объем = " + str(V))
#     print("Площадь поверхности = " + str(S))
# begin_5(int(input("Введите число:")))

# def begin_6(a, b, c):
#     V = a * b * c
#     S = 2 * (a*b + b*c + a*c)
#     print("Объем = " + str(V))
#     print("Площадь поверхности = " + str(S))
# begin_6(int(input("Введите число:")), int(input("Введите число:")), int(input("Введите число:")))

# def begin_7(R):
#     p = 3.14
#     L = 2 * p * R
#     S = p * R**2
#     print("Длина окружности = " + str(L))
#     print("Площадь круга = " + str(S))
# begin_7(int(input("Введите число:")))

# def begin_8(a, b):
#     S = (a + b)/2
#     print("Среднее арифмитическое = " + str(S))
# begin_8(int(input("Введите число:")), int(input("Введите число:")))
"""
import math
def begin_9(a, b):
    if a and b > 0:
        S = math.sqrt(a * b)
        print("Корень = " + str(S))
    else:
        print("Введите неотрицвтельные числа")
begin_9(float(input("Введите число:")), float(input("Введите число:")))
"""

"""
def begin_10(a, b):
    if a and b > 0:
        print("Сумму = " + str(a**2 + b **2))
        print("Разность = " + str(a**2 - b **2))
        print("Произведение = " + str(a**2 * b **2))
        print("Частное = " + str(a**2 / b **2))
    else:
        print("Введите число больше нуля")
begin_10(float(input("Введите число:")), float(input("Введите число:")))
"""
"""
def begin_11(a, b):
    if a or b > 0:
        print("Сумму = " + str(abs(a) + abs(b)))
        print("Разность = " + str(abs(a) - abs(b)))
        print("Произведение = " + str(abs(a) * abs(b)))
        print("Частное = " + str(abs(a) / abs(b)))
    else:
        print("Введите число больше нуля")
begin_11(float(input("Введите число:")), float(input("Введите число:")))
"""

# def begin_12(a, b):
#     c = math.sqrt(a**2 + b**2)
#     P = a + b + c
#     print("Гипотенузу = " + str(c))
#     print("Периметр = " + str(P))
# begin_12(int(input("Введите число:")), int(input("Введите число:")))

# def begin_13(R1, R2):
#     if R1 > R2:
#         p = 3.14
#         S1 = p * R1**2
#         S2 = p * R2**2
#         S3 = S1 - S2
#         print("Площадь круга 1: ", S1)
#         print("Площадь круга 2: ", S2)
#         print("Площадь кольца: ", S3)
#     else:
#         print("Ведите число которий R1>R2 (Радиус 1 больше Радиус 2)")
# begin_13(int(input("Радиус 1: ")), int(input("Радиус 2: ")))

# def begin_14(L):
#     pi = 3.14
#     R = L / 2 / pi
#     S = pi * R**2
#     print("Радиус окружности: ", R)
#     print("Площадь круга: ", S)
# begin_14(int(input("Длина окружности: ")))

# import math
# def begin_15(S):
#     pi = 3.14
#     R = math.sqrt(S / pi)
#     L = 2 * pi * R
#     D = 2 * R
#     print("Радиус окружности: ", R)
#     print("Длина окружности: ", L)
#     print("Диаметр окружности: ", D)
# begin_15(int(input("Площадь круга: ")))


# def begin33(X, A, Y):
#     price = A / X
#     cost_Y = price * Y
#     print(X, "kg = ", A, " rubles")
#     print("1 kg = ", price, " rubles")
#     print(Y, "kg = ", cost_Y, " rubles")
#
# begin33(5,5,7)

# def begin34(X, A, Y, B):
#     price_choko = X / A
#     price_iris = Y / B
#     price_raz = price_choko / price_iris
#     print("1 kg chokolad =", price_choko, "rubles")
#     print("1 kg irisk =", price_iris, "rubles")
#     print("Raznisa", price_raz, "rubles")
#
# begin34(5,5,7,5)

# def begin35(V, U, T1, T2):
#     if U < V:
#         Distance_ozera = V * T1
#         Distance_reca = (V - U) * T2
#         print("Скорость лодки в стоячей воде", V)
#         print("Скорость течения реки:", U)
#         print("Скорость в реке (вверх по течению):", V-U)
#         print("Время движения лодки по озеру", T1)
#         print("Время движения лодки по реке (против течения) ", T2)
#         print("Путь в озере:", Distance_ozera)
#         print("Путь в реке:", Distance_reca)
#     else:
#         print("(U < V)")
# begin35(15,18,8,6)

# def begin36(v1, v2, S, t):
#     total_speed = v1 + v2
#     x = t * (v1 + v2)+ S
#     print("1-я скорость автомобиля:", v1)
#     print("Вторая скорость автомобиля:", v2)
#     print("Время:", t)
#     print("Общая скорость:", total_speed)
#     print("Начальное расстояние между транспортными средствами:", S)
#     print("Конечное расстояние между транспортными средствами:", x)
# begin36(15, 20, 10, 5)
