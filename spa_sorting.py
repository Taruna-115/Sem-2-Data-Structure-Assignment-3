"""
Sorting Performance Analyzer (SPA)
Data Structures - Unit 2 Assignment

Name of the School:        	School of Engineering & Technology 
Program: 					B.Tech (AI and ML) 
Course Title:				Data Structures 
Course Code:				ETCCDS202 
Unit Title:					Sorting Algorithms
Student Name:				Taruna Tewatia 
Roll Number:				2501730115 
Section:					A 
Semester:					2 
Batch:					    2025-26 
Submitted To:				Mrs. Neetu Chauhan 
"""

import random
import time
import sys
sys.setrecursionlimit(20000)




# Task 1: Sorting Algorithms
# -----------------------------



# 1. Insertion Sort (Stable, In-place)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr



# 2. Merge Sort (Stable, Out-of-place)
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)



# 3. Quick Sort (In-place, Not Stable)
def partition(arr, low, high):
    import random
    
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Wrapper for quick sort
def quick_sort_wrapper(arr):
    quick_sort(arr, 0, len(arr) - 1)
    return arr






# Task 2: Timing Utility
# -----------------------------

def measure_time(sort_func, arr):
    arr_copy = arr.copy()
    start = time.time()

    if sort_func == quick_sort_wrapper:
        sort_func(arr_copy)
    else:
        sort_func(arr_copy)

    end = time.time()
    return (end - start) * 1000  # milliseconds




# Dataset Generator
# -----------------------------

def generate_datasets():
    sizes = [1000, 5000, 10000]
    datasets = {}

    random.seed(42)

    for size in sizes:
        datasets[("random", size)] = [random.randint(1, 100000) for _ in range(size)]
        datasets[("sorted", size)] = list(range(size))
        datasets[("reverse", size)] = list(range(size, 0, -1))

    return datasets




# Correctness Check
# -----------------------------

def check_correctness():
    test = [5, 2, 9, 1, 5, 6]
    expected = sorted(test)

    assert insertion_sort(test.copy()) == expected
    assert merge_sort(test.copy()) == expected

    temp = test.copy()
    quick_sort_wrapper(temp)
    assert temp == expected

    return "Correctness Check Passed!"




# Run Experiments
# -----------------------------

def run_experiments():
    datasets = generate_datasets()

    algorithms = [
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort_wrapper)
    ]

    results = []

    for (dtype, size), data in datasets.items():
        for name, func in algorithms:
            time_taken = measure_time(func, data)
            results.append((dtype, size, name, round(time_taken, 3)))
            print(f"{dtype} | {size} | {name} | {round(time_taken, 3)} ms")

    return results




# Save Output
# -----------------------------

def save_output(results):
    with open("output.txt", "w") as f:
        f.write("Type | Size | Algorithm | Time (ms)\n")
        f.write("-" * 50 + "\n")
        for r in results:
            f.write(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} ms\n")




# Main
# --------

def main():
    print(check_correctness())
    print("\nRunning Experiments...\n")

    results = run_experiments()
    save_output(results)

    print("\nResults saved to output.txt")


if __name__ == "__main__":
    main()
