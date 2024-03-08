class Solution:
    def maxProfit(self, array: list[int]) -> int:
        result = 0
        left = 0
        right = left + 1
        while right < len(array):
            if left == len(array) - 1:
                break
            if array[left] >= array[right]:
                left, right = right, right + 1
                continue
            while right < len(array):
                if array[left] > array[right]:
                    left, right = right, right + 1
                    continue
                else:
                    if result < (res := array[right] - array[left]):
                        result = res
                        right += 1
                    else:
                        right += 1
        return result


def main():
    s = Solution()
    assert s.maxProfit([1, 2, 4]) == 3
    assert s.maxProfit([1, 2]) == 1
    assert s.maxProfit([7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0


if __name__ == "__main__":
    main()
