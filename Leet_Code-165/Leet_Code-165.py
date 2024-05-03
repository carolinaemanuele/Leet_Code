'''
Question 165
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        comp = 0
        for i in range(max(len(v1), len(v2))):
            if i < len(v2) and i < len(v1):
                if v1[i]>v2[i]:
                    comp = 1
                    break
                elif v1[i]<v2[i]:
                    comp = -1
                    break
            elif i >= len(v2) and v1[i]!=0:
                comp = 1
                break
            elif i >= len(v1) and v2[i]!=0:
                comp = -1
                break
        return comp