# # 递归算法，转换进制
# def change(num, base):
#     table = "0123456789ABCDEF"
#     if num < base:  # 基本结束条件
#         return table[num]
#     else:
#         return change(num // base, base) + table[num % base]  # 调用自身，向更小规模演进
#
# print(change(10, 16 ))


#
# # 递归，调用自身，画螺线
# import turtle
# t = turtle.Turtle()
# def draw(t, len):
#     if len > 0:
#         t.forward(len)
#         t.right(90)
#         return draw(t, len - 5)
#
# draw(t, 100)
# turtle.done()


#
# # 用递归实现画树
# import turtle
#
# def tree(len):
#     if len>5:  # 基本条件
#         t.forward(len)
#         t.right(20)   # 向前走完以后，右转，这个时候方向定了，又相当于：以这个“根节点”，再画一个二叉树（实现了演进）
#         tree(len-15)  # 这个就把右边给画完了
#         t.left(40)   # 当上面的执行完，回到这一步时，还是在原来那一层，然后开始转到左边，以左边为“根节点”，又开始画树
#         tree(len-15) # 把左边的画完
#         # 当每次一右边的小树画完以后，需要退回到上一颗大树的根，再开始画左边的小树，确保左右两边是一个根
#         t.right(20)  # 把笔摆正
#         t.backward(len)  # 后退，返回原来的位置
#
# t = turtle.Turtle()
# t.left(90)  # 让笔向上
# t.penup()
# t.backward(100)  # 让笔回退一点，在屏幕的下面
# t.pendown()
# t.color("green")
# t.pensize(2)
# tree(75)
# t.hideturtle()
# turtle.done()


# # 绘制诺尔宾斯三角形
# import turtle
# import math
# t = turtle.Turtle()
# points = {"left":(-200,-100), "right": (200, -100), "top":(0, 200*math.sqrt(3)-100)}
# def DrawTriangle(points, color):
#     t.fillcolor(color)
#     t.penup()
#     t.goto(points["top"])
#     t.pendown()
#     t.begin_fill()
#     t.goto(points["left"])
#     t.goto(points["right"])
#     t.goto(points["top"])
#     t.end_fill()
#
# def GetMid(p1, p2):
#     return ((p1[0] + p2[0])/2 , (p1[1] + p2[1])/2)
#
# # 因为要画三个三角形，所以可以递归调用三次，每次都把新的坐标传入
# def DeDraw(count, points):
#     colormap = ["red", "yellow", "blue", "green", "white", "black"]
#     DrawTriangle(points, colormap[count])
#     if count > 0:   # 这个count是传递的，越往内，count就是越小
#         DeDraw(count - 1, points = {"left":points["left"],
#                                     "top":GetMid(points["left"], points["top"]),
#                                     "right":GetMid(points["left"], points["right"])})
#         DeDraw(count - 1, points = {"top":points["top"],
#                                     "left":GetMid(points["left"], points["top"]),
#                                     "right":GetMid(points["top"], points["right"])})
#         DeDraw(count - 1, points = {"right":points["right"],
#                                     "left":GetMid(points["left"], points["right"]),
#                                     "top":GetMid(points["top"], points["right"])})
#
# DeDraw(2, points)
#

# # 递归实现汉罗塔
# def moveTower(n, fromPole, withPole, toPole):
#     if n == 1:
#         DiskTower(n, fromPole, toPole)
#     else:
#         # 对于上面的n-1，我们是要把它移动到with柱，具体怎么移动的不管，但是都是多个，所以也是利用这个函数移动（这时候，开始，中间，和目标柱就不一样了）
#         moveTower(n-1, fromPole, toPole, withPole)
#         # 这一步就可以把最后一个盘子直接移过去了
#         DiskTower(n, fromPole, toPole)
#         moveTower(n-1, withPole, fromPole, toPole)
#
#
# def DiskTower(disk, fromPole, toPole):
#     print(f"移动第{disk}个盘, 从{fromPole} 到 {toPole}")
#
# moveTower(3, "开始柱", "过渡柱", "目标柱")




















