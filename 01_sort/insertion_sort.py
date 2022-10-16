import random


def insertion_sort(numbers):
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            # print(j, end=' ')
            numbers[j + 1] = numbers[j]
            j -= 1
        temp = numbers[j + 1]
    return numbers


if __name__ == '__main__':
    numbers = [random.randint(0, 1000) for _ in range(10)]
    print(numbers)
    print(insertion_sort(numbers=numbers))
