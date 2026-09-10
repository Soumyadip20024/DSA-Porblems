class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int minprice = Integer.MAX_VALUE;
        int maxprofit = 0;

        for(int i=0; i<n; i++){
            minprice = Math.min(prices[i], minprice);

            int profit = prices[i] - minprice;

            maxprofit = Math.max(maxprofit, profit);
        }
        return maxprofit;
    }
}