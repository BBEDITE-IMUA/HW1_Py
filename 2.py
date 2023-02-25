x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

position1 = 4
position2 = 4

# Определим часть в которой находится первая точка:
if x1 > 0 and y1 > 0:
    position1 = 1

elif x1 < 0 and y1 > 0:
    position1 = 2

elif x1 < 0 and y1 < 0:
    position1 = 3


# Определим часть в которой находится вторая точка:
if x2 > 0 and y2 > 0:
    position2 = 1

elif x2 < 0 and y2 > 0:
    position2 = 2

elif x2 < 0 and y2 < 0:
    position2 = 3


# Выполняем проверку условия, и если четверти одинаковые - выводим результат "YES", если четверти разные то выводим - "NO":
if position1 == position2:
    print("YES")
else:
    print("NO")