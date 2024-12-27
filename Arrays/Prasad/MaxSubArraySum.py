'''
https://leetcode.com/problems/maximum-subarray/
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_till_now, res = float('-inf'), float('-inf')

        for i in range(len(nums)):
            max_till_now = max(max_till_now+nums[i], nums[i])
            res = max(res, max_till_now)
        
        return res