# 队列的应用
# 传土豆，即：所有人围成一个圈，传递num次，到谁手上谁就出局，最后剩下来的人胜利
# 使用队列：队列头部的代表拿到土豆的，传递完以后就回到队列尾部，传递完num次以后，把队列头部的踢出局，然后如此循环
import random

# from pythonds.basic import Queue
#
# def hot_potato(name_list, num):
#     queue = Queue()
#     for name in name_list:
#         queue.enqueue(name)
#     while queue.size() > 1:
#         for i in range(num):
#             queue.enqueue(queue.dequeue())
#
#         queue.dequeue()  # 出局操作
#     return queue.dequeue()
#
# name_list = ["red", "black", "blue", "yellow"]
# print(hot_potato(name_list, 3))


# # 打印机模拟
# from pythonds.basic import Queue
# import random
# # 打印机对象
# class Printer:
#     def __init__(self, ppm):
#         self.ppm = int(ppm)
#         self.current_task = None
#         self.time_remaining = 0
#     def is_busy(self):
#         if self.current_task == None:
#             return False
#         else:
#             return True
#     def print(self):
#         if self.current_task != None:
#             self.time_remaining -= 1
#             if self.time_remaining <= 0:
#                 self.current_task = None
#
#     def start_new(self, new_task):
#         self.current_task = new_task
#         self.time_remaining = (new_task.get_page() * 60/self.ppm)
# # 任务对象
# class task:
#     def __init__(self, current_time):
#         self.page = random.randint(1, 21)
#         self.timestamp = current_time
#     def get_page(self):
#         return self.page
#     def get_timestamp(self):
#         return self.timestamp
#     def get_waittime(self, current_time):
#         return current_time - self.timestamp
#
# # 是否生成新任务函数
# def new_task():
#     num = random.randint(1,181)
#     if num == 180:
#         return True
#     else:
#         return False
#
# # 模拟程序
# def simulation(totaltime, ppm):
#     queue = Queue()
#     waittime_list = []
#     printer = Printer(ppm)
#     for time in range(totaltime):
#         if new_task():
#             newtask = task(time)
#             queue.enqueue(newtask)
#         if not printer.is_busy() and not queue.isEmpty():
#             nexttask = queue.dequeue()
#             waittime_list.append(nexttask.get_waittime(time))  # 统计这个任务被放入前的等待时间
#             printer.start_new(nexttask)  # 把新任务放入打印机
#
#         printer.print()
#     average_wait = sum(waittime_list)/len(waittime_list)
#     print(f"平均等待时间是：{average_wait:.2f},\t同时还有{queue.size()}个任务未完成")
#
# for i in range(10):
#     simulation(3600, 10)
#








