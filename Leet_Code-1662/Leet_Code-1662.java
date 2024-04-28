/*
 * Question 1662
 */

class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        String w1 = String.join("", word1);
        String w2 = String.join("", word2);
        return w1.equals(w2);
    }
}