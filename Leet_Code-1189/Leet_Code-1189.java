/*
 * Question 1189
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int maxNumberOfBalloons(String text) {
        List<Character> textList = new ArrayList<>();
        for (char c : text.toCharArray()) {
            textList.add(c);
        }
        List<Integer> counts = new ArrayList<>();
        counts.add(Collections.frequency(textList, 'b'));
        counts.add(Collections.frequency(textList, 'a'));
        counts.add(Collections.frequency(textList, 'l')/2);
        counts.add(Collections.frequency(textList, 'o')/2);
        counts.add(Collections.frequency(textList, 'n'));

        if (counts.contains(0)){
            return 0;
        }
        return Collections.min(counts);
    }
}