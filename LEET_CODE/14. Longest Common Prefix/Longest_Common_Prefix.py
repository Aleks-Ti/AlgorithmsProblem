class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix: str = strs[0]
        all_count_word = len(strs) - 1
        counter = 1
        while counter <= all_count_word:
            if prefix == "":
                break
            
            if prefix != strs[counter][:len(prefix)]:
                prefix = prefix[:-1]
            else:
                counter += 1

        return prefix

def main():
    s = Solution()
    assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert s.longestCommonPrefix(["dog","racecar","car"]) == ""


if __name__ == "__main__":
    main()
