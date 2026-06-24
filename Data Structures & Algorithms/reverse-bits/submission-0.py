class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            # 1. Shift the result left to make room for the incoming bit
            result <<= 1
            
            # 2. Extract the rightmost bit of n and add it to the result
            result |= (n & 1)
            
            # 3. Shift n right to bring the next bit into focus
            n >>= 1
        
        return result
        