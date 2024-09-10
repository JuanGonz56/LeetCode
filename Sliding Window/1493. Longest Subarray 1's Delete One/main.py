class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, zero_count, res = 0,0,0
        #for loop begins with right 
        for right in range(len(nums)):
            #increases the zero count if right element == 0
            zero_count += 1 if nums[right] == 0 else 0
            #this while loop makes sure that there are no zero's in window 
            while zero_count > 1:
                zero_count -= 1 if nums[left] == 0 else 0
                left += 1
            #returns the max len of subarray found. no + 1 after r-l because we need to delete 1 element 
            res = max(res, right - left)

        return res