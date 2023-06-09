def reverse_number(n):
    # переводим число в строку, затем разворачиваем ее и преобразуем обратно в целое число
    return int(str(n)[::-1])

def difference(n):
    # вычисляем числа с обратным порядком цифр
    reverse = reverse_number(n)
    # вычисляем разность между числами
    diff = abs(n - reverse)
    return diff

# пример использования
n = 537
diff = difference(n)
print("Разность между числом", n, "и числом с обратным порядком цифр равна", diff)