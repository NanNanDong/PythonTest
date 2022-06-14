// 设计Set

// https://leetcode-cn.com/problems/design-hashset/solution/yi-ti-san-jie-jian-dan-shu-zu-lian-biao-nj3dg/
import java.util.Iterator;
import java.util.LinkedList;

// 链地址法
class MyHashSet {

    private static final int BASE = 769;
    private LinkedList[] data;


    /** Initialize your data structure here. */
    public MyHashSet() {
        data = new LinkedList[BASE];

        for (int i = 0; i < BASE; ++i){
            data[i] = new LinkedList<Integer>();
        }
    }

    public void add(int key) {
        int h = hash(key);
        // 判断是否已经存在
        Iterator<Integer> it = data[h].iterator();
        while(it.hasNext()) {
            Integer e = it.next();
            if (e == key) {
                return;
            }
        }

        data[h].addFirst(key); // 头插法
    }

    public void remove(int key) {
        int h = hash(key);
        Iterator<Integer> it = data[h].iterator();
        while(it.hasNext()) {
            Integer e = it.next();
            if (e == key) {
                data[h].remove(e);
                return;
            }
        }
    }

    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        int h = hash(key);
        Iterator<Integer> it = data[h].iterator();
        while(it.hasNext()) {
            Integer e = it.next();
            if (e == key) {
                return true;
            }
        }
        return false;
    }


    private int hash(int key) {
        return key % BASE;
    }


}