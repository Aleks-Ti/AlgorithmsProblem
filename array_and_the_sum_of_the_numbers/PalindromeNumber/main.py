class Solution:
    def isPalindrome(self, head):
        ls_head = [x for x in str(head)]
        count = -1
        for i in ls_head:
            if i == ls_head[count]:
                count -= 1
                continue
            return False
        return True
                    




ret = Solution()
ret.isPalindrome(121)
print(ret)