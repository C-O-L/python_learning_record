print(" 输入分子及分母进行除法运算")
print("输入 'q' 退出.")

while True:
    first_number = input("\n分子: ")
    if first_number == 'q':
        break
    second_number = input("分母: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("分母不能为0")
    else:
        print(answer)
