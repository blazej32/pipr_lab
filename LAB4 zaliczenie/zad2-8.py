# Z listy stringów zwróć ile z nich zaczyna się i kończy na tą samą literę

test_list = ['aa', 'ab', 'aba', 'abab', 'ababaa']


def first_equals_last(words):
    counter = 0
    for word in words:
        if word[0] == word[-1]:
            counter += 1
    return counter


print(first_equals_last(test_list))
