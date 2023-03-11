radius = int(input('Введите радиус круга')) 
kvadrat = int(input('Введите длинну стороны квадрата')) 
ploshad1 = 3.14 * radius * radius 
ploshad2 = kvadrat * kvadrat 
if ploshad1 > ploshad2: 
 print('площадь круга больше площади квадрата') 
else: 
 print('площадь круга меньше площади квадрата')