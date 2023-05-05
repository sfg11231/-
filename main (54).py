from random import random
n = round(random() *100)
i = 1
print("Компьютер загадал число от 1 до 100")
while i <= 100:
    u = int(input(str(i) + '-я попытка: '))
    if u>n:
        print('Много')
    elif u<n:
        print('Мало')
    else:
        print('Вы угадали с % d-й попытки')
        break
    i +=1
else:
    print('Вы исчерпали 10 попыток. Было загадано', n)