# 归并排序
# def merge_sort(alist):
#     if len(alist) > 1:  # 这个是基本结束条件，必须要有的
#         mid = len(alist)//2
#         left_list = alist[:mid]
#         right_list = alist[mid:]
#         merge_sort(left_list)
#         merge_sort(right_list)
#         # 上面是分块的过程，下面是重新拷贝回原来数组的过程
#         left, right, k = 0,0,0
#         while left < len(left_list) and right < len(right_list):
#             if left_list[left] <= right_list[right]:
#                 alist[k] = left_list[left]
#                 left += 1
#             else:
#                 alist[k] = right_list[right]
#                 right += 1
#             k += 1  # 移动指向数组的下标
#         while left < len(left_list):
#             alist[k] = left_list[left]
#             left += 1
#             k += 1
#         while right < len(right_list):
#             alist[k] = right_list[right]
#             right += 1
#             k += 1
#
# list = [4,5,3,2,1,0]
# merge_sort(list)
# print(list)

# 快速排序
# def quick_sort(alist):
#     quickhelp(alist, 0, len(alist)-1)
#
# def quickhelp(alist, first, last):
#     if first < last:
#         split_point = split(alist, first, last)  # 对整体进行快速排序后，再对左右快速排序（减小了规模，调用自身）
#         quickhelp(alist, first, split_point-1)  # 新的左右序列
#         quickhelp(alist, split_point+1, last)
#
# def split(alist, first, last):  # 其实分裂就是对一部分进行排序
#     mid_val = alist[first]
#     p_first = first+1
#     p_last = last
#     done = False
#     while not done:
#         while p_first <= p_last and alist[p_first] <= mid_val:  # 要考虑所有情况，不要漏了等号
#             p_first += 1
#         while p_first <= p_last and alist[p_last] >= mid_val:
#             p_last -= 1
#         if p_first > p_last:
#             alist[first], alist[p_last] = alist[p_last], alist[first]
#             done = True
#         else:
#             alist[p_first], alist[p_last] = alist[p_last], alist[p_first]
#     return p_last
#
#
# list = [9,7,8,5,3,4,9]
# quick_sort(list)
# print(list)

















