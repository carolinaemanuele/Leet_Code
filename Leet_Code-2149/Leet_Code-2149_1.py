'''
Question 2149 
'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        output = []
        for x in nums:
            if (x<0):
                negative.append(x)
            else:
                positive.append(x)
        for i in range(0,len(positive)):
            output.append(positive[i])
            output.append(negative[i])
        
        return output