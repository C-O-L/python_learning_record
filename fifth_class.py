# height = input("请输入身高：");
# if int(height) >= 36:
#     print("满足条件");
# else:
#     print("不满足")

# *****************************************************************

# # 编写一个程序,输入一个数字,打印1至该数字一共有多少个奇数!

# num = input("input number:")
# j = 0
# for i in range(1, int(num)):      #遍历1~num
#     if i % 2 != 0:
#         j += 1                    #有一个奇数j+1
#         print(i)
# print("1至" + num + "共有" + str(j) + "个奇数")

# *****************************************************************

# while语句

# active = True
# while active:
#     message = input()
#     if message == 'quit':
#         active = False               #当message=='quit'时退出程序
#     else:
#         print(message)

# /////////////////////////////////////////////////////////////////

# while True:
#     city = input()
#     if city == 'nx':
#         break
#     else:
#         print("city is " + city +".")

# /////////////////////////////////////////////////////////////////

#打印1--max_number之间的奇数

# current_number = 0
# max_number=input("请输入任意数字,打印其中的奇数: ")
# while current_number < int(max_number):
#     current_number += 1
#     if current_number % 2 == 0:        #如果是偶数
#         continue                       #跳出本次循环
#     print(current_number)              #否则打印current_number

# /////////////////////////////////////////////////////////////////

# 有一网站根据用户级别赠送618的代金卷,级别为level1--level3的用户赠送20
# 元,级别未level4-level6的用户赠送40元,level6以上的用户赠送80元,请编写
# 一循环,询问用户级别,并打印其能获得多少钱的代金卷!

# active = True
# while active:
#     level = input("输入用户等级：")
#     if int(level) < 4:
#         print("送20元")
#     elif int(level) > 3 and int(level) < 7:
#         print("送40元")
#     elif int(level) > 6:
#         print("送80元")
#     elif level == 'quit':
#         active = False