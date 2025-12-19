# Вариант 2, Вислоухов
import json
choice = 0
print("start code …")
while True:
    # Меню ввода
    print(">> 1   Вывод записей")
    print(">> 2   Вывод записи по полю")
    print(">> 3   Добавить запись")
    print(">> 4   Удалить запись по полю ")
    print(">> 5   Выход их программы")
    print(" ")
    # Запрашиваем пункт
    choice = int(input("Выберите пункт: "))
    if(choice == 0 or choice <= 0 or choice > 5): # Проверяем правльное ли число
        print("Введено неверное число")
        print(" ")
    else:
        match choice: # Проверяем введеное число
            case 1:
                with open("dump.json", "r", encoding = "utf-8") as file:
                    data_1 = json.load(file) # Запрашиваем данные из файла
                    print(json.dumps(data_1, ensure_ascii=False, indent=4))

            case 2:
                search_id = input("Введите id записи: ") # Запрашиваем id записи
                with open("dump.json", "r", encoding="utf-8") as file:
                    data_2 = json.load(file) # Запрашиваем данные из файла

                flag = False
                for i, j in enumerate(data_2): # Перебираем данные из файла
                    if str(j.get("id")) == search_id:
                        print(json.dumps(j, ensure_ascii=False, indent=4))
                        flag = True
                        break
                if not flag: # Проверяем существует ли файл
                    print("Запись с таким id не найдена.")

            case 3:
                with open("dump.json", "r", encoding="utf-8") as file:
                    data_3 = json.load(file)  # Запрашиваем данные

                # Запрашиваем данные у пользователя
                new_id = int(input("Введите id: "))
                name = input("Введите название цветка: ")
                latin_name = input("Введите латинское название: ")
                is_red_book = input("Цветок краснокнижный? (да/нет): ").strip().lower() == "да"
                price = float(input("Введите цену: "))

                # Создаем словарь данных
                new_flower = {
                    "id": new_id,
                    "name": name,
                    "latin_name": latin_name,
                    "is_red_book_flower": is_red_book,
                    "price": price
                }

                if data_3 is None:
                    data_3 = []

                data_3.append(new_flower)  # Добавляем словарь в список

                # Сохраняем данные в файл
                with open("dump.json", "w", encoding="utf-8") as file:
                    json.dump(data_3, file, ensure_ascii=False, indent=4)

            case 4:
                delete_id = input("Введите id записи для удаления: ") # Запрашиваем id записи
                with open("dump.json", "r", encoding="utf-8") as file:
                    data_4 = json.load(file)

                original_len = len(data_4) 
                data_4 = [flower for flower in data_4 if str(flower.get("id")) != delete_id] # Перебираем список, ищем и удаяляем запись с введеным id

                if len(data_4) < original_len: # Проверяем удалился ли элемент
                    with open("dump.json", "w", encoding="utf-8") as file:
                        json.dump(data_4, file, ensure_ascii=False, indent=4) # Сохраняем изменения
                    print("Запись удалена.")
                else:
                    print("Запись с таким id не найдена.")

            case 5:
                break # Завершаем цикл
print("end code …")