# 实现有序列表
class Node:
    def __init__(self, node_data):
        self._data = node_data
        self._next = None
    def get_data(self):
        return self._data
    def set_data(self, new_data):
        self._data = new_data
    data = property(get_data, set_data)
    def get_next(self):
        return self._next
    def set_next(self, new_next):
        self._next = new_next
    next = property(get_next, set_next)
    def __str__(self):  # 要返回一个可以转换成字符串的对象
        return str(self._data)

class OrderedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False
    def add(self, item):
        current = self.head
        previous = None
        node = Node(item)
        stop = False
        while current is not None and not stop:
            if item < current.data:
                stop = True
            else:
                previous = current
                current = current.next
        if previous is None:
            node.set_next(self.head)
            self.head = node
        elif current is None:
            previous.next = node
        else:
            node.next = current
            previous.next = next
    def remove(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.data == item:
                stop = True
            elif item > current.data:
                raise ValueError(f"{item} is not in the list")
            else:
                previous = current
                current = current.next
        if current is None:
            raise ValueError(f"{item} is not in the list")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next


orderedlist = OrderedList()
for i in range(1,10):
    orderedlist.add(i)
print(orderedlist.size())
print(orderedlist.search(1))
orderedlist.remove(1)
print(orderedlist.size())
print(orderedlist.search(1))