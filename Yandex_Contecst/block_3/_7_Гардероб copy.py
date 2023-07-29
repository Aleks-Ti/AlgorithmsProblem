def closet(array):
    result = []
    pink = 0
    yellow = 0
    raspberry = 0

    cabinet = {
        '0': pink,
        '1': yellow,
        '2': raspberry,
    }

    for i in array:
        cabinet[i] += 1

    if cabinet['0'] != 0:
        result.append('0 ' * cabinet['0'])
    if cabinet['1'] != 0:
        result.append('1 ' * cabinet['1'])
    if cabinet['2'] != 0:
        result.append('2 ' * cabinet['2'])

    return ''.join(result)


if __name__ == '__main__':
    array_len = int(input())
    array = [x for x in input().split()]
    print(closet(array))
