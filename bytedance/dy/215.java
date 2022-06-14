import java.util.Comparator;
import java.util.PriorityQueue;

// 215. 数组中的第K个最大元素


class Solution {

    public int findKthLargest(int[] nums, int k) {
        // PriorityQueue 要熟悉
        Comparator<Integer> compare = new Comparator<Integer>(){
            public int compare(Integer o1, Integer o2) {
                return o1 - o2; // 小顶堆，堆顶最小，留下的是最大的
            }
        };
        PriorityQueue<Integer> queue = new PriorityQueue<Integer>(compare);

        for (int i = 0; i < nums.length; i++) {
            queue.offer(nums[i]);
            if (queue.size() > k) 
                queue.poll();
        }
        return queue.peek();
    }

}