/*
 * Question 1051
 */

import java.util.Arrays;

class Solution {
    public int heightChecker(int[] heights) {
        int[] exp = Arrays.copyOf(heights, heights.length);
        Arrays.sort(exp);
        int w = 0;
        for (int i = 0; i < heights.length; i++){
            if (exp[i] != heights[i]){
                w += 1;
            }
        }
        return w;
    }
}