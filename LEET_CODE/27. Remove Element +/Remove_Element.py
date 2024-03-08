class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        while True:
            if len(nums) == count:
                break
            if nums[count] == val:
                nums.pop(count)
            else:
                count += 1

        return len(nums), nums


def main():
    s = Solution()
    assert s.removeElement([3, 2, 2, 3], 3)[0] == 2
    assert s.removeElement([3, 2, 2, 3], 3)[1] == [2, 2]

    assert s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)[0] == 5
    assert sorted(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)[1]) == sorted([0, 1, 4, 0, 3])


if __name__ == "__main__":
    main()
