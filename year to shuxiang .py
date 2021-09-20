def main(a):
    if a == 0:
        print("鼠")
    elif a == 1:
        print("牛")
    elif a== 2:
        print("虎")
    elif a == 3:
        print("兔")
    elif a == 4:
        print("龙")
    elif a == 5:
        print("蛇")
    elif a == 6:
        print("马")
    elif a == 7:
        print("羊")
    elif a == 8:
        print("猴")
    elif a == 9:
        print("鸡")
    elif a == 10:
        print("狗")
    elif a == 11:
        print("猪")
while (1):
    b=input("输入年份")
    a=(int(b)-int(2008))%12
    print(a)
    print(main(a))