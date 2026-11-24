class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        max_frequency = 0
        max_size = 0
        l = 0

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            if counts[s[r]] > max_frequency:
                max_frequency = counts[s[r]]
            if (r - l + 1) - max_frequency > k:
                counts[s[l]] -= 1
                l += 1
            elif (r - l + 1) > max_size:
                max_size = r - l + 1
        return max_size