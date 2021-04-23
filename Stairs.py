def foo ():
    i = 1
    s = str (input ("В какую сторону бдует направлена лесенка: LU - сверху влево, RU - свверху вправо, LD - свнизу влево, RD - снизу вправо: "))
    n = int (input("Введите размер лесенки: "))
    f = input("Введите из чего состоит лесенка: ")
    c=n
    if (s == "LU"):
        while (i <= n):
            a = " " * c
            b = f * i
            print (a, b)
            i+=1
            c-=1

    if (s == "RU"):
        while(i <= n):
            b = f * i
            print (b)
            i+=1

    if (s == "LD"):
        while(i <= n):
            a= f*c
            b=" "*i
            print (b,a)
            i+=1
            c-=1

    if (s == "RD"):
        while(i <= n):
            a= f*c
            print (a)
            i+=1
            c-=1

    return (n,f)
print (foo())