/*
 * Question 1249
 */

import java.util.ArrayList;
class Solution {
    public String minRemoveToMakeValid(String s) {
        ArrayList<Integer> c_open = new ArrayList();
        ArrayList<Integer> c_close = new ArrayList();
        int i = 0;
        int n = s.length();
        while (i < n) {
            if (s.charAt(i) == '(') {
                c_open.add(i);
            } else if (s.charAt(i) == ')') {
                c_close.add(i);
                if (c_close.size() > c_open.size()) {
                    s = s.substring(0,i)+s.substring(i+1,s.length());
                    c_close.remove(c_close.size()-1);
                    n--;
                    i--;
                };
            };
            i++;
        };
        while (c_open.size() > c_close.size()) {
            int c = c_open.get(c_open.size()-1);
            s = s.substring(0,c)+s.substring(c+1,s.length());
            c_open.remove(c_open.size()-1);
        };
        return s;
    }
}