def foo():
    H = int (input ("Введите количество часов (0 ≤ H < 12): "))
    M = int (input ("Введите количество минут (0 ≤ M < 60): "))
    S = int (input ("Введите количество секунд (0 ≤ S < 60): "))
    degreesH = H * 60
    degreesM = M
    degreesS = S / 60
    minute = degreesS + degreesH + degreesM
    degrees = minute / 2
    return degrees
print (foo())