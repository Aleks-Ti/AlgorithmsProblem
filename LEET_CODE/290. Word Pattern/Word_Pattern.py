class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(list_word := s.split()):
            return False
        match_case_pattern: dict[str, str] = {}
        match_case_s: dict[str, str] = {}
        for char_pattern, word in zip(pattern, list_word):
            if match_case_pattern.get(char_pattern) and match_case_pattern[char_pattern] != word:
                return False
            if match_case_s.get(word) and match_case_s[word] != char_pattern:
                return False
            match_case_pattern[char_pattern] = word
            match_case_s[word] = char_pattern
        return True




def main():
    s = Solution()
    assert s.wordPattern("abba", "dog cat cat dog") is True
    assert s.wordPattern("abba", "dog cat cat fish") is False
    assert s.wordPattern("aaaa", "dog cat cat dog") is False
    assert s.wordPattern("abba", "dog dog dog dog") is False
    assert s.wordPattern("aaa", "aa aa aa aa") is False


if __name__ == "__main__":
    main()
