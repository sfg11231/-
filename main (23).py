a = int(input('Введите первое 4 значное число')) 
q = int(input('Введите второе 4 значное число')) 
if 9999 > a < 10000: 
 print('Число подходит') 
 b = a + q 
 c = a * q 
 print('Сумма', b, 'Произведение', c) 
else: 
 print('Некоректное число')