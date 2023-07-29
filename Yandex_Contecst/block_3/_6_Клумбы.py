def flowerbeds(array: list, array_len):
    result = []
    array.sort()
    count = 0
    left, right = array[count]
    while count < array_len:
        if left <= array[count][0] <= right:
            _, rest = array[count]
            count += 1
            if rest > right:
                right = rest
        else:
            result.append([left, right])
            left, right = array[count]
            count += 1
    result.append([left, right])

    for _ in result:
        print(*_)
    return None


if __name__ == '__main__':
    array_len = int(input())
    # array = [x.split() for x in range(array_len) for x in input().split('\n')]
#     array = [x.split() for x in ['2 3',
# '5 6',
# '3 4',
# '3 4']]
    array = [list(map(int, input().split())) for _ in range(array_len)]
    flowerbeds(array, array_len)
