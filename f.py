# f) Binary Search


def binary_search(items, start, last, find_item):
    if last >= 1:
        mid = (start + last) // 2

        if items[mid] == find_item:
            return mid
        elif items[mid] > find_item:
            return binary_search(items, start, mid -1, find_item )
        else:
            return binary_search(items, mid + 1, last, find_item)

input= [1,2,3,6,8,9,4,5,7]
last = len(input - 1)

result = binary_search(input, 0, last, 8)
print(result)