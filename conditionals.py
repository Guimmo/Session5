try:
    num = input("Gimme number")
    num = int(num)

    if num % 2 == 1:
        print("odd number:", num)
    else:
        print("even number:", num)
except ValueError:
    print("that is not a number")


a=10
b=10
if a>b:
    print(a, "is greater than",b)
elif a==b:
    print(a, "is equal to",b)
else:
    print(a, "is less than",b)


money= 10

if money>1000000000000:
    print("billionaire")
elif money>1000000000:
    print("multi millionaire")
elif money>800000:
    print("almost but not quite millionaire")
elif money> 100000:
    print("six figure club")
elif money>10000:
    print("not really poor")
else:
    print("you are broke")
    


