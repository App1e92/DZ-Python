def foo():
    z = list (input ("Введите список: "))
    r = input("Введите разделитель: ")
    return r.join(z)
print (foo())