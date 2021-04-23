def foo ():
    c1 = int (input("Введите количсетво учащихся в первом классе: "))
    c2 = int (input("Введите количсетво учащихся во втором классе: "))
    c3 = int (input("Введите количсетво учащихся в третьем классе: "))
    desks = (c1 + c2+ c3)
    if (desks % 2 != 0 ):
        desks = (desks+1) / 2
    else:
        desks = desks / 2
    return round(desks)
print (foo())