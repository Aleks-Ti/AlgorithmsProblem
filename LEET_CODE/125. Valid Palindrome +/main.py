class Solution(object):
    def base_exit(self, s):
        if s == "" or s == " ":
            return True
        if len(s) == 1 and s[0].isalpha():
            return True
        elif len(s) == 1 and not s[0].isalpha():
            return True

    def isPalindrome(self, s: str) -> bool:
        if flag := self.base_exit(s):
            return flag
        for char in s:
            if not char.isalnum():
                s = s.replace(char, "")
        if flag := self.base_exit(s):
            return flag

        left = 0
        right = -1
        while True:
            if left >= len(s) // 2 or right < -(len(s) // 2):
                if s[left].lower() == s[right].lower():
                    return True
            if s[left].lower() != s[right].lower():
                return False
            right -= 1
            left += 1


if __name__ == "__main__":
    param_1 = "A man, a plan, a canal: Panama"
    ret = Solution().isPalindrome(param_1)
    assert ret is True
    param_2 = " "
    ret = Solution().isPalindrome(param_2)
    assert ret is True
    param_3 = "0P"
    ret = Solution().isPalindrome(param_3)
    assert ret is False
    param_4 = "a"
    ret = Solution().isPalindrome(param_4)
    assert ret is True
    param_5 = "a."
    ret = Solution().isPalindrome(param_5)
    assert ret is True
    param_6 = "ab@a"
    ret = Solution().isPalindrome(param_6)
    assert ret is True
    param_7 = "."
    ret = Solution().isPalindrome(param_7)
    assert ret is True
    param_8 = ".,"
    ret = Solution().isPalindrome(param_8)
    assert ret is True
    param_9 = "Marge, let's \"[went].\" I await {news} telegram."
    ret = Solution().isPalindrome(param_9)
    assert ret is True
    param_10 = "A man, a plan, a canal -- Panama"
    ret = Solution().isPalindrome(param_10)
    assert ret is True
