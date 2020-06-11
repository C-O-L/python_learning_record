# ********************函数******************************

# def WelcomeUser(name, sex, level):
#     print("欢迎" + name + ", " + sex + ", 等级：" + level)

# WelcomeUser('展昭', '男', 'VIP') 

# ********************函数******************************

# def WelcomeUser(name, sex, level):
#     print("欢迎" + name + ", " + sex + ", 等级：" + level)

# WelcomeUser(sex = '男', name = '展昭', level = 'VIP')

# ********************函数返回值************************

# def get_formatted_name(first_name, last_name):       
#     print("返回全名")
#     full_name = first_name + ' ' + last_name       
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix') 
# print(musician)

# ********************函数返回字典**********************

# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)

# ********************函数结合循环**********************

# def get_formatted_name(first_name,last_name  ):      
#     full_name = first_name + "  " + last_name       
#     return full_name.title()

# active = True
# while active:       
#     print("\nPlease tell me your name:")       
#     f_name = input("First name:")       
#     l_name = input("Last name:")
#     if f_name == 'quit':
#         active = False
#     formatted_name = get_formatted_name(f_name,l_name)       
#     print("\nHello, " + formatted_name + "!")

# ****************函数传递任意数量的实参****************

def make_pizza(*toppings):     
    # """概述要制作的披萨."""     
    print("\n打印顾客要点的所有配料:")     
    for topping in toppings:         
        print("- " + topping) 

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese') 
make_pizza('牛肉', '鸡肉', '羊肉') 
