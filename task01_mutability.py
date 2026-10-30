values = [10, 20, 30, 40, 50, 60]
tup = (10, 20, 30, 40, 50, 60)

print("список:", type(values), id(values))
print("кортеж:", type(tup), id(tup))

list_id_before = id(values)
values[2] = 99
print("список после изменений:", values, "то же id:", id(values) == list_id_before)

new_tup = (10, 20, 99, 40, 50, 60)
print("старый id кортежа:", id(tup))
print("новый id кортежа:", id(new_tup))
print("id равны? :", id(tup) == id(new_tup))