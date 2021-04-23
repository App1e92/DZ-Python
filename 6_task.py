def foo():
    n = list(map(int, input("Введите список чисел: ")))
    l=n[-1]
    for i in range (len(n)-1, 0, -1):
        n[i]=n[i-1]
    n[0]=l
    return n
print (foo())
