'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
class Solution:
    def findFirstPosition(nums: List[int], target: int):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                if (mid-1 < 0 or nums[mid-1] != target):
                    return mid
                right=mid-1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        
        return -1

    def findLastPosition(nums: List[int], target: int):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                if (mid+1 >= len(nums) or nums[mid+1] != target):
                    return mid
                left=mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [Solution.findFirstPosition(nums,target), Solution.findLastPosition(nums,target)]