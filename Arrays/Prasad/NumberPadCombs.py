'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
class Solution:
    dialpad = {
        '2': ['a', 'b', 'c'], 
        '3': ['d', 'e', 'f'], 
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'], 
        '8': ['t', 'u', 'v'], 
        '9': ['w', 'x', 'y', 'z']
    }
    result = []

    def recurForCombs(self, digits, seq):
        if len(digits) < 1:
            Solution.result.append(seq)
            return
        
        digit = digits[0]  # Get the first digit from the string

        # Loop through the characters mapped to this digit
        for char in Solution.dialpad[digit]:  # Use `digit` here, not `char`
            self.recurForCombs(digits[1:], seq + char)  # Pass the remaining digits and updated sequence

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []  # Handle edge case where input is empty
        
        Solution.result = []  # Reset the result list for a fresh call
        self.recurForCombs(digits, '')
        return Solution.result
