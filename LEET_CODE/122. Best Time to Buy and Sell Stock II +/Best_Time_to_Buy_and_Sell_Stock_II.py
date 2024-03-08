class Solution:
    def maxProfit(self, array: list[int]) -> int:
        result = 0
        left = 0
        right = left + 1

        for _ in range(len(array) + 1):
            if len(array) <= right:
                break

            if right >= len(array) and result == 0 and right - 1 == left:
                break

            if right >= len(array) - 1:
                if (
                    right >= len(array) - 1
                    and right - 1 == left
                    and array[right] < array[left]
                ):
                    break
                result += array[right] - array[left]
                left = right + 1
                right = left + 1
                if right >= len(array) and result == 0 and right - 1 == left:
                    break
                continue
            if array[left] < array[right]:
                if right == len(array) - 1:
                    left = right + 1
                    right = left + 1
                    continue
                if array[right] > array[right + 1]:
                    result += array[right] - array[left]
                    left = right + 1
                    right = left + 1
                    continue
                right += 1
            else:
                left += 1
                right += 1

        return result


def main():
    s = Solution()
    assert s.maxProfit([1, 7, 4, 2]) == 6
    assert s.maxProfit([1, 2]) == 1
    assert s.maxProfit([1, 2, 3, 4, 5]) == 4
    assert s.maxProfit([1, 5, 1, 5, 1, 5]) == 12
    assert s.maxProfit([1, 5, 7, 1, 5]) == 10
    assert s.maxProfit([7, 1, 5, 3, 6, 1]) == 7
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0


if __name__ == "__main__":
    main()
