/*
 * Question 2441
 */

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
class Solution {
    public int findMaxK(int[] nums) {
        List<Integer> ord_nums = Arrays.stream(nums).boxed().collect(Collectors.toList());
        Collections.sort(ord_nums, Collections.reverseOrder());
        int max = -1;
        int i = 0;
        while (ord_nums.get(i)>0){
            if (ord_nums.contains(-ord_nums.get(i))){
                max = ord_nums.get(i);
                break;
            }
            if (i == ord_nums.size() - 1){
                break;
            } else{
                i += 1;
            }
        }
        return max;
    }
}