// 剑指 Offer 09. 用两个栈实现队列
// stack1负责插入，stack2负责删除
class CQueue {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;

    public CQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }
    
    public void appendTail(int value) {
        stack1.push(value);
    }
    
    public int deleteHead() {
        if(!stack2.isEmpty()) {
            return stack2.pop();
        } else {
            while (!stack1.isEmpty()) { // 把stack1的数据往stack2压入，负负得正
                stack2.push(stack1.pop()); 
            }
            return stack2.isEmpty() ? -1 : stack2.pop();
        }
    }
}
