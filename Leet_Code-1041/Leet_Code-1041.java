/*
 * Question 1041
 */

class Solution {
    public boolean isRobotBounded(String instructions) {
        int[] position = {0,0};
        int[] p = {0,0};
        Map<Integer, int[]> directions = new HashMap<>();
        directions.put(0, new int[]{0,1});
        directions.put(1, new int[]{-1,0});
        directions.put(2, new int[]{0,-1});
        directions.put(3, new int[]{1,0});
        int i = 0;
        for (int n = 0; n <5; n++){
            for(char l : instructions.toCharArray()){
                if (l == 'L' && i<3){
                    i+=1;
                } else if (l == 'L' && i==3){
                    i=0;
                } else if (l == 'R' && i>0){
                    i-=1;
                } else if (l == 'R' && i==0){
                    i=3;
                } else{
                    position[0] += directions.get(i)[0];
                    position[1] += directions.get(i)[1];
                }
            }
            if (Arrays.equals(position,p)){
                return true;
            }
        }
        return false;
    }
}