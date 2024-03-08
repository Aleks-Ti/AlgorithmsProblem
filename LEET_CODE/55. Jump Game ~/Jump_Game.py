class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True

        reachable = nums[0]

        for i in range(1, len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])
            if i == len(nums) - 1:
                return True

        return False


def main():
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4]) is True
    assert s.canJump([2, 5, 0, 0]) is True
    assert s.canJump([1, 0, 1, 0]) is False
    assert s.canJump([1, 2, 3]) is True
    assert s.canJump([2, 3, 1, 1, 4]) is True
    assert s.canJump([3, 2, 1, 0, 4]) is False
    assert s.canJump([0]) is True
    assert s.canJump([1, 2]) is True
    assert s.canJump([2, 0, 0]) is True
    assert s.canJump([2, 0, 2]) is True


if __name__ == "__main__":
    main()
