# 栈的应用
# 简单括号匹配
# from pythonds.basic.stack import Stack
# def check(str):
#
#     stack = Stack()
#     balenced = True
#     pos = 0
#     while pos < len(str) and balenced:
#         if str[pos] == '(':
#             stack.push(str[pos])
#         else:
#             if not stack.isEmpty() and str[pos] == ')':
#                 stack.pop()
#         pos += 1
#     if not stack.isEmpty():
#         balenced = False
#     return balenced
#
# str = '(()'
# print(check(str))



# 通用括号匹配 （重点：删去对应的括号）
#
# from pythonds.basic.stack import Stack
# def matches(top, char):
#     s1 = "({[<"
#     s2 = ")}]>"
#     return s1.index(top) == s2.index(char)
# def check(str):
#     balenced = True
#     pos = 0
#     stack = Stack()
#     while pos < len(str) and balenced:
#         if str[pos] in "({[<":
#             stack.push(str[pos])
#         else:
#             if not stack.isEmpty() and str[pos] in ")}]>":
#                 top = stack.pop()
#                 if not matches(top, str[pos]):
#                     balenced = False
#         pos +=1
#     if not stack.isEmpty():
#         balenced = False
#     return balenced
#
# str = "([{}])"
# print(check(str))



# # 十进制代码转换成二进制代码
# from pythonds.basic.stack import Stack
# def devideby2(num):
#     stack = Stack()
#     while num > 0:
#         remember = num%2
#         stack.push(remember)
#         num //= 2
#
#     result = ""
#     while not stack.isEmpty():
#         result = result+str(stack.pop())
#     return result
#
# print(devideby2(42))


# # 转换成不同基数：十进制转十六进制（注意可以创建一个字符串，后通过余数去找到字符串中对应数字）
# from pythonds.basic.stack import Stack
# def dividebybase(num, base):
#     stack = Stack()
#     strbase = "0123456789ABCDEF"
#     while num > 0:
#         remember = num % base
#         stack.push(remember)
#         num //= base
#     result = ""
#     while not stack.isEmpty():
#         result += strbase[stack.pop()]
#     return result
#
# print (dividebybase(15, 10))
# print (dividebybase(15, 2))
# print (dividebybase(15, 16))

# 表达式转换

# from pythonds.basic.stack import Stack
# def change(s1):
#     prior = {}
#     prior["("] = 1
#     prior["*"] = 2
#     prior["/"] = 2
#     prior["//"] = 2
#     prior["+"] = 3
#     prior["-"] = 3
#
#     stack = Stack()
#     tokenlist = list(s1)
#     result = ""
#     for token in tokenlist:
#         if token in "0123456789ABCDEF":
#             result += token
#         elif token =="(":
#             stack.push(token)
#         elif token ==")":
#             top = stack.pop()
#             while top != "(":
#                 result += token
#                 top = stack.pop()
#         else:
#             while (not stack.isEmpty()) and (prior[stack.peek()] <= prior[token]):
#                 result += stack.pop()
#             stack.push(token)
#
#     while not stack.isEmpty():
#         result += stack.pop()
#
#     return result
#
# print(change("1+3*5"))


# 后缀表达式求值
# from pythonds.basic import Stack
#
# def domath (op, op1, op2):
#     result = 0
#     if op == "+":
#         result = op1 + op2
#     if op == "-":
#         result = op1 - op2
#     if op == "*":
#         result = op1 * op2
#     if op == "/":
#         result = op1 / op2
#     if op == "//":
#         result = op1 // op2
#     return result
# def calculate(str):
#     opstack = Stack()
#     str_list = list(str)
#     for ope in str_list:
#         if ope in "0123456789":
#             opstack.push(int(ope))
#         else:
#             op2 = opstack.pop()
#             op1 = opstack.pop()
#             new_op = domath(ope, op1, op2)
#             opstack.push(new_op)
#
#     return opstack.pop()
#
# str = "325*+"
# print(calculate(str))






