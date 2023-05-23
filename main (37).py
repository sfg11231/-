def zagadki():
    global k
    l=0
    if k>3:
        u=1+l
        l += 1
        print(l)
        answer=input("Выше написано кол-во общих попыток \n Попрробуйте решить задачи ещё раз ")
        if k==3:
                print("Ваши общие попытки закончились")
                quit()
        
    a=print("загадка №1\n Каких камней не бывает в речке? \n у вас есть пять попыток")
    answer=input("введите ответ ")
    answer=answer.lower()
    n=0
    while n<3:
        if answer=="сухих":
            print("правильный ответ")
            break
        else:
            print("ответ неверный попробуйте еще раз")
            k=1+n
            n += 1
            print(k)
            answer=input("Выше написано кол-во попыток \n введите ответ:")
            if k==3:
                print("Ваши попытки закончились")
                quit()
    
    b=print("загадка №2\n Завязать можно, а развязать нельзя. Что это? \n у вас есть пять попыток")
    answers=input("введите ответ ")
    answers=answers.lower()
    n=0
    while n<3:
        if answers=="разговор":
            print("правильный ответ")
            break
        else:
            print("ответ неверный попробуйте еще раз")
            k=1+n
            n += 1
            print(k)
            answers=input("Выше написано кол-во попыток \n введите ответ:")
            if k==3:
                print("Ваши попытки закончились")
                quit()
    

    
    c=print("загадка №3\n Что не вместится даже в самую большую кастрюлю? \n у вас есть пять попыток")
    answerk=input("введите ответ ")
    answerk=answerk.lower()
    n=0
    while n<3:
        if answerk=="ее крышка":
            print("правильный ответ")
            break
        else:
            print("ответ неверный попробуйте еще раз")
            k=1+n
            n += 1
            print(k)
            answerk=input("Выше написано кол-во попыток \n введите ответ:")
            if k==3:
                print("Ваши попытки закончились")
                quit()
    zagadki()