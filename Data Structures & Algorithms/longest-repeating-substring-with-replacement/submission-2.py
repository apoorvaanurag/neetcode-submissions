class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # NAIVE APPROACH

        # max_freq_char = 0
        # max_replaceable_len = 0
        
        # for left in range(len(s)):
        #     d = {}
        #     for right in range(left, len(s)):
        #         d[s[right]] = 1 + d.get(s[right],0)

        #         max_freq_char = max(max_freq_char, d[s[right]])

        #         replaceable_len = right-left+1 - max_freq_char

        #         if replaceable_len <= k:
        #             max_replaceable_len = max(max_replaceable_len, right-left+1)
        #         else:
        #             break
        
        # return max_replaceable_len

        # OPTIMAL APPROACH

        max_freq_char = 0
        max_len = 0

        l=0
        r=0
        d = {}

        while r<len(s):
            length = r-l+1
            d[s[r]] = 1+d.get(s[r],0)
            max_freq_char = max(max_freq_char, d[s[r]])

            if length-max_freq_char <= k:
                max_len = max(max_len, length)
                r += 1
            else:
                d[s[l]] -= 1
                l+=1
                r+=1
        
        return max_len



        