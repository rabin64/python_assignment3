#e. Linear Search


def linear_search(items, find_item):
    for index in range(0,len(items)):
        if find_item == items[index]:
            return index

res = linear_search([1,2,4,6,7,8,9,3,5], 5)
print(res)