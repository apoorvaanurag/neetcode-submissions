class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # NAIVE APPROACH

        max_freq_char = 0
        max_replaceable_len = 0
        
        for left in range(len(s)):
            d = {}
            for right in range(left, len(s)):
                d[s[right]] = 1 + d.get(s[right],0)

                max_freq_char = max(max_freq_char, d[s[right]])

                replaceable_len = right-left+1 - max_freq_char

                if replaceable_len <= k:
                    max_replaceable_len = max(max_replaceable_len, right-left+1)
                else:
                    break
        
        return max_replaceable_len

        