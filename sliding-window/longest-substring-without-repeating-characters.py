class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = {}
        max_len = 0
        start = 0
        for i in range(len(s)):
            if s[i] in substring and substring[s[i]] >= start:
                max_len = max(max_len, i - start)
                start = substring[s[i]] + 1
            substring[s[i]] = i
        return max(max_len, len(s) - start)