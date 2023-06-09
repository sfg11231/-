def digit_sum_product(n):
    # инициализация переменных
    sum = 0
    product = 1

    # вычисление суммы и произведения цифр
    while n != 0:
        digit = n % 10
        sum += digit
        product *= digit
        n //= 10

    # возврат результатов
    return sum, product

# пример использования
n = int(input("Введите четырехзначное число: "))
sum, product = digit_sum_product(n)
print("Сумма цифр:", sum)
print("Произведение цифр:", product)