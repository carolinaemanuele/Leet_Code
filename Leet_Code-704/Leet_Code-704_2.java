/*
 * Question 704
 */

import java.util.Arrays;
class Solution {
    public int search(int[] nums, int target) {
        int i = Arrays.binarySearch(nums, target);
        return (i>=0) ? i: -1;
    }
}