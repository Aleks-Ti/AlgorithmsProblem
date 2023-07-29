def closet(array):
    result = []
    pink = []
    yellow = []
    raspberry = []

    cabinet = {
        '0': lambda x: pink.append(x),
        '1': lambda x: yellow.append(x),
        '2': lambda x: raspberry.append(x),
    }

    for i in array:
        cabinet[i](i)

    if pink != []:
        result.append(' '.join(pink))
    if yellow != []:
        result.append(' '.join(yellow))
    if raspberry != []:
        result.append(' '.join(raspberry))

    return ' '.join(result)


if __name__ == '__main__':
    array_len = int(input())
    array = [x for x in input().split()]
    print(closet(array))
