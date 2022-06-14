import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    public int findKthLargest(int[] nums, int k) {

        // PriorityQueue 要熟悉
        PriorityQueue<Integer> queue = new PriorityQueue(new Comparator<Integer>(){
            public int compare(Integer o1, Integer o2) {
                return o1 - o2; // 小顶堆
            }
        });

        for (int i = 0; i < nums.length; i++) {
            queue.add(nums[i]); // 先add的话，因为要保证这个循环出来的size固定
            if (queue.size() > k) {
                queue.poll();
            }
        }

        return queue.peek();
    
    }
}
