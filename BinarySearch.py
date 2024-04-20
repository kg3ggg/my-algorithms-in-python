
def binary_search(num, nums):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == num:
            return mid + 1
        elif nums[mid] > num:
            high = mid - 1
        else:
            low = mid + 1

    return None


print(binary_search(99, [i for i in range(1, 101)]))
