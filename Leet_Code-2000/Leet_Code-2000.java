/*
 * Question 2000
 */

class Solution {
    public String reversePrefix(String word, char ch) {
        int i = word.indexOf(ch);
        StringBuilder rev_pref = new StringBuilder(word.substring(0,i+1)).reverse();
        String r_prefix = rev_pref.toString();
        word = r_prefix + word.substring(i+1, word.length());
        return word;
    }
}