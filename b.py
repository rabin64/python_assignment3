# b) Insertion Sort

def insertion_sort(items):
    len_of_list = len(items)
    for i in range(0,len_of_list):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:
            items[j+1] = items[j]
            j = j - 1
        items[j + 1] = key
    return items

res = insertion_sort([1,2,4,6,7,3,9,8])
print(res)