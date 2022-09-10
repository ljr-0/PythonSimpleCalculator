import math
print("计算器")
print("例子：")
print("5")
print("+")
print("3")
print("要打根号，输入r或√(按住Alt,依次按小键盘41420)")
while True:
    a=float(input())
    t=input()
    b=float(input())
    if t=="+":
        print(a,t,b,"=",a+b)
    elif t=="-":
        print(a,t,b,"=",a-b)
    elif t=="*":
        print(a,t,b,"=",a*b)
    elif t=="/":
        print(a,t,b,"=",a/b)
    elif t=="^":
        print(a,t,b,"=",float(pow(a,b)))
    elif t=="√":
        print(a,t,b,"=",float(pow(b,1/a)))
    elif t=="r":
        print(a,"√",b,"=",float(pow(b,1/a)))
    print("按下Enter键退出或继续")
input()
