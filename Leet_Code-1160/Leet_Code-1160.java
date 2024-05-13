/*
 * Question 1160
 */

class Solution {
    public int countCharacters(String[] words, String chars) {
        int ans = 0;
        for (String w: words){
            int[] charCount = new int[26];
            boolean isGoodWord = true;
            for (char c: chars.toCharArray()){
                charCount[c - 'a']++;
            }
            for (char c: w.toCharArray()){
                if (charCount[c - 'a'] == 0){
                    isGoodWord = false;
                    break;
                }
                charCount[c - 'a']--;
            }
            if (isGoodWord){
                ans += w.length();
            }
        }
        return ans;
    }
}
