/*
 * Question 412
 */

 import java.util.ArrayList;
import java.util.List;
 class Solution {
     public List<String> fizzBuzz(int n) {
         List<String> answer = new ArrayList<>();
         for (int x = 1; x < n+1; x++){
             if (x%3==0 && x%5==0){
                 answer.add("FizzBuzz");
             } else if (x%3==0){
                 answer.add("Fizz");
             } else if (x%5==0){
                 answer.add("Buzz");
             } else {
                 answer.add(Integer.toString(x));
             };
         };
         return answer;
     }
 }