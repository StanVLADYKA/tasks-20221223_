# Вычислить индекс массы (ИМТ = масса в кг/ (рост в метрах возвести
# в квадрат)

w = int(input("𝑤𝑒𝑖𝑔ℎ𝑡 (kg) :"))
h = int(input("ℎ𝑒𝑖𝑔ℎ𝑡 (sm) :"))
a = int(input("age (ears) :"))

i = w / (h/100)**2

print(i)

if a < 45:
    if i < 18.5:
        res = 1
    elif i >= 18.5 and i < 24.99:
        res = 2
    elif i > 25 and i < 29.99:
        res = 3
    elif i >= 30:
        res = 4
else:
    if i < 22:
        res = 1
    elif i >= 22 and i < 26.99:
        res = 2
    elif i >27 and i < 31.99:
        res = 3
    elif i >= 32:
        res = 4


if res == 1:
    print("Underweight")
elif res == 2:
    print("Norm")
elif res == 3:
    print("Overweight")
elif res == 4:
    print("Obesity")