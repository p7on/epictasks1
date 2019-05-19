import random


def search_number(put_something):
    counter = 0
    min_index = some_numbers.index(min(some_numbers))
    max_index = some_numbers.index(max(some_numbers))
    for negative_number in some_numbers[min_index: max_index]:
        if negative_number < 0:
            counter += 1
        else:
            continue
    return counter


some_numbers = [random.randrange(-1000, 1000) for number in range(1000)]
print(search_number(some_numbers))
