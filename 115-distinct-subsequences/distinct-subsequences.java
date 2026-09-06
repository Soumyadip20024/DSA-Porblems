class Solution {
    public int numDistinct(String s, String t) {
        int[][] dp = new int[1001][1001];
        for(int i=0; i<dp.length; i++){
            Arrays.fill(dp[i], -1);
        }
        return solve(s, t, 0, 0, dp);
    }
    public int solve(String s, String t, int i, int j, int[][] dp){
        if(j == t.length()){
            return 1;
        }
        if(i == s.length()){
            return 0;
        }
        if(dp[i][j] != -1){
            return dp[i][j];
        }
        if(s.charAt(i) == t.charAt(j)){
            return dp[i][j] = solve(s, t, i+1, j+1, dp) + solve(s, t, i+1, j, dp);
        }
        else{
            return dp[i][j] = solve(s, t, i+1, j, dp);
        }
    }
}