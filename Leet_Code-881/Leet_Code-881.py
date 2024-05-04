'''
Question 881
'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        i, n = 0, len(people)
        while i < n:
            if i == n-1:
                boats += 1
                break
            if people[i] + people[n-1] <= limit:
                i += 1
            n -= 1
            boats += 1
        return boats