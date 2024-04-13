# # 硬币找零
# import time
# total = int(input("请输入你要找的money总数："))
# a = 0
# b = 0
# c = 0
# d = 0
#
# def find(total):
#     for a in range(0,3):
#         if 25*a < total and 25*(a+1) > total:
#             for b in range(0,3):
#                 if b*10 < total-(a*25) and (b+1)*10 > total-(a*25):
#                     for c in range(0,3):
#                         if c*5 < total-(a*25)-(b*10) and (c+1)*5 > total-(a*25)-(b*10):
#                             for d in range(0,10):
#                                 if a*25+b*10+c*5+d*1 == total:
#                                     print(f"总共要找{a}张25元，{b}张10元，{c}张5元，{d}张1元")
#
#

# # 找零问题的递归解决：但是这种算法几乎是试过每一种可能，效率低
# def make_change_1(coins, change):   # 这个change其实也总金额
#     if change in coins:
#         return 1
#     min_coins = float("inf")  # 这个是无穷大的意思，在这里相当于先初始化min_coins
#     # 用列表推导式创建列表,把面值小于的依次循环——尝试
#     for i in [c for c in coins if c <= change]:
#         # 意思就是：当选择了一个面值以后，返回的是1,，减去这个面值，规模减小了，然后再调用自身
#         num_coins = 1 + make_change_1(coins, change-i)  # num_coins记录总硬币数，change-i实际上也是减去这一个面值后的剩余金额
#         min_coins = min(num_coins, min_coins)
#     return min_coins  # 这个对应的是每个面值中的最少数量
#     （不要去深究递推的内部过程，只要知道：每次在对应的面值上取走一个值以后，剩下的金钱还是面对同样的问题）
# print(make_change_1([25,10,5,1], 63))


# 所以下面，提出一种查表法+递归：记录下每一个面值已经找好的最优解，然后让后续的查找是建立在前面最优解的基础上：
def make_change_2(coins, change, record):
    min_coins = change
    if change in coins:
        return 1
    elif record[change] > 0:  # 这个面值对应的record有记录了，代表已经有最优解了
        return record[change]
    else:
        for i in [c for c in coins if c < change]:
            num_coins = 1 + make_change_2(coins, change-i, record)
            min_coins = min(min_coins, num_coins)
            record[change] = min_coins
        return min_coins

print(make_change_2([25,10,5,1], 63, [0]*64))








