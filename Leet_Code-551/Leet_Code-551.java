/*
 * Question 551
 */

class Solution {
    public boolean checkRecord(String s) {
        if (s.contains("LLL") || s.chars().filter(ch -> ch == 'A').count() >=2){
            return false;
        }
        return true;
    }
}