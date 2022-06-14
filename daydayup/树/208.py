# 208. 实现 Trie (前缀树)

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]: # 子节点不存在，创建一个新的节点
                node.children[ch] = Trie()
            node = node.children[ch] # 移动到下一个节点
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]: # 子节点不存在，说明不包含前缀
                return None
            node = node.children[ch] # 继续搜索
        return node

