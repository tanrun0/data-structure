# # 找零问题，动态规划
# def find(coins_list, total, min_table, used_table):
#     for small_total in range(1, total+1):
#         coincount = small_total
#         new_coin = 1
#         for coin in [c for c in coins_list if c < small_total]:
#             if min_table[small_total-coin] + 1 < coincount:    # 每一次多次回调后，都会返回一个硬币数，我们就要比较硬币数最小的，也就是最优解
#                 coincount = min_table[small_total-coin] + 1
#                 new_coin = coin
#         min_table[small_total] = coincount
#         used_table[small_total] = new_coin
#     return min_table[total]
#
#
# coins_list = [25,10,5,1]
# total = int(input("请输入你要找零的钱数:"))
# min_table = [0]*(total+1)
# used_table = [0]*(total+1)
#
#
# def Print_num():
#     print(find(coins_list, total, min_table, used_table))
# def Print_every(total, used_table):
#     remainder = total
#     while remainder > 0:
#         this_coin = used_table[remainder]
#         print(this_coin, end=" ")
#         remainder -= this_coin
#     print()
#
# Print_num()
# Print_every(63, used_table)


# 动态规划，博物馆大盗问题

# tr = [None,{'w':2, 'v':3},{'w':3, 'v':4},{'w':4, 'v':8},{'w':5, 'v':8},{'w':9, 'v':10},]  # 第一个元素设为空，用来占位
# w_max = 20
# m = {(i,w):0 for i in range(len(tr)) for w in range(w_max+1)}  # 初始化表格
# for i in range(1, len(tr)):  # 从最简单到最后,把表中每一个空的最优解填上
#     for w in range(1, w_max+1):
#         if tr[i]['w'] > w:
#             m[(i,w)] = m[(i-1,w)]
#         else:
#             m[(i,w)] = max(m[(i-1,w)], m[(i-1,w-tr[i]['w'])] + tr[i]['v'])
# print(m[(len(tr)-1,w_max)])


# 用递归解决博物馆大盗问题
#
# tr = {(2,3), (3,4),(4,8),(5,8),(9,10)}
# w_max = 20
# m = {}
# def vm(tr, w):
#     if tr == set() or w == 0:
#         m[(tuple(tr)), w] = 0
#         return 0
#     elif (tuple(tr),w) in m:
#         return m[(tuple(tr)), w]
#     else:
#         vmax = 0
#         for t in tr:
#             if t[0] <= w:
#                 v = vm(tr-{t}, w-t[0]) + t[1]
#                 vmax = max(vmax,v)
#         m[tuple(tr), w] = vmax
#         return vmax
#
# print(vm(tr,w_max))



# m1 = {(i,w):0 for i in range(5) for w in range(5)}  # 把每个元素设置成（i，w）：0:，其中i和w根据后面的表达式来定
# print(m1)  # 字典（等效的就是一个有上侧和左侧表头的二维表格）
# m2 = {(i,w) for i in range(5) for w in range(5)}  # 把每个元素设置成（i，w），其中i和w根据后面的表达式来定
# print(m2)  # 集合


# 查找和排序
# 有序表的二分查找
# def find(list, item):
#     first = 0
#     last = len(list) - 1
#     while first <= last:
#         mid = (first+last)//2
#         if list[mid] == item:
#             return mid
#         elif list[mid] < item:
#             first = mid +1
#         else:
#             last = mid - 1
#     return False
#
# print(find([1,2,3,4,5,6],4))


# 冒泡排序
# def my_sort1(a_list:list):
#     for i in range(len(a_list)-1,0,-1):
#         for j in range(i):
#             if a_list[j] > a_list[j+1]:
#                 a_list[j], a_list[j+1] = a_list[j+1], a_list[j]

# 适当优化版(判断是否已经排序完了)
# def my_sort2(alist:list):
#     time = len(alist) - 1
#     is_right = False
#     while time > 0 and not is_right:
#         is_right = True
#         for j in range(time):
#             if alist[j] > alist[j + 1]:
#                 is_right = False
#                 alist[j], alist[j+1] = alist[j+1], alist[j]
#         time -= 1
# list = [5,4,3,2,1]
# my_sort2(list)
# print(list)

# 选择排序（在一轮比较结束后，只移动最大/最小的那一个）
# def sel_sort(alist:list):
#     for i in range(len(alist)-1, 0, -1):
#         max_index = i
#         for j in range(0, i):
#             if alist[j] > alist[max_index]:
#                 max_index = j
#         alist[max_index], alist[i] = alist[i], alist[max_index]
#
# list = [5,6,2,7,5,1]
# sel_sort(list)
# print(list)


# 插入排序
# def ins_sort(alist:list):
#     for i in range(1, len(alist)):
#         new_item = alist[i]
#         position = i  # position是指向空位置的
#         while position > 0 and alist[position-1] > new_item:
#             alist[position] = alist[position-1]  # 把比新项大的项后移
#             position -= 1
#         alist[position] = new_item
#
#
# list = [5,4,3,2,1]
# ins_sort(list)
# print(list)

# 希尔排序（分子列->插入排序->缩小间隔->插入排序...直到间隔为1，然后最后一次插入排序）
def shell_sort(alist):
    sub_count = len(alist)//2
    while sub_count > 0:
        for start in range(sub_count):
            sub_insert_soert(alist, start, sub_count)
        sub_count = sub_count // 2

def sub_insert_soert(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        cur_val = alist[i]
        cur_pos = i
        while cur_pos >= gap and alist[cur_pos-gap] > cur_val:  # 确保cur_pos-gap>=0(要能和下标为0的元素比较到)
            alist[cur_pos] = alist[cur_pos-gap]
            cur_pos -= gap
        alist[cur_pos] = cur_val


list = [4,5,3,2,1]
shell_sort(list)
print(list)

