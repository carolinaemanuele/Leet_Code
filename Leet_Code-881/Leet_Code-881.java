/*
 * Question 881
 */

import java.util.Arrays;
class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int boats = 0;
        int i = 0;
        int n = people.length;

        while (i < n){
            if (i == n-1){
                boats += 1;
                break;
            }
            if (people[i] + people[n-1] <= limit){
                i += 1;
            }
            n -= 1;
            boats += 1;
        }
        return boats;
    }
}