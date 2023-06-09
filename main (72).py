def contains_digit(n):
   
    num_str = str(n)
    
   
    for digit in num_str:
        if digit == '2':
            return True
    
   
    return False

def get_number_from_input():
    while True:
        try:
            number = int(input("Введите целое число: "))
            return number
        except ValueError:
            print("Ошибка: некорректное значение. Попробуйте еще раз.")
number = get_number_from_input()

if contains_digit(number):
    print("Число", number, "содержит цифру 2.")
else:
    print("Число", number, "не содержит цифру 2.")