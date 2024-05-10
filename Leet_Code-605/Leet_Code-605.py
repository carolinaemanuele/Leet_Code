'''
Question 605
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        p = 0
        while i < len(flowerbed):
            if (i == 0 or flowerbed[i-1] == 0) and flowerbed[i] == 0 and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                p += 1
            elif i == len(flowerbed) and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                p += 1
            i += 1
        return p >= n