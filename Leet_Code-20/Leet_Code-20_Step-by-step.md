# LeetCode - 20. Valid Parentheses
Solution step by step in python for the question 20. Valid Parentheses of Leet Code.

# Goal
To solve this problem it is necessary to iterate the string *s* in order to detect whether the brackets have ordered pairs.

---

# Step by step
## Step 1: Creation of the variables necessary for analysis
Initially it is necessary to create a list containing the open brackets, named *b_open*, and another containing the close brackets, *b_close*. Furthermore, a list *v* must be created to store the open brackets in the order they appear, an *output* variable to determine the value to be returned by the function and a *wrong_close* variable to evaluate whether a close bracket is in the wrong order.

## Step 2: Iteration over the string *s*
A for repetition structure must be used to access each value in string *s*.

## Step 3: Analysis of the opening and closing order of the brackets
The values are analyzed by a conditional structure:
* If the character is present in the *b_open* list, thus being an open bracket, then it must be added to the *v* list;
* If the character is a close bracket, present in *b_close* list and if there is a previously open bracket, that is, the number of elements of *v* is different from 0, and its last element, `v[-1]`, must be equal to *b_close* element with the same index as the closed bracket being analyzed, `b_open[b_close.index(x)] == v[-1]`, then the last element of the list *v* must be removed, being the open bracket. This indicates that the bracket in question was closed in the correct order;
* However, if none of these conditions are true, we must indicate that the bracket was closed wrongly, assigning the boolean *True* to the variable *wrong_close*. Furthermore, the loop for must be stopped with *break*, because the order of the brackets in the string is not valid.

## Step 4: Validating the order of parentheses
Finally, a conditional structure must be defined to evaluate whether the order of parentheses is valid.
* If the string containing the relatives that were not properly closed is null, `len(v) == 0` and if there is no close bracket in the wrong order, then the output must be equal to *True*, since the order of the parentheses is valid.
* However, if these conditions are not followed, the order of the parentheses will not be valid, therefore the output value must be boolean *False*.

## Step 5: Returning the output value of the function
Finally, the value to be returned by the function is the output variable.

# Analyzing an example

### Let's use this string as an example: `s = "[([]])"`
1. In the **first step**, the variables necessary for analysis are initialized.
2. In the **second step**, this string will be analyzed character by character.
3. Initially, the character *"["* will be analyzed. In the **third step**, in the analysis of the conditional structure, the first condition will be true, since *"["* is contained in the list *b_open*, therefore this character will be added to the list *v*. This will also occur with the characters *"("* and *"["*. 
We then have: `v=["[","(","["]`.
4. When analyzing the character *"]"*, the second condition will be true, since it is present in the list *b_close* and the list *v* contains 3 elements, being `len(v)!=0`. Furthermore, the condition `b_open[b_close.index(x)] == v[-1]`, can be rewritten as: `b_open[1] == v[-1]`, since `b_close.index("]")` returns the value 1, so this condition is true, because *b_open[1]* is *"["*, equal to the last open bracket in the string order. Therefore, as the last bracket was closed correctly, we can use the `v.pop()` command to eliminate it.
5. When analyzing the next element *"]"*, no condition will be met, since it is present in *b_close*, but the next bracket that must be closed is *"("* and not *"["*, being `b_open[1 ] != v[-1]`. Therefore, there is an incorrect closure that must be indicated when passing the boolean value *True* to the *wrong_close* variable. Furthermore, the loop for is broken by the *break* command, since a single error leads to non-validation of parentheses.
6. Moving on to **step 4**, the condition that indicates the evaluation of the validation of parentheses is not met, considering that the list *v* contains two elements, `v=["[","("]`, `len(v)==2`, which correspond to two parentheses which were not closed and the *wrong_close* variable is different from *False*, since there was an incorrect closure. Therefore, the *output* variable must be the boolean *False*. 
7. In **step 5** we return the output variable.

### → Therefore, parsing the string: `s = "[([]])"` with the isValid() function returns the boolean False, indicating that the order of the brackets is not valid.


---
◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪
# Thanks for reading! 😊
◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪◩◪
