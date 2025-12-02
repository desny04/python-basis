# a=23
# if a<20:
#     print(a,"is less than 20")

# else:
#     print(a, "is greater than 20")

# b=4
# if b%2==0:
#     print(b,"is even number")

# else:
#     print(b,"is odd number")



#if elif

# day=int(input('enter a number:'))
# if day==1:
#     print('sunday')
# elif day==2:
#     print('Monday')
# elif day==2:
#     print('Tuesday')
# else:
#     print('Invalid Output')


#nested if

a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

if a>b:
    if a>c:
        print(a,"is larger")
    else:
        print(c,"is larger")
else:
    if b>c:
        print(b,"is larger")
    else:
        print(c,"is larger")


