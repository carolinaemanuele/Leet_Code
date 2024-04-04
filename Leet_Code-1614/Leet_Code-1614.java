/*
 * Question 1614
 */

 class Solution {
    public int maxDepth(String s) {
        int max_depth = 0;
        for (int i = 0 ; i < s.length(); i++){
            String sub_s = s.substring(0, i);
            int depth = count(sub_s,'(') - count(sub_s,')');
            if (depth > max_depth){
                max_depth = depth;
            }
        }
        return max_depth;
    }
    public static int count(String s, char c) {
        int cnt = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == c) {
                cnt++;
            }
        }
        return cnt;
    }
}