# class Solution():
#     def isPalindrome(head):
#         for j in range(len(head)):
#             for i in range(len(head)):
#                 if str(head[i]) == str(head)[-(j + 1)]:
#                     if str(head[i + 1] == str(head[-(j + 1)])):
#                         return True
                    
#         else:
#             return False


# param_1 = [1, 2, 2, 1]
# ret = Solution.isPalindrome(param_1)
# print(ret)


class Solution(object):
    def isPalindrome(self, head):
        for j in range(len(head)):
            for i in range(len(head)):
                if str(head[i]) == str(head)[-(j + 1)]:
                    try:
                        if str(head[i + 1] == str(head[-(j + 1)])):
                            return True
                    except Exception:
                        pass
        else:
            return False
        
param_1 = [1, 2, 2, 1]
ret = Solution().isPalindrome(param_1)
print(ret)