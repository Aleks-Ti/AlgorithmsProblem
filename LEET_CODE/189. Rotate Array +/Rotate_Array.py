class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while True:
            if k > len(nums):
                k = k - len(nums)
            else:
                break

        nums[:] = nums[-k:] + nums[:-k]
        return nums


def main():
    s = Solution()

    assert s.rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert s.rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
    assert s.rotate([1, 2], 3) == [2, 1]
    assert s.rotate([1, 2, 3, 4, 5, 6], 11) == [2, 3, 4, 5, 6, 1]


if __name__ == "__main__":
    main()
