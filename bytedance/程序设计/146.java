public class LRUCache {
    class DLinkedNode {
        int key;
        int value;
        DLinkedNode prev;
        DLinkedNode next;
        public DLinkedNode() {}
        public DLinkedNode(int key, int value){
            this.key = key;
            this.value = value;
        }
    }

    private Map<Integer, DLinkedNode> cache = new HashMap<Integer, DLinkedNode>();
    private int size;
    private int capacity;
    private DLinkedNode head, tail;

    public LRUCache(int capacity) {
        this.size = 0;
        this. capacity = capacity;
        // 使用伪头节点和伪尾节点
        head = new DLinkedNode();
        tail = new DLinkedNode();
        head.next = tail;
        tail.prev = head;
    }



    public int get(int key) {
        DLinkedNode node = cache.get(key);
        if (node == null){
            return -1;
        }
        // 如果 key 存在，先通过哈希表定位，再移到头部
        moveToHead(node);
        return node.value;
    }

    public void put(int key, int value){
        DLinkedNode node = cache.get(key);
        if (node == null) {
            DLinkedNode newNode = new DLinkedNode(key, value);
            cache.put(key, newNode);
            addToHead(newNode);
            size++; // 不打印，前++和后++没区别

            if (size > capacity){
                DLinkedNode tail = removeTail();
                cache.remove(tail.key);
                size--; 
            }
        } else {
            node.value = value;
            moveToHead(node);
        }
    }


    // region ===== 辅助函数 =====
    private void addToHead(DLinkedNode node){
        // 插入到伪头节点到后面
        node.prev = head; 
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
    } 

    private void removeNode(DLinkedNode node){
        // LRU需要双向链表的原因：删除操作，需要知道前驱
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void moveToHead(DLinkedNode node) {
        removeNode(node);
        addToHead(node);
    }

    private DLinkedNode removeTail(){
        DLinkedNode res = tail.prev;
        removeNode(res);
        return res;
    }
    // endregion ======

}



// 基于LinkedHashMap

class LRUCache {

    private LinkedHashMap map;

    public LRUCache(int capacity) {
        map = new LinkedHashMap()
    }
    
    public int get(int key) {

    }
    
    public void put(int key, int value) {

    }
}
