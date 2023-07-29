# ID - 87713369
from typing import List


def hous(number_of_houses: int, houses_map: List[int]) -> list:
    result = []
    count = 1
    count_null = 0
    for index_hous in range(number_of_houses):
        if houses_map[index_hous] != 0:
            result.append(count)
            count += 1
        else:
            count_null += 1
            if index_hous != 0:
                if count_null == 1:
                    result.reverse()
                    result.append(0)
                    count_null += 1
                    count = 1
                elif result[index_hous - 1] == 2:
                    result[index_hous - 1] = 1
                    count = 1
                    result.append(0)
                elif result[index_hous - 1] > 2:
                    step = result[index_hous - 1] // 2
                    for i in range(1, step + 1):
                        result[index_hous - i] = i
                    count = 1
                    result.append(0)
                else:
                    count = 1
                    result.append(0)
            else:
                count = 1
                result.append(0)

    return result


if __name__ == '__main__':
    number_of_houses = int(input())
    houses_map = [int(x) for x in input().split()]
    print(*hous(number_of_houses, houses_map), sep=' ')
