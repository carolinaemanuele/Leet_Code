/*
 * Question 506
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
class Solution {
    public String[] findRelativeRanks(int[] score) {
        Integer[] ord = Arrays.stream(score).boxed().toArray(Integer[]::new);
        Arrays.sort(ord, Collections.reverseOrder());
        ArrayList<Integer> order = new ArrayList<>(Arrays.asList(ord));
        int c = 0;
        String[] classification = new String[score.length];
        for (int i = 0; i < score.length; i++) {
            c = order.indexOf(score[i]) + 1;
            switch (c) {
                case 1:
                    classification[i] = "Gold Medal";
                    break;
                case 2:
                    classification[i] = "Silver Medal";
                    break;
                case 3:
                    classification[i] = "Bronze Medal";
                    break;
                default:
                    classification[i] = "" + c;
                    break;
            };
        };
        return classification;
    }
}