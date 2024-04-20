/*
 * Question 128
 */

import java.util.*;
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set_nums = new HashSet<>();
        for (int num : nums) {
            set_nums.add(num);
        }
        ArrayList<Integer> nums_ord = new ArrayList<>(set_nums);
        Collections.sort(nums_ord);
        ArrayList<Integer> consts = new ArrayList<>();
        if (nums_ord.size() >= 1){
            consts.add(1);
        } else {
            consts.add(0);
        }
        int cons = 1;

        for(int i = 1; i < nums_ord.size(); i++) {
            if (nums_ord.get(i) == nums_ord.get(i-1) + 1) {
                cons += 1;
            } else{
                consts.add(cons);
                cons = 1;
            }
            if (i == nums_ord.size()-1){
                consts.add(cons);
            }
        }
        return Collections.max(consts);
    }
}