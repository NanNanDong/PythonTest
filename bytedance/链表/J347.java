import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {

    public class Bucket {
        int val;
        int freq;

        public Bucket(int val, int freq) {
            this.val = val;
            this.freq = freq;
        }
    }

    public int[] topKFrequent(int[] nums, int k) {
        // 预处理
        Map<Integer, Integer> freq = new HashMap<>(nums.length);

        for(int i = 0;  i < nums.length; i++) {
            freq.put(nums[i], freq.getOrDefault(nums[i], 0) + 1);
        }

        List<Bucket> list = new ArrayList<>(freq.size());

        Iterator<Map.Entry<Integer, Integer>> it = freq.entrySet().iterator();

        while(it.hasNext()) {
            Map.Entry<Integer, Integer> entry = it.next();
            list.add(new Bucket(entry.getKey(), entry.getValue()));
        }


        // 构造小顶堆
        PriorityQueue<Bucket> queue = new PriorityQueue<>(new Comparator<Bucket>(){
            public int compare(Bucket b1, Bucket b2){
                return b1.freq - b2.freq;
            }
        });

        for (int i = 0; i < list.size(); i++) {
            queue.add(list.get(i));
            if (queue.size() > k) {
                queue.poll();
            }
        }

        int[] res = new int[queue.size()];
        for (int i = 0 ; i < res.length; i++) {
            res[i] = queue.poll().val;
        }

        return res;
    }
}