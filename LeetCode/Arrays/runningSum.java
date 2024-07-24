

class Solution {
    public static void main(String[] args) {
        // Prints "Hello, World" in the terminal window.
        System.out.println("Hello, World");
        int[] nums = new int[]{1,2,3,4};
        Solution.runningSum(nums);
    }
   
    public static int[] runningSum(int[] nums) {
        int[] result = new int[nums.length];
        result[0] = nums[0];
        
        for(int i = 0; i < nums.length; i++){
            result[i] = nums[i] + result[i-1];
        }
        
        return result;
    }
}