#a)	Bubble Sort


def bubble_sort(lst):
    size = len(lst)
    for i in range(size):
        for j in range(0,size-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
unsorted_list = [1,2,5,7,8,9,6,4]
res = bubble_sort(unsorted_list)

print(res)