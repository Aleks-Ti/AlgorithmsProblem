class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = 0
        while True:
            if len(nums) == count + 1:
                break
            if nums[count] == nums[count + 1]:
                nums.pop(count)
            else:
                count += 1

        return len(nums), nums


def main():
    s = Solution()
    result = s.removeDuplicates([1, 1, 2])
    assert result[0] == 2
    assert result[1] == [1, 2]

    result = s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    assert result[0] == 5
    assert result[1] == [0, 1, 2, 3, 4]


if __name__ == "__main__":
    main()
