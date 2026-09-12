class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int n = nums.length;
        int total = 0;

        int currMax= 0;
        int max = Integer.MIN_VALUE;

        int currMin = 0;
        int min = Integer.MAX_VALUE;

        for(int i=0; i<n; i++){
            currMax += nums[i];

            if(currMax > max){
                max = currMax;
            }
            if(currMax < 0){
                currMax = 0;
            }
            currMin += nums[i];

            if(currMin < min){
                min = currMin;
            }
            if(currMin > 0){
                currMin = 0;
            } 
            total += nums[i];
        }
        if(max < 0){
            return max;
        }
        return Math.max(max, (total - min));

    }
}