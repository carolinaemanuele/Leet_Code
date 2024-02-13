'''
Question 20 - Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        b_open = ['(', '[', '{']
        b_close = [')',']','}']
        v = []
        output = False
        wrong_close = False

        for x in s:
            if x in b_open:
                v.append(x)
            elif (x in b_close) and (len(v)!=0) and (b_open[b_close.index(x)] == v[-1]):
                v.pop()
            else:
                wrong_close = True
                break

        if (len(v)==0) and (wrong_close == False):
            output = True
        else:
            output = False
    
        return output
            

                    