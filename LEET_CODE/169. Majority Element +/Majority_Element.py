class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        num_dict = {}
        for num in nums:
            if not num_dict.get(num, False):
                num_dict.setdefault(num, 1)
            else:
                num_dict[num] += 1
        max_key = max(num_dict, key=num_dict.get)
        return max_key


def main():
    s = Solution()

    assert s.majorityElement([3, 2, 3]) == 3
    assert s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert s.majorityElement([3, 3, 4]) == 3


if __name__ == "__main__":
    main()
