# ID - 88670158


def quick_sorting(array):
    if len(array) == 1:
        return array

    def sorting(start, end):
        if start >= end:
            return array
        mid = (start + end) // 2
        pivot = array[mid]
        left, right = start, end
        while left < right:
            while array[left] < pivot:
                left += 1
            while pivot < array[right]:
                right -= 1
            if left <= right:
                array[left], array[right] = (
                    array[right],
                    array[left],
                )
                left += 1
                right -= 1

        sorting(start, right)
        sorting(left, end)

        return array

    return sorting(0, len(array) - 1)


if __name__ == '__main__':
    def permutation(name, points, penalty):
        return -int(points), int(penalty), name

    print(
        *(
            login
            for _, _, login in quick_sorting(
                [permutation(*input().split()) for _ in range(int(input()))]
            )
        ),
        sep='\n'
    )
