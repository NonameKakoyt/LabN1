request_ids = [501, 507, 512, 507, 526, 531, 512, 544, 501, 558, 526]
unique_ids = set(request_ids)

print("список:", request_ids, "длина =", len(request_ids))
print("множество:", unique_ids, "длина =", len(unique_ids))
print("убрано дубликатов:", len(request_ids) - len(unique_ids))