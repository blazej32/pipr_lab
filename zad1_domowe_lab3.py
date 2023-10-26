def count_symbols(letter_grid):
    counter = {}
    for letter_list in letter_grid:
        for letter in letter_list:
            counter[letter] = counter.get(letter, 0) + 1
    return counter


test_grid = [['a', 'c', 'o'],
             ['a', 'a', 'c'],
             ['d', 'o', 'O'],
             ['c', 'b', 'a']]

print(count_symbols(test_grid))
