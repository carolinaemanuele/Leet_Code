# Goal

The objective of this problem is to find the maximum depth that a number has inside parentheses. This can be verified by checking how many parenthetical openings are made to the left of the analyzed element and how many of them are closed, `s[:i].count('(') - s[:i].count(')')`.

---

# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(1)$$ 

---
# Steps
## Step 1: Definition of the variable that will store the result
The first step is to initialize a variable that will store the maximum depth value, *max_depth*.

## Step 2: Create a for loop to traverse sections of the string and determine its depth
The second step is to create a *for loop* that has the variable *i* as a counter for the string indices. Within this loop we define a *depth* variable to determine the depth of each piece of code by counting *'('* to the left of the element at the checked index, `s[:i].count('(')`, subtracted by the count of *')'* to the left of the element, `s[:i].count(')')`. If this value is greater than the value stored in the *max_depth* variable, it will be updated.

## Step 3: Returning the function value
The last step is to return the *max_depth* variable as the function value.

# Code
```
class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        for i in range(len(s)):
            depth = s[:i].count('(') - s[:i].count(')')
            if depth > max_depth:
                max_depth = depth
        return max_depth
```

---
# <span style="color:purple">◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪
# <span style="color:purple">Thanks for reading! 😊 </span>
# <span style="color:purple">◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪ </span>