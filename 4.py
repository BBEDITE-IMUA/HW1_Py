a = input()

units = " "
dozens = " "

# Формируем единицы:
if a[-1] == "1":
    units = "I"
elif a[-1] == "2":
    units = "II" 
elif a[-1] == "3":
    units = "III"
elif a[-1] == "4":
    units = "IV"
elif a[-1] == "5":
    units = "V"
elif a[-1] == "6":
    units = "VI"
elif a[-1] == "7":
    units = "VII"
elif a[-1] == "8":
    units = "VIII"
elif a[-1] == "9":
    units = "IX"

# Формируем десятки:
if int(a) > 9:
    if int(a[0]) == 4:
        dozens = "XL"
    elif 9 > int(a[0]) >= 5:
        dozens = "L" + "X" * (int(a[0]) - 5)
    elif int(a[0]) == 9:
        dozens = "XM"
    elif int(a) == 100:
        dozens = "M"
    else:
        dozens = "X" * int(a[0])

print(dozens + units)