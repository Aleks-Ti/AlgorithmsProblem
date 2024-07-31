"""
Есть массив с числамиб нужно получить строку, в которой подряд идущие \
    числа из массива `свернуты` и все диапазоны идут по возрастанию.
"""


def shrink(data: list):
    result = ""
    left_ind = 0
    right_ind = 1
    data.sort()
    while True:
        if right_ind >= len(data) - 1:
            if right_ind == len(data) - 1:
                result += f"{str(data[left_ind])}-{str(data[right_ind])}"
            else:
                result += str(data[left_ind])
                break
        elif data[left_ind + 1] != data[left_ind] + 1:
            result += str(data[left_ind]) + ", "
            left_ind = right_ind
            right_ind = left_ind + 1

        elif data[right_ind] + 1 == data[right_ind + 1]:
            right_ind += 1
        else:
            result += f"{str(data[left_ind])}-{str(data[right_ind])}, "
            left_ind = right_ind + 1
            right_ind = left_ind + 1
    return result


if __name__ == "__main__":
    data = [1, 5, 7, 6, 2, 9]
    data1 = [1, 2, 8, 3, 4, 6, 7, 9, 15, 16, 17, 18, 19, 20, 11]
    data2 = [1, 8, 15, 16, 17, 20, 11]
    assert shrink(data1) == "1-4, 6-9, 11, 15-20"
    assert shrink(data) == "1-2, 5-7, 9"
    assert shrink(data2) == "1, 8, 15-20, 11"
