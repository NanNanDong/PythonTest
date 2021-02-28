// 460. LFU 缓存 --> 困难
// 删除时间戳最小的，所以插入有讲究
 class Node {
    int key, val, freq;

    Node(int key, int val, int freq) {
        this.key = key;
        this.val = val;
        this.freq = freq;
    }
}
class LFUCache {

    int minfreq, capacity;
    Map<Integer, Node> keyTable;
    Map<Integer, LinkedList<Node>> freqTable; // 频率map,链地址法

    public LFUCache(int capacity) {
        this.minfreq = 0
        this.capacity = capacity;
        keyTable = new HashTable<Integer, Node>();
        freqTable = new HashTable<Integer, LinkedList<Node>>();
    }
    
    public int get(int key) {
        if (capacity == 0){
            return -1;
        }
        if (!keyTable.containsKey(key)) {
            return -1;
        }
        Node node = keyTable.get(key);
        int val = node.val, freq = node.freq;

        freqTable.get(freq).remove(node);



    }
    
    public void put(int key, int value) {

    }
}
