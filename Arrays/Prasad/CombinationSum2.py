'''
https://leetcode.com/problems/combination-sum-ii/
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def recurForCombs(candidates, target, index, candidates_till_now, result):
            if target == 0:
                result.append(candidates_till_now)
                return
            
            if target < 0:
                return
            
            for i in range(index, len(candidates)):
                if (i > index and candidates[i] == candidates[i-1]):
                    continue
                values_till_now = candidates_till_now + [candidates[i]]
                recurForCombs(candidates, target-candidates[i], i+1, values_till_now, result)
        
        recurForCombs(candidates, target, 0, [], res)

        return res