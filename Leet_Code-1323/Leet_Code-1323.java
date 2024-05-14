/*
 * Question 1323
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int maximum69Number (int num) {
        List<Integer> nums = new ArrayList();
        nums.add(num);
        String s_num = String.valueOf(num);
        for (int i = 0; i < s_num.length(); i++){
            s_num = String.valueOf(num);
            if (s_num.charAt(i) == '6'){
                s_num = s_num.substring(0,i)+'9'+s_num.substring(i+1);
            } else{
                s_num = s_num.substring(0,i)+'6'+s_num.substring(i+1);
            }
            nums.add(Integer.parseInt(s_num));
        }
        return Collections.max(nums);
    }
}