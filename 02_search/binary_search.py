import random


def binary_search(numbers, value):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def selection_sort(numbers: list[int]) -> list[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_idx = i
        for j in range(i + 1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers


if __name__ == '__main__':
    numbers = [random.randint(0, 1000) for _ in range(10)]
    numbers = [196, 268, 280, 343, 384, 440, 454, 537, 801, 982]
    print(numbers)
    sort_numbers = selection_sort(numbers=numbers)
    print(sort_numbers)
    print(binary_search(sort_numbers, 280))
