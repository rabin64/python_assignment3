# d) Merge Sort



def merge_sort(items):
    if len(items) > 1:
        mid_value = len(items) // 2
        left_half = items[:mid_value]
        right_half = items[mid_value:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                items[k] = left_half[i]
                i += 1
            else:
                items[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            items[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            items[k] = right_half[j]
            j += 1
            k += 1


input = [1,2,3,5,6,4,9,8,7]
merge_sort(input)
print(iinput)