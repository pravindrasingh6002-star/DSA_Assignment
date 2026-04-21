import time
import random
import sys

# Increase recursion limit (safety)
sys.setrecursionlimit(20000)

# -------------------------------
# Insertion Sort
# -------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# -------------------------------
# Merge Sort
# -------------------------------
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# -------------------------------
# Quick Sort (Random Pivot FIXED)
# -------------------------------
def partition(arr, low, high):
    # Random pivot to avoid worst-case recursion
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    while low < high:   # tail recursion optimization
        pi = partition(arr, low, high)

        # Sort smaller part first (reduces recursion depth)
        if pi - low < high - pi:
            quick_sort(arr, low, pi - 1)
            low = pi + 1
        else:
            quick_sort(arr, pi + 1, high)
            high = pi - 1


# -------------------------------
# Timing Function
# -------------------------------
def measure_time(sort_func, arr):
    arr_copy = arr.copy()
    start = time.time()

    if sort_func == quick_sort:
        sort_func(arr_copy, 0, len(arr_copy) - 1)
    else:
        sort_func(arr_copy)

    end = time.time()
    return round((end - start) * 1000, 3)  # ms


# -------------------------------
# Dataset Generator
# -------------------------------
def generate_datasets(size):
    random_list = random.sample(range(1, 100000), size)
    sorted_list = sorted(random_list)
    reverse_list = sorted_list[::-1]

    return random_list, sorted_list, reverse_list


# -------------------------------
# Main
# -------------------------------
def main():
    sizes = [1000, 5000, 10000]

    with open("output.txt", "w") as f:
        f.write("Sorting Performance Results (ms)\n\n")

        # Correctness Check
        test = [5, 2, 9, 1, 5, 6]

        arr1 = test.copy()
        insertion_sort(arr1)

        arr2 = test.copy()
        merge_sort(arr2)

        arr3 = test.copy()
        quick_sort(arr3, 0, len(arr3) - 1)

        f.write("Correctness Check:\n")
        f.write(f"Insertion: {arr1}\n")
        f.write(f"Merge: {arr2}\n")
        f.write(f"Quick: {arr3}\n\n")

        # Experiments
        for size in sizes:
            random_list, sorted_list, reverse_list = generate_datasets(size)

            f.write(f"\nSize: {size}\n")
            f.write("Type\t\tInsertion\tMerge\tQuick\n")

            # Random
            f.write(f"Random\t\t{measure_time(insertion_sort, random_list)}\t\t"
                    f"{measure_time(merge_sort, random_list)}\t\t"
                    f"{measure_time(quick_sort, random_list)}\n")

            # Sorted
            f.write(f"Sorted\t\t{measure_time(insertion_sort, sorted_list)}\t\t"
                    f"{measure_time(merge_sort, sorted_list)}\t\t"
                    f"{measure_time(quick_sort, sorted_list)}\n")

            # Reverse
            f.write(f"Reverse\t\t{measure_time(insertion_sort, reverse_list)}\t\t"
                    f"{measure_time(merge_sort, reverse_list)}\t\t"
                    f"{measure_time(quick_sort, reverse_list)}\n")

    print("✅ Done! Check output.txt")


if __name__ == "__main__":
    main()