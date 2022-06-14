import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class J692 {

    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.topKFrequent(new String[]{"i", "love", "leetcode", "i", "love", "coding"}, 2);
    }

    public class Solution {

        public List<String> topKFrequent(String[] words, int k) {
            // 1. 哈希表统计频率
            Map<String, Integer> count = new HashMap<>();
            for (String word: words) {
                count.put(word, count.getOrDefault(word, 0) + 1);
            }
    
            // 2. 小根堆  --> 我的卡点
            PriorityQueue<String> minHeap = new PriorityQueue<>((s1, s2)->{
                if(count.get(s1).equals(count.get(s2))) {
                    return s2.compareTo(s1);
                } else {
                    return count.get(s1) - count.get(s2);
                }
            });
    
            // 3.依次加入元素
            for (String s: count.keySet()) {
                minHeap.offer(s);
                // 堆中元素大于k，弹出堆顶最小
                if (minHeap.size() > k) {
                    minHeap.poll();
                }
            }
    
            // 4.依次弹出堆中k个元素，放入集合
            List<String> res = new ArrayList<>(k);
            // 必须poll才有序
            while (minHeap.size() > 0) {
                res.add(minHeap.poll());
            }
    
            // 5.因为刚好是逆序堆需要反转
            Collections.reverse(res);
            return res;
        }
    }
} 
x



