def subsequence(array_inner, array):
    # count_array = 0
    count_inner = 0
    for char in array:
        CONTROL = array_inner[count_inner]
        if array_inner[count_inner] == char:
            count_inner += 1
        if count_inner >= len(array_inner):
            print(True)
            return

    print(False)


# if __name__ == '__main__':
#     array_inner = str(input())
#     array = str(input())
#     subsequence(array_inner, array)


if __name__ == '__main__':
    array_inner = 'abcp'  # str(input())
    array = 'ahpc'  # str(input())
    subsequence(array_inner, array)
