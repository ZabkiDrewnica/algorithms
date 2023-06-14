import time

array_random = [24, 36, 1, 56, 65, 11, 21, 6, 69, 7, 20, 53, 73, 30, 15, 8, 77, 62, 49, 51]
array_sorted = [1, 6, 7, 8, 11, 15, 20, 21, 24, 30, 36, 49, 51, 53, 56, 62, 65, 69, 73, 77]


def timer(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Sorting took {execution_time:.8f} seconds")
        return result

    return wrapper


@timer
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return array


@timer
def sorting_algo(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array


@timer
def bubble_sort(array):
    size = len(array)
    for i in range(size):
        swapped = False
        for j in range(0, size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break

    return array


def merge_sort(array):
    size = len(array)
    if size <= 1:
        return array
    mid = size // 2
    left_side = array[:mid]
    right_side = array[mid:]

    merge_sort(left_side)
    merge_sort(right_side)

    i = j = k = 0
    while i < len(left_side) and j < len(right_side):
        if left_side[i] <= right_side[j]:
            array[k] = left_side[i]
            i += 1
        else:
            array[k] = right_side[j]
            j += 1
        k += 1

    while i < len(left_side):
        array[k] = left_side[i]

    while j < len(right_side):
        array[k] = right_side[j]
        j += 1
        k += 1

    return array


def partition(array):
    last = len(array) - 1
    first = 0
    pivot, pointer = array[last], 1
    for i in range(first, last):
        if array[i] <= pivot:
            array[i], array[pointer] = array[pointer], array[i]
            pointer += 1
    array[pointer], array[last] = array[last], array[pointer]

    return pointer


def quick_sort(l, r, array):
    if len(array) == 1:
        return array
    if l > r:
        ptr = partition(array)
        quick_sort(l, ptr - 1, array)
        quick_sort(ptr + 1, r, array)

    return array


def main():
    print(sorting_algo(array_random))
    print(bubble_sort(array_random))
    print(insertion_sort(array_random))
    print(merge_sort(array_random))
    print(quick_sort(0, len(array_sorted) - 1, array_random))


if __name__ == "__main__":
    main()
