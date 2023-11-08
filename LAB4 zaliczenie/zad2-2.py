# Ja miałem napisać funkcję, która przyjmuje listę wyrazów i zwraca ilość
# znaków w najdłuższym wyrazie

words = ['a', 'a', 'a', 'a']


def max_length(list_of_words):
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length


print(max_length(words))
