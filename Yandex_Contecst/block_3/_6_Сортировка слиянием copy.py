def merge(arr, lf, mid, rg):
    left = arr[lf:mid]
    right = arr[mid:rg]

    l, r, k = 0, 0, lf
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr[k] = left[l]
            l += 1
        else:
            arr[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        arr[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
        arr[k] = right[r]
        r += 1
        k += 1

    return arr


def merge_sort(arr, lf, rg):
    if rg - lf > 1:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        merge(arr, lf, mid, rg)

    return arr


def main(array):
    a = array
    b = merge_sort(a, 0, len(a))
    return ' '.join(str(num) for num in b)


# def test():
#     a = [1, 4, 9, 2, 10, 11]
#     b = merge_sort(a, 0, len(a))
#     expected = [1, 2, 4, 9, 10, 11]
#     assert b == expected

#     c = [1, 4, 2, 10, 1, 2]
#     merge_sort(c, 0, len(c))
#     expected = [1, 1, 2, 2, 4, 10]
#     assert c == expected


if __name__ == '__main__':
    command = str(input())
    array_length = int(input())
    array = [int(x) for x in input().split()]
    if array_length == 1:
        print(array[0])
    else:
        print(main(array))
