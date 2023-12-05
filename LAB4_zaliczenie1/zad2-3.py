# Ja miałem zrobić funkcję, która przyjmuje listę liczb i podmienia w tej
# liście liczby mniejsze od średniej liczb na największą liczbę z tej listy

list_of_numbers = [1, 2, 3, 4]


def below_avg_to_max(nums):
    new_nums = []
    nums_average = sum(nums) / len(nums)
    nums_max = max(nums)
    for num in nums:
        if num < nums_average:
            new_nums.append(nums_max)
        else:
            new_nums.append(num)
    return new_nums


print(below_avg_to_max(list_of_numbers))
