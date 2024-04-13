# 无序表的链表实现
# 可以把指针域（对下一个对象的引用）理解成：像C语言里面一个不能进行加减操作的，但是甚至可以直接表示成值(魔术方法)的指针
class Node:
    def __init__(self, new_data):
        self._data = new_data
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
    def __str__(self):
        return str(self._data)

# 在定义一个无序列表
class UnorderedList:  # 无序列表
    def __init__(self):  # 无序列表需要有一个对表头的引用（即：需要有这个属性）
        self._head = None
    # is_empty方法
    def is_empty(self):
        return self._head is None
    # add方法（我们先规定，把元素都加载列表的头部）
    def add(self, item):  # 注意要先让节点连接上，然后再改变列表头部的引用
        temp = Node(item)
        temp.set_next(self._head)  # 把原来头指针指向的对象赋值给新的指针，新的指针就会指向原来的对象
        self._head = temp  # 使头指针指向新添加的对象

# 移动指针的时候，要注意，当指针已经移动到最后一个None时，再移动就会越界了
    # 使用指针的时候要注意：当指针 is None不能被使用
    # size方法
    def size(self):
        current = self._head  # 拿到头指针
        count = 0
        while current.data is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self._head
        # 注意：这里直接使用current是字符1
        # 但是，使用data要确保current不是None
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        current = self._head
        previous = None
        while current.data != item and current is not None:
            previous = current
            current = current.next
        if current is None:
            raise ValueError(f"{item} is not in the list")
        if previous is None:
            self._head = current.next
        else:
            previous.next = current.next

unorderedlist = UnorderedList()
for i in range(1,10):
    unorderedlist.add(i)
print(unorderedlist.search(1))
unorderedlist.remove(1)
print(unorderedlist.search(1))






# # 什么是数据域，什么是指针域？测试：
# # （py中数据域是直接对数据的应用，即：看上去是赋值数据）
# # （py中指针域存储的是对对下一个对象的引用，即：看上去是赋值对象）
# class Node:
#     def __init__(self, new_data):
#         self._data = new_data
#         self._next = None
#     def get_data(self):
#         return self._data
#     def set_data(self, new_data):
#         self._data = new_data
#     data = property(get_data, set_data)
#     def get_next(self):
#         return self._next
#     def set_next(self, new_next):
#         self._next = new_next
#     next = property(get_next, set_next)
#     # def __str__(self):
#     #     return str(self._data)
#
# class UnorderedList:  # 无序列表
#     def __init__(self):  # 无序列表需要有一个对表头的引用（即：需要有这个属性）
#         self.head = None
#     # is_empty方法
#
#
#     def add(self, item):  # 注意要先让节点连接上，然后再改变列表头部的引用
#         temp = Node(item)
#         temp.set_next(self.head)
#         self.head = temp
#
#
# unorderedlist = UnorderedList()
# for i in range(1,10):
#     unorderedlist.add(i)
#
# head = unorderedlist.head
# print(type(head.data))  # 类型是int
# print(type(head))  # head 是Node类的实例，是对象,是无序列表中第一个对象
# print(type(head.next))  # head,next 也是Node的实例，是对象
# # 没有__str__的时候使用对象
# print(head)  # 是一串地址
# print(head.next)  # 地址
# # 说明其实next存储的就是对下一个对象的引用，python储存的都是引用
# # 当我们使用对象.data可以直接得到数据值
# # 但是在类定义时我们使用了魔术方法，使得我们直接使用对象也可以得到数据值，这样显得我们存储的主要是数据，而next只是对下一个对象的引用





