def foo():
    n = list (map(int, input("Введите список чисел: ")))
    imin=n.index(min(n))
    imax=n.index(max(n))
    k=max(n)
    o=min(n)
    n.remove(o)
    n.remove(k)
    n.insert(imin, k)
    n.insert(imax, o)
    return n
print (foo())
