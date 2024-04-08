/*
 * Question 1700
 */

import java.util.ArrayList;
class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        ArrayList<Integer> st = new ArrayList<>();
        for (int student : students) {
            st.add(student);
        };
        for (int j: sandwiches) {
            if (st.contains(j)) {
                st.remove((Integer) j);
            } else {
                break;
            };
        };
        return st.size();
    }
}