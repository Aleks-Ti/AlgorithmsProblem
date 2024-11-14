from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazin_collections = defaultdict(int)
        for char in magazine:
            magazin_collections[char] += 1
        build_detail = defaultdict(int)
        for char in ransomNote:
            build_detail[char] += 1
        for key, value in build_detail.items():
            exists = magazin_collections.get(key)
            if not exists:
                return False
            if value > exists:
                return False
        return True


if __name__ == "__main__":
    assert Solution().canConstruct("a", "b") is False
    assert Solution().canConstruct("aa", "ab") is False
    assert Solution().canConstruct("aa", "aab") is True
