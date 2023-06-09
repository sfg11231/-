def last_two_digits(n):
    # проверка, что число больше или равно 10^4
    if n < 10000:
        return "Число должно быть пятизначным!"

    # вычисление последней и предпоследней цифр
    last_digit = n % 10
    second_last_digit = (n // 10) % 10

    # возврат результатов
    return second_last_digit, last_digit

# пример использования
n = int(input("Введите пятизначное число: "))
digits = last_two_digits(n)

if isinstance(digits, str):
    print(digits)
else:
    print("Предпоследняя цифра:", digits[0])
    print("Последняя цифра:", digits[1])