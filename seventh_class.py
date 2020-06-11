# ***********************创建和使用类************************

# class Dog():
#     # 构造函数，初始化name, age
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sit(self):
#         print(self.name.title() + "蹲下")

#     def roll_over(self):
#         print(self.name.title() + "打滚")

# my_dog = Dog('豆豆', 3)
# print("dog name is " + my_dog.name + ".")
# print("dog age is " + str(my_dog.age) + ".")

# 创建一个User的类，其中包含“姓”“名”，还有用户基本信息比如VIP级别，
# 性别，身高等！在类User中定义一个describe_user()的方法，打印用户
# 的基本信息！再定义一个greet_user()的方法，向用户发出网站的问候！

# class User():
#     def describe_user(first_name, last_name, level, sex, stature):
#         print(first_name + last_name + level + sex + str(stature))

#     def greet_user():
#         print("Welcome!")

#     describe_user('hel', 'chu', 'VIP', 'man', 159)
#     greet_user()
        
# ***********************创建和使用类************************

class Car():
    #模拟汽车的类，其基本描述信息为厂家，型号，年代
    def __init__(self,make,model,year):
        #初始化描述汽车属性
        self.make=make
        self.model=model
        self.year=year

    def get_descriptive_name(self):
        #返回描述信息
        long_name=str(self.year) + ' ' +self.make + ' '+self.model
        return long_name.title( )

my_new_car = Car('长城','哈费','2019')
print(my_new_car.get_descriptive_name())
