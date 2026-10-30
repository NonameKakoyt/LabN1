import sys

users = {101: "Иван", 102: "Анна", 103: "Петр", 104: "Мария", 105: "Олег", 106: "Елена"}
print("Имя по ключу 102:", users[102])

lst = list(range(6))
tpl = tuple(range(6))
st = set(range(6))
dct = {i: i for i in range(6)}

print("Размер списка:", sys.getsizeof(lst), "байт")
print("Размер кортежа:", sys.getsizeof(tpl), "байт")
print("Размер множества:", sys.getsizeof(st), "байт")
print("Размер словаря:", sys.getsizeof(dct), "байт")

total = sys.getsizeof(users)
for k, v in users.items():
    total += sys.getsizeof(k) + sys.getsizeof(v)
print("Полный размер словаря со строками:", total, "байт")