def foo ():
    width = int (input ("Введите ширину: "))
    height = int (input ("Введите высоту: "))
    s = input ("Из чего состоит рамка: ")

    if (width < height): #Если ширина меньше высоты
        j=1
        i=0
        for i in range(0, width-1):
            print(s, end='')

        while (i < height):
            while (j < width):
                print (s, end=" "*(width-2))
                print (s)
                j+=1
            i+=1

        for i in range(0, width-1):
            print(s, end='')
    
    if (width > height): #Если высота меньше ширины
        j=0
        i=1
        for i in range(0, width-1):
            print(s, end='')

        while (i < width):
            while (j < height):
                print (s, end=" "*(width-2))
                print (s)
                j+=1
            i+=1

        for i in range(0, width-1):
            print(s, end='')

    return s    
print (foo())
