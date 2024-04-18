/*
 * Question 434
 */

class Solution {
    public int countSegments(String s) {
        int i = 0;
        int c = 0;
        boolean seg = false;
        while (i < s.length()){
            if (s.charAt(i) != ' ' && seg == false){
                seg = true;
            } else if (s.charAt(i) == ' ' && seg == true){
                c++;
                seg = false;
            }
            i++;
        }
        if (seg == true) {
            c++;
        }
        return c;
    }
}