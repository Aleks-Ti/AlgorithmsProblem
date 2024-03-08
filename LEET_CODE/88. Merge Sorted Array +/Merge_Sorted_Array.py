class Solution(object):
    def merge(self, nums1: list, m: int, nums2: list, n: int):
        for _ in range(len(nums1) - m):
            nums1.pop()
        nums1 += nums2
        nums1[:] = sorted(nums1)
        return nums1


def main():
    s = Solution()
    assert s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
    assert s.merge([1], 1, [], 0) == [1]
    assert s.merge([0], 0, [1], 1) == [1]
    assert s.merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3) == [-1, 0, 0, 1, 2, 2, 3, 3, 3]


if __name__ == "__main__":
    main()
