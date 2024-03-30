/*
 * Question 13
*/

class Solution {
    public int romanToInt(String s) {
        List<Integer> z = new ArrayList();
        int x = 0;
        for (int i = 0; i < s.length(); i++){
            switch (s.charAt(i)) {
                case 'I':
                    z.add(1);
                    break;
                case 'V':
                    z.add(5);
                    break;
                case 'X':
                    z.add(10);
                    break;
                case 'L':
                    z.add(50);
                    break;
                case 'C':
                    z.add(100);
                    break;
                case 'D':
                    z.add(500);
                    break;
                case 'M':
                    z.add(1000);
                    break;
            };
        };

        for (int j = 0; j < z.size(); j++) {
            if (j == z.size()-1){
                x += z.get(j);
            }else if (z.get(j) >= z.get(j+1)){
                x += z.get(j);
            }else{
                x += -(z.get(j));
            }
        };
        return x;
    }
}