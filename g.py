# f) Interpolation Search

def interpolation_search(items, start, last, find_item):
    if (start <= last and find_item >= items[start] and find_item <= items[last]):

        position = start + ((last - start) // (items[last] - items[start]) * (
                    find_item - items[start]))
        if items[position] == find_item:
            return position
        elif items[position] < find_item:
            return interpolation_search(items, position + 1, last, find_item)
        else:
            return interpolation_search(items, start, position - 1, find_item)
    return -1


input = [1,2,5,7,9,10,15]
start = 0
last = len(input) - 1
result = interpolation_search(input, start, last, 10)
print(result)
