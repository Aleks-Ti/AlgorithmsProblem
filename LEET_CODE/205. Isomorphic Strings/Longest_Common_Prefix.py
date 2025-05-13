class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map_word: dict[str, list[int]] = {}
        t_map_word: dict[str, list[int]] = {}
        counter_char = 0
        for s, t in zip(s, t):
            if not s_map_word.get(s, False):
                s_map_word[s] = [counter_char]
            else:
                s_map_word[s].append(counter_char)
            if not t_map_word.get(t, False):
                t_map_word[t] = [counter_char]
            else:
                t_map_word[t].append(counter_char)
            counter_char += 1

        for s_indexes, t_indexes in zip(s_map_word.values(), t_map_word.values()):
            if s_indexes != t_indexes:
                return False

        return True

def main():
    s = Solution()
    assert s.isIsomorphic("egg", "add") is True
    assert s.isIsomorphic("foo", "bar") is False
    assert s.isIsomorphic("paper", "title") is True


if __name__ == "__main__":
    main()
