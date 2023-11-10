test_word = 'abababacccvsfgar'


def counting_letters(word):
    counting_dict = {}
    for char in word:
        counting_dict[char] = counting_dict.get(char, word.count(char))
    return counting_dict


print(counting_letters(test_word))
