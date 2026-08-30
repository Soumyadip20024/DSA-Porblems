class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int n = nums.length;

        HashMap<Integer, Integer> map = new HashMap<>();

        for(int num: nums){
            map.put(num, map.getOrDefault(num, 0)+1);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>(
            (a,b) -> map.get(b) - map.get(a)
        );
        pq.addAll(map.keySet());

        int i = 0;

        int[] ans = new int[k];

        while(i<k){
            ans[i] = pq.poll();
            i++;
        }
        return ans;
    }
}