def math_set(xin, yin):
    if xin[0] >= yin[0] and xin[0] <= yin[-1]:
        return True
    if xin[-1] >= yin[0] and xin[-1] <= yin[-1]:
        return True
    return False


def plant_union(xin, yin) -> str:
    result = []
    if int(xin[0]) < int(yin[0]):
        result.append(xin[0])
    else:
        result.append(yin[0])

    if int(xin[-1]) < int(yin[-1]):
        result.append(yin[-1])
    else:
        result.append(xin[-1])
    return result


def flowerbeds(array: list, array_len):
    result=[]
    array.sort()
    count = 0
    zero = array[0]
    for i in range(array_len - 1):
        for j in range(1, array_len):
            CONTROL = zero
            CONTROL1 = array[j]
            if zero == array[j]:
                break
            if math_set(array[i], array[j]):
                asd = plant_union(array[i], array[j])
                zero = asd
                continue
            else:
                if zero not in result:
                    result.append(zero)
                if array[j] not in result:
                    result.append(array[j])
                zero = array[j]

    for _ in result:
        print(*_)
    return None

if __name__ == '__main__':
    array_len = int(input())
    array = [x.split() for x in range(array_len) for x in input().split('\n')]
    # array = [x.split() for x in ['7 8', '7 8', '2 3', '6 10']]
    array = flowerbeds(array, array_len)