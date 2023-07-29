number = int(input())


def convert_binary(num: int):
    result = []
    num = num
    if num == 0:
        return 0
    while num >= 1:
        if num % 2 != 0:
            result.append('1')
            num = num // 2
        if num % 2 == 0:
            result.append('0')
            num = num // 2

    result = ''.join((result[::-1]))
    if result[0] == '0':
        return result[1::]
    return result


print(convert_binary(number))
