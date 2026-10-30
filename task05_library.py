rules = ("Техно", 21, 5)

requests = [501, 507, 512, 526, 531, 544]

debtors = {507, 526, 544}

books = {
    "B-101": "Чистый код",
    "B-102": "Алгоритмы",
    "B-103": "Python. К вершинам мастерства",
    "B-104": "Паттерны проектирования",
}

print(f"Правила выдачи: библиотека «{rules[0]}», {rules[1]} день, не более {rules[2]} книг")
print("Заявки в порядке поступления:", ", ".join(map(str, requests)))
print("Читатели с задолженностью:", ", ".join(map(str, sorted(debtors))))
print("Книги:", "; ".join(f"{num} - «{title}»" for num, title in books.items()))
print()

requests.append(558)
print("После добавления заявки:", ", ".join(map(str, requests)))

reader_id = 526
has_debt = reader_id in debtors
print(f"Читатель {reader_id} имеет задолженность: {'да' if has_debt else 'нет'}")

inventory_number = "B-102"
book_title = books.get(inventory_number, "книга не найдена")
print(f"Книга с номером {inventory_number}: «{book_title}»")