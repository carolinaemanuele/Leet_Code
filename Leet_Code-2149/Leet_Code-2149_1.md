# Goal
The objective of this question is to order the numbers in the *nums* list according to their signs and their order of appearance. To do this, we must separate the *nums* list into two lists according to the sign of each element and then join them alternately.

# Step by step

## Step 1: Creating the lists
Initially it is necessary to create an empty list that will be filled with positive values, the *positive* list, and one for negative values, the *negative* list. Another list must also be created to join them at the end, the *output* list.

## Step 2: Completing the lists
A *for* loop must be created to go through each number in the *nums* list. If the element in question is negative, *x<0*, it will be added to the *negative* list via the *append* command. On the other hand, if it is positive it will be added to the *positive* list.

## Step 3: Merging the lists
Later, another *for* loop must be created to create an index within the range of 0 to the length of the *positive* list, which is equal to the length of the *negative* list. In the *output* list, the corresponding index value from the *positive* list will be added first to the *output* list, and then the corresponding index value  from the *negative* list will be added. This way the numbers will be organized so that the first number in *output* list is positive, the next negative and the rest interspersed.

## Step 4: Returning the function value
At the end, the *output* list must be returned as the function value.

# Code
```
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Step 1
        positive = []
        negative = []
        output = []
        # Step 2
        for x in nums:
            if (x<0):
                negative.append(x)
            else:
                positive.append(x)
        # Step 3
        for i in range(0,len(positive)):
            output.append(positive[i])
            output.append(negative[i])
        # Step 4
        return output

```
# Analyzing an example

## Let's use the following list as an example: `nums = [3,1,-2,-5,2,-4]`
1. In the **first step**, the lists necessary for sorting are created.
2. In the **second step** the numbers will be analyzed individually so that:
- The number 3 is not negative, 3>0, therefore the *else* command will be executed. Therefore, it will be added to the *positive* list. The same goes for the next number, 1.
- The number -2 obeys the if condition, -2<0, therefore it will be added to the *negative* list, as will the next number, -5.
- Following this logic, the last numbers 2 and -4 will be added to the *positive* list and the *negative* list, respectively.

This way, `positive = [3,1,2]` and `negative = [-2,-5,-4]`.

3. In the **third step**, according to the range defined for the index *i* from 0 to 2, we have:
- i = 0: The value of *positive* list at index 0, `positive[0]`, and subsequently, the value of *negative* list at index 0, `negative[0]`, will be added to the *output* list. At the end of this first step `output = [3,-2]`.
- i = 1: The value of `positive[1]` first and then `negative[1]` will be added to the *output* list. Thus, `output = [3,-2,1,-5]`.
- i = 2: The values of `positive[2]` and `negative[2]`, respectively, will be added, and then `output = [3,-2,1,-5,2,-4]`.

So at the end of the for loop: `output = [3,-2,1,-5,2,-4]`.

4. In the **fourth step** the *output* list will be returned as the value of the *rearrangeArray()* function.
→ Thus, rearranging the array `nums = [3,1,-2,-5,2,-4]` according to the order established by the question, we will have the array as a result: `[3,-2,1,-5 ,2,-4]`.

---
# ◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪

# Thanks for reading! 😊
# ◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪