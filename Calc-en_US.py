import math
print("Calculator")
print("Example :")
print("5")
print("+")
print("3")
print("square root, input r or √(41420 holding Alt and in turn by the keypad)")
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
    print("Press Enter to exit or continue")
input()
