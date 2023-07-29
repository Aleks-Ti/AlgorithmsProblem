def plusOne(digits: list):
    convert = int(''.join([str(x) for x in digits])) + 1
    return [int(x) for x in str(convert)]


if __name__ == '__main__':
    print(plusOne([9, 9]))
