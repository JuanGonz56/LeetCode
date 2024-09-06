class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
       
        left, max_window, num_zeros = 0,0,0

        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1

                left += 1
            
            w = right - left + 1

            max_window = max(w, max_window)

        return max_window 

