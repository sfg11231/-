def print_digits(n):
    digits = []

    # проверяем каждую цифру числа и добавляем ее в список
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n //= 10

    # переворачиваем список и выводим на экран
    digits.reverse()
    print("Цифры числа:", digits)

# вызываем функцию и передаем ей целое число
n = int(input("Введите целое число: "))
print_digits(n)