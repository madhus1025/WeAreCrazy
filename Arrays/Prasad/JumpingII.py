'''
https://leetcode.com/problems/jump-game-ii
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = [0]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            if (nums[i]+i) >= len(nums) - 1: 
                min_jumps[i] = 1
            elif (nums[i] == 0):
                min_jumps[i] = float('inf')
            else:
                min_jumps[i] = min(min_jumps[i+1:nums[i]+i+1]) + 1

        return min_jumps[0]