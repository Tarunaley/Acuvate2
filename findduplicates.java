import java.util.*;
class Solution {
    public int findDuplicate(int[] nums) {
        HashSet<Integer> numSet = new HashSet<>();
        int dup = 0;

        for(int x : nums){
            if(numSet.contains(x)){
                dup = x;
                break;
            }
            numSet.add(x);

            
            
        }
        return dup;



        
    }
}