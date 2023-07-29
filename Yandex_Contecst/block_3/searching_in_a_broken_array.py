# ID - 88669455

def broken_search(array, target):
    length = len(array)
    low, high = 0, length - 1
    while low < high:
        mid = (low + high) // 2
        array_mid = array[mid]
        if array_mid == target:
            return mid
        if array_mid > array[high]:
            low = mid + 1
        else:
            high = mid

    offset = low

    low, high = 0, length - 1
    while low <= high:
        mid = (low + high) // 2
        real_mid = (mid + offset) % length
        value_real_mid = array[real_mid]
        if value_real_mid == target:
            return real_mid
        if array[mid] == target:
            return mid
        if value_real_mid < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == '__main__':
    target = 21
    array = [int(x) for x in '19 21 100 101 1 4 5 7 12'.split()]
    broken_search(array, target)