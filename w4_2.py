str_1 = "Break and Continue operators"
num=0
for i in str_1:
    num += 1
    if i == "p":
        break
    if num%3 == 0:
        continue
    print(i)