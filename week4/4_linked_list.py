# 首先创建一个结点类,里面包含数据元素和指向下一个数据元素的指针
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


# 然后创建一个单链表的类
class SingleLinkedList(object):

    """创建一个单链表"""

    def __init__(self):
        self.head = None

    """判断链表是否为空"""

    def judge(self):
        return self.head is None

    """获取链表的长度"""

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    """在链表的头部添加元素"""

    def add_first(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    """在链表的尾部添加元素"""

    def add_last(self, data):
        node = Node(data)
        if self.judge():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    """在指定位置添加元素"""

    def insert_node(self, index, data):
        node = Node(data)
        if index < 0 or index > self.length():
            return False
        elif index == 0:
            self.add_first()
        elif index == self.length():
            self.add_last()
        else:
            cur = self.head
            count = 0
            while count < index - 1:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    """删除指定结点"""

    def remove_node(self, data):
        cur = self.head  # 当前结点
        pre = None  # 当前结点的前一个
        if self.head.data == data:
            self.head.next = self.head
        else:
            while cur.data is not data:
                pre = cur
                cur = cur.next
            pre.next = cur.next

    """查找指定结点是否存在"""

    def search(self, data):
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        return False

    """改变指定结点的值"""

    def change(self, index, data):
        node = Node(data)
        if index < 0 or index > self.length():
            return False
        elif index == 0:
            node.next = self.head.next
            self.head = node
        else:
            count = 0
            cur = self.head
            pre = None
            while count < index:
                pre = cur
                cur = cur.next
                count += 1
            node.next = cur.next
            pre.next = node

    """遍历整个链表"""

    def traversal(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


if __name__ == "__main__":
    lists = SingleLinkedList()
    lists.add_first(2)
    lists.add_first(1)
    lists.add_last(4)
    lists.insert_node(2, 3)
    lists.change(1, 5)
    lists.traversal()
    print(lists.judge())
    print(lists.length())
    lists.remove_node(4)
    print(lists.search(3))
    lists.traversal()
