num = int(input("enter 1-4"))

yea_={
    1:"зима",
    2:"весна",
    3:"лето",
    4:"осень",
    }
print(yea_[num])


# задача на вес, рост, возраст, имя

from collections import namedtuple

name = input("Назовись воин!")
a = float(input("Возраст"))
b = float(input("Рост"))
c = float(input("Вес"))

user_info = {
 "Имя" : name if name != "" else name,
"Возраст": a if a > 0 else "Неверный ввод",
"Рост": b if b > 0 and b<290 else "Неверный ввод",
"Вес": c if c > 0 and b<180 else "Неверный ввод",
}

if 0 < a <= 18:
    user_info["возраст"] = "Молодой"
elif 18 < a < 40:
    user_info["возраст"] = "В расцвете сил"
elif 40 < a < 140:
    user_info["возраст"] = "Не молодой"
elif 140 < a < 10000000000000000000000000000000000:
    user_info["возраст"] = "Грязный врунишка"

if 0 < b < 100:
    user_info["Рост"] = "Низкий"
elif 100 < b <= 180:
    user_info["Рост"] = "Обычный"
elif 180 < b < 300:
    user_info["Рост"] = "Высокий"
elif 300 < b < 100000000000000000000000000000000000000000000000000000000000:
    user_info["Рост"] = "Грязный врунишка"

if 0 < c < 50:
    user_info["Вес"] = "Худой"
elif 50 < c < 90:
    user_info["Вес"] = "Средний"
elif 90 < c < 400:
    user_info["Вес"] = "Кость широкая"
elif 400 <= c < 10000000000000000000000000000000000000000:
    user_info["Вес"] = "Я бы задумался..."

print("Твое имя:", name, "вес - ", user_info["Вес"], "рост -",user_info["Рост"], "возраст -", user_info["возраст"] )

#print(f"{name}")

#user = namedtuple("User",["user","Рост"])
#u = user(name,age=user_info.get("Рост"))
#print(u)