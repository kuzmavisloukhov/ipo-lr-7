# Вариант 2, Вислоухов 
import json

print("start code …")

with open("dump.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

flag = False
num = input("Введите номер специальности: ")

for i in data:
    fields = i.get("fields", {})
    code = fields.get("code", "")
    if(code == num):
        print("=" * 15, " Найдено ", "=" * 15)
        print(num, ">>", " Специальность", fields.get("title", ""), fields.get("c_type", ""))
        flag = True

if(flag == False):
     print("=" * 15, " Не найдено ", "=" * 15)

print("end code …")