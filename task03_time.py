import timeit

for n in [1000, 10000, 100000]:
    my_list = list(range(n))
    my_set = set(my_list)
    
    t_list_yes = timeit.timeit(lambda: (n-1) in my_list, number=1000) / 1000
    t_set_yes = timeit.timeit(lambda: (n-1) in my_set, number=1000) / 1000
    
    t_list_no = timeit.timeit(lambda: (n+1) in my_list, number=1000) / 1000
    t_set_no = timeit.timeit(lambda: (n+1) in my_set, number=1000) / 1000
    
    print(f"n={n}:")
    print(f"  Список (есть): {t_list_yes*1000000:.2f} мкс, (нет): {t_list_no*1000000:.2f} мкс")
    print(f"  Множ.  (есть): {t_set_yes*1000000:.2f} мкс, (нет): {t_set_no*1000000:.2f} мкс")