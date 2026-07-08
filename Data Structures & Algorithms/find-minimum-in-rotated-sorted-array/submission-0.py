class Solution:
    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums)-1
        mid = (low+high)//2
        ans = 2**31-1

        while (low<=high):
            if (nums[low]<=nums[mid]):
                ans = min(ans, nums[low])
                low = mid+1
            else:
                ans = min(nums[mid], ans)
                high = mid-1
            mid = (low+high)//2
        
        return ans
        