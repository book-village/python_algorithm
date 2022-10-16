import random


# forループが２重となっているため、オーダはn**2となる
def bubble_sort(numbers: list[int]) -> list[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == '__main__':
    # numbers = [1, 5, 4, 3, 6, 9, 8, 7, 6]
    numbers = [random.randint(0, 1000) for _ in range(1000)]
    print(bubble_sort(numbers))
