/*
 * Question 383
 */

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int i = -1;
        for (char c: ransomNote.toCharArray()){
            i = magazine.indexOf(c);
            if (i == -1){
                return false;
            } else {
                magazine = magazine.substring(0, i) + magazine.substring(i + 1);
            }
        }
        return true;
    }
}