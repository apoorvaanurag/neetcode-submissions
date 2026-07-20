class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # water kya hai? area = min(left, right)*(dist between left and right)
        # left and right pe pointers rakho, dono me se jaha chota element hai, waha se pointer khiskao
        # harr point pe upar wale formule ka max value

        left = 0
        right = len(heights)-1
        ans = 0

        while left<right:
            ans = max(ans, min(heights[left], heights[right])*(right-left))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return ans

        