class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        match_case_s_word: dict[str, int] = {}
        match_case_t_word: dict[str, int] = {}
        for char_1, char_2 in zip(s, t):
            if match_case_s_word.get(char_1):
                match_case_s_word[char_1] += 1
            else:
                match_case_s_word[char_1] = 1
            if match_case_t_word.get(char_2):
                match_case_t_word[char_2] += 1
            else:
                match_case_t_word[char_2] = 1
            
        return match_case_s_word == match_case_t_word



def main():
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") is True
    assert s.isAnagram("rat", "car") is False
    assert s.isAnagram("a", "ab") is False

if __name__ == "__main__":
    main()
