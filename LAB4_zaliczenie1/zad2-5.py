# Ja miałem napisać funkcję, która przyjmuje listę stringów i zwraca liczbę
# stringów z tej listy, w których liczba znaków jest liczbą parzystą

words = ['aa', 'a', 'aaa', 'aaaa']


def even_length_strings(list):
    new_list = []
    for word in list:
        if len(word) % 2 == 0:
            new_list.append(word)
    return new_list


print(even_length_strings(words))
