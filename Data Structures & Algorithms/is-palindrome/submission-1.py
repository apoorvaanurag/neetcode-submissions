import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left = 0
        right = len(cleaned)-1

        if cleaned == ''.join(reversed(cleaned)):
            return True
        else :
            return False


        