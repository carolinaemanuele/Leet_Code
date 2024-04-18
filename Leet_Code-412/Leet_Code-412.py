'''
Question 412
'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for x in range(1,n+1):
            if x % 3 == 0 and x % 5 == 0:
                answer.append('FizzBuzz')
            elif x % 3 == 0:
                answer.append('Fizz')
            elif x % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(str(x))
        return answer