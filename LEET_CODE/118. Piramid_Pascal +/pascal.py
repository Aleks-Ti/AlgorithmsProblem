def pascal(piramid_row: int):
    if piramid_row == []:
        return None

    result = [[1] * (row + 1) for row in range(piramid_row)]

    if len(result) <= 2:
        return result

    for row in range(2, piramid_row):
        for item_index in range(1, len(result[row - 1])):
            result[row][item_index] = (
                result[row - 1][item_index - 1] + result[row - 1][item_index]
            )

    return result


if __name__ == '__main__':
    data_user = int(input())
    print(pascal(data_user))
