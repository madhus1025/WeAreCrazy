'''
https://leetcode.com/problems/combination-sum/
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def recurForCombs(candidates, target, candidates_till_now):
            if target == 0:
                res.append(candidates_till_now)
                return
            
            if target < 0:
                return
            
            for i in range(len(candidates)):
                recurForCombs(candidates[i:], target-candidates[i], candidates_till_now+[candidates[i]])
        
        recurForCombs(candidates, target, [])

        return res