/*
 * Question 165
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int compareVersion(String version1, String version2) {
        List<Integer> v1 = intVersion(version1);
        List<Integer> v2 = intVersion(version2);
        int comp = 0;
        for (int i = 0; i < Math.max(v1.size(), v2.size()); i++){
            if (i<v2.size() && i<v1.size()){
                if (v1.get(i) > v2.get(i)){
                    comp = 1;
                    break;
                } else if (v1.get(i)<v2.get(i)){
                    comp = -1;
                    break;
                }
            } else if (i >= v2.size() && v1.get(i)!=0){
                comp = 1;
                break;
            } else if (i >= v1.size() && v2.get(i)!=0){
                comp = -1;
                break;
            }
        }

        return comp;
    }
    public static List<Integer> intVersion (String version) {
        List<String> strVersion = Arrays.asList(version.split("\\."));
        List<Integer> intV = new ArrayList<>();

        for (String s : strVersion) {
            intV.add(Integer.parseInt(s));
        }

        return intV;
    }
}