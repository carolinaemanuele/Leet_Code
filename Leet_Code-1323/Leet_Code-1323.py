'''
Question 1323
'''

class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = [num]
        for i in range(len(str(num))):
            s_num = str(num)
            if s_num[i] == '6':
                s_num = s_num[:i]+'9'+s_num[i+1:]
            else:
                s_num = s_num[:i]+'6'+s_num[i+1:]
            nums.append(int(s_num))
        return max(nums)