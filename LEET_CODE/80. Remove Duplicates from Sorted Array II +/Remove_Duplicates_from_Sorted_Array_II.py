class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        remove_num = {}
        count = 0
        while True:
            if len(nums) == count + 1:
                break
            if nums[count] == nums[count + 1]:
                if not remove_num.get(nums[count], False):
                    remove_num.setdefault(nums[count], 1)
                if remove_num.get(nums[count], False) and remove_num[nums[count]] == 1:
                    remove_num[nums[count]] += 1
                    count += 1
                    continue
                else:
                    nums.pop(count)
            else:
                count += 1

        return len(nums), nums


def main():
    s = Solution()
    result = s.removeDuplicates([1, 1, 1, 2, 2, 3])
    assert result[0] == 5
    assert result[1] == [1, 1, 2, 2, 3]

    result = s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])
    assert result[0] == 7
    assert result[1] == [0, 0, 1, 1, 2, 3, 3]


if __name__ == "__main__":
    main()
