def buble_sort_back(array_len, array: list):

    flag = True
    while flag:
        count = 0
        count_equal = 0
        for i in range(array_len):
            if i + 1 != array_len:
                if array[i] > array[i + 1]:
                    count += 1
                    array[i], array[i + 1] = array[i + 1], array[i]
                elif array[i] == array[i + 1]:
                    count_equal += 1
                    if count_equal == array_len - 1:
                        print(' '.join([str(x) for x in array]))
                else:
                    pass
            else:
                break
        if count != 0 and array_len > 2:
            print(' '.join([str(x) for x in array]))
        elif count == 0 and array_len <= 2:
            print(' '.join([str(x) for x in array]))
            return False
        else:
            return False


if __name__ == '__main__':
    array_len = 2
    array = [int(x) for x in '4 5'.split()]
    buble_sort_back(array_len, array)
    