class Solution:
    def isSubsequence(self, substring: str, target_string: str) -> bool:
        left = 0
        right = 0
        substring_counter = 0
        while right <= len(target_string) - 1:
            if target_string[right] == substring[substring_counter]:
                substring_counter += 1
                right += 1
                if target_string[left:right] == substring:
                    return True
            else:
                right += 1
                left = right
                substring_counter = 0
        if target_string[left:right] == substring:
            return True
        return False


def main() -> None:
    assert Solution().isSubsequence("abc", "ahbgdcabc") is True
    assert Solution().isSubsequence("axc", "ahbgaxcdc") is True


if __name__ == "__main__":
    main()
