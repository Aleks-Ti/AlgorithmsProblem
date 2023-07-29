def pascal(rowIndex: int):
    if rowIndex == 0:
        return [1]

    result = [[1] * (row + 1) for row in range(rowIndex + 1)]

    if len(result) <= 2:
        return result[-1]

    for row in range(2, rowIndex + 1):
        for item_index in range(1, len(result[row - 1])):
            result[row][item_index] = (
                result[row - 1][item_index - 1] + result[row - 1][item_index]
            )

    return result[-1]


if __name__ == '__main__':
    data_user = int(input())
    print(pascal(data_user))
