def big_number(array_len, array):
    for i in range(array_len - 1):
        for j in range(0, array_len-i-1):
            num1 = array[j] + array[j+1]
            num2 = array[j + 1] + array[j]
            if num1 < num2:
                array[j], array[j+1] = array[j+1], array[j]

    print("".join(array))


if __name__ == '__main__':
    array_len = int(input())
    array = [x for x in input().split()]
    big_number(array_len, array)
