'''
Question 20
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
            

                    