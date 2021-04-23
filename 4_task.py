def foo(k):
    n = list(map(int, input("Введите число заканчивающееся нулём: ")))
    s=1
    o=0
    if (n[-1]!=0):
        n.append(0)
    for i in range (len(n)-1, 0 ,-1):
        if (n[i] == n[i-1] or s > k):
            s+=1
            if (o != n[i] and s > k):
                k=s
                s=1
        else:
            s=1
            o=n[i]
    print (k)
    return n
print (foo(k=0))