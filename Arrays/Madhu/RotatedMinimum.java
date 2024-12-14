// Problem Link - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/?envType=problem-list-v2&envId=array
class Solution {
    public int findMin(int[] nums) {
        int index = 0;
        if (nums[0] >= nums[nums.length-1]) {
            while(index+1 < nums.length && nums[index] <= nums[index+1]) {
                index++;
            }
            if(index+1 < nums.length)
                return nums[index+1];
        } 
        return nums[index];
    }
}
