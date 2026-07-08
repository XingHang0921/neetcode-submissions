class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        isSeemed = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in isSeemed:
                isSeemed.remove(s[l])
                l += 1
            isSeemed.add(s[r])
            res = max(res, r - l + 1)
        return res