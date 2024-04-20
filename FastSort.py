
def fast_sort(lst):
    if len(lst) <= 1:
        return lst

    support_element = lst[0]
    lefts = list(filter(lambda x: x < support_element, lst))
    center = list(filter(lambda x: x == support_element, lst))
    right = list(filter(lambda x: x > support_element, lst))

    return fast_sort(lefts) + center + fast_sort(right)


print(fast_sort([1, 4, 56, 76, 8, 3, 1]))
