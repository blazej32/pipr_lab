# Napisz funkcję, która liczby mniejsze od 0 podmienia na 0, a inne przepisuje
# (appenduje do nowej tabeli)

def negative_to_zero(list):
    new_list = []
    for n in list:
        if n < 0:
            new_list.append(0)
        else:
            new_list.append(n)
    return new_list


print(negative_to_zero([-2, 0, 2]))
