class Solution:
    def isSubsequence(self, substring: str, target_string: str) -> bool:
        pointer = 0
        substring_counter = 0
        while substring_counter <= len(substring) - 1 and pointer <= len(target_string) - 1:
            if substring_counter == len(substring):
                return True
            if target_string[pointer] == substring[substring_counter]:
                substring_counter += 1
                pointer += 1
            else:
                pointer += 1
        if substring_counter == len(substring):
            return True
        return False


def main() -> None:
    assert Solution().isSubsequence("abc", "ahbgdc") is True
    assert Solution().isSubsequence("axc", "ahbgdc") is False


if __name__ == "__main__":
    main()
