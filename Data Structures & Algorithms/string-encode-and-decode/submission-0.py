class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ''

        for i in strs:
            num = len(i)
            final += str(num)+'#'+i

        return final


    def decode(self, s: str) -> List[str]:
        final = []
        i = 0

        while i < len(s):
            num = ''
            # Read number until '#'
            while s[i] != '#':
                num += s[i]
                i += 1
            i += 1  # skip the '#'

            length = int(num)
            final.append(s[i:i+length])
            i += length  # move pointer to next encoded segment

        return final


