'''
Question 1700
'''

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for j in sandwiches:
            if j in students:
                students.remove(j)
            else:
                break
        return len(students)