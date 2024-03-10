'''
Question 66
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(-1,-len(digits)-1,-1):
            if (digits[i]==10):
                digits[i] = 0
                if (i==-len(digits)):
                    digits.insert(0, 1)
                else:
                    digits[i-1] += 1
            else:
                break
        return digits