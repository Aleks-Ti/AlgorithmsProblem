def merge(arr, lf, mid, rg):
    result = []
    left = arr[lf:mid]
    right = arr[mid:rg]
    i_left = i_right = 0
    while len(result) < len(left) + len(right):
        if left[i_left] <= right[i_right]:
            result.append(left[i_left])
            i_left += 1
        else:
            result.append(right[i_right])
            i_right += 1
        if i_right == len(right):
            result += left[i_left:]
            break
        if i_left == len(left):
            result += right[i_right:]
            break
    return result


def merge_sort(arr, lf, rg) -> None:
    if rg - lf >= 2:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        arr[lf:rg] = merge(arr, lf, mid, rg)

    return arr


def main(array):
    a = array
    b = merge_sort(a, 0, len(a))
    return ' '.join(str(num) for num in b)


if __name__ == '__main__':
    command = str(input())
    array_length = int(input())
    array = [int(x) for x in input().split()]
    if array_length == 1:
        print(array[0])
    else:
        print(main(array))