class Solution:
    def strStr(self, haystack: str, needle: str) -> bool:
        if len(needle) > len(haystack):
            return -1
        pointer = 0
        needle_counter = 0
        saveback = 0
        fix_slices = 0
        while needle_counter <= len(needle) - 1 and pointer <= len(haystack) - 1:
            if needle_counter == len(needle):
                return fix_slices
            if haystack[pointer] == needle[needle_counter]:
                needle_counter += 1
                pointer += 1
            else:
                needle_counter = 0
                pointer, saveback = saveback + 1, saveback + 1
                fix_slices = pointer
        if needle_counter == len(needle):
            return fix_slices
        return -1


def main() -> None:
    assert Solution().strStr("sadbutsad", "sad") == 0
    assert Solution().strStr("leetcode", "leeto") == -1
    assert Solution().strStr("hello", "ll") == 2
    assert Solution().strStr("mississippi", "issip") == 4


if __name__ == "__main__":
    main()
