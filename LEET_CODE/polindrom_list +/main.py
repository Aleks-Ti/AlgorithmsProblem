class Solution(object):
    def isPalindrome(self, head):
        left = 0
        right = -1
        while True:
            if left > len(head) // 2 or right < -(len(head) // 2):
                if head[left] == head[right]:
                    return True
            if head[left] != head[right]:
                return False
            right -= 1
            left += 1


def main():
    param_1 = [1, 1, 2, 1]
    param_2 = [1, 2, 2, 1]
    res = Solution().isPalindrome(param_1)
    assert res is False
    res = Solution().isPalindrome(param_2)
    assert res is True


if __name__ == "__main__":
    main()
