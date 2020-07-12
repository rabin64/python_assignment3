# c) Quick Sort


def swap(a, b):
    a, b = b, a
    return (a, b)


def partition(items, lower, upper):
    pivot = items[upper]
    start = lower - 1
    for i in range(lower, upper):
        if (items[i] <= pivot):
            start = start + 1
            items[start], items[i] = items[i], items[start]
    items[start + 1], items[upper] = swap(items[start + 1], items[upper])
    return start + 1


def quick_sort(items, lower, upper):
    if lower < upper:
        location = partition(items, lower, upper)
        quick_sort(items, lower, location - 1)
        quick_sort(items, location + 1, upper)


input_list = [1,2,3,5,6,8,9,4,7]
last = len(input_list)
start = 0
quick_sort(input_list, start, last-1)
print(input_list)