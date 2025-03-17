#🔹 Задание 1: Обработать деление на ноль
#🔹 Напиши функцию, которая делит два числа и обрабатывает ZeroDivisionError.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль невозможно."
print(safe_divide(10, 0))
