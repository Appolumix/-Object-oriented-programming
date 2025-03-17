#🔹 Задание 5: Проверить тип переменной
#🔹 Напиши функцию, которая принимает только числа и выбрасывает TypeError, если передан текст.

def square(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Ошибка: аргумент должен быть числом!")
    return num ** 2

try:
    print(square("строка"))  # Ошибка TypeError
except TypeError as e:
    print(e)
