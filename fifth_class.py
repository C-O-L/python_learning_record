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

# /////////////////////////////////////////////////////////////////

# #创建一个待验证的列表
# #创建一个用来存储验证用户的列表

# unconfirmed_users = ['zhangsna','lisi','wangmazi']
# confirmed_users = []

# #验证用户
# #把每个验证过的用户移动到已验证用户列表

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("您已经被验证了" + current_user)

#     #将验证过的用户移动到confirmed_users表中
#     confirmed_users.append(current_user)

# #显示所有已验证用户
# print("\n验证过的用户: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user)

# /////////////////////////////////////////////////////////////////

# #建立一空字典
# responses = {}

# #设置一个标志，指出调查是否继续
# flag = True
# while flag:
#     #提示被调查者的名字和回答
#     name = input("\n请输入姓名： ")
#     response = input("想去哪里旅游?  ")

#     #将输入结果存储到字典中
#     responses[name] = response

#     #看还有用户要被调查吗!
#     repeat = input("还有没有用户要参加调查? (yes/no)： ")
#     if repeat == 'no' :
#         flag = False

# #调查结束，打印
# print("-----调查结果---")
# for name, response in responses.items():
#     print(name + "想去" + response + "旅游")

# /////////////////////////////////////////////////////////////////

# def greet_user(): 	      
#     print("欢迎来到美丽的沙漠水城《中卫》")
# 	print("中卫历史悠久，有两千多年的历史")
# 	print("中卫的特色小吃很多，来了不要忘了吃点蒿子面")

# /////////////////////////////////////////////////////////////////

# #实参与形参实例

# def describe_pet(animal_type,sex, pet_name):

#     # """显示宠物的信息"""
#     print("\n 你家的宠物的类型是：" + animal_type)
#     print("\n 你家的宠物是公的还是母的：" + sex)
#     print("\n 你家的宠物的名字：" + pet_name)

# #位置实参
# describe_pet ('狗','公','jk')

# #关键字实参
# describe_pet(pet_name = 'gh', animal_type = '山羊', sex = '母')

# /////////////////////////////////////////////////////////////////

def get_formatted_name(first_name,last_name):
   full_name= first_name + ' ' + last_name    
   return full_name.title() 
   musician = get_formatted_name('jimi', 'hendrix')
print(musician)