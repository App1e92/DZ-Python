def foo():
    n = int (input ("Введите количество минут: "))
    while (n > 1439):
       n=n-1439
    minute = n % 60
    hours = n // 60
    print(hours, ":" ,minute)
    return 
print (foo())
