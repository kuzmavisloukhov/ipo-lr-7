# Вариант 2, Вислоухов
print("start code …")
book = []
for i in range(1, 6):
    book.append(dict(
        title = input("Введите название:"),
        author = input("Введите автора: "),
        year = input("Введите год: "))) 


for i in range(len(book)):
    print("-" * 20, f"Книга {i + 1}", "-" * 20)
    print(f"Название: {book[i]["title"]}, Автор: {book[i]["author"]},")
    print("-" * 20, book[i]["year"], "-" * 20)
print("end code …")
