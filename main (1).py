exam=int(input('Введите оценку за экзамен - '))
projects=int(input('Введите количество выполненных проектов - '))
if exam>=90 and projects>=10:
        print(100)
elif exam>=75 and projects>=5:
    print(90)
elif exam>=50 and projects>=2:
    print(75)
else:
    print(0)