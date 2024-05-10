/*
Question 605
*/

class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int i = 0;
        int p = 0;
        int l = flowerbed.length;
        while (i <l){
            if ((i==0 || flowerbed[i-1]==0) && flowerbed[i] == 0 && (i == l-1 || flowerbed[i+1] == 0)){
                flowerbed[i] = 1;
                p += 1;
            } else if (i == l-1 && flowerbed[i] == 0 && flowerbed[i-1] == 0){
                p += 1;
            }
            i += 1;
        }
        return p >= n;
    }
}