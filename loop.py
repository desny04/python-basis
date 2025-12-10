#for loop

# for i in range(1,11):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# for i in range(1,11):
#     if i%2==0:
#         print(i)


# a=int(input("Enter First num:"))
# b=int(input("Enter Second num:"))

# for i in range(a,b):
#     print(i)

# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)


#while loop

# i=1
# while(i<=10):
#     print(i)
#     i+=1

# i=10
# while(i>=1):
#     print(i)
#     i-=1

# i=0
# while(i<=10):
#     i+=1
#     if i%2==0:
#         print(i)


# a=int(input("Enter 1st num:"))
# b=int(input("Enter 2nd num:"))

# while(a<=b):
#     print(a)
#     a+=1

# sum=0
# i=1
# while(i<=10):
#     i+=1
#     sum=sum+i
# print(sum)

# i=1
# while(i<=5):

#     print(i)
#     i+=1


#horizontal print

# for i in range(1,11):
#     print(i,end=' ')


#nested loop

# for i in range(4):
#     for j in range(4):
#         print('*', end=' ')
#     print()

# for i in range(1,4):
#     for j in range(3):
#         print(i,end=' ')
#     print()

# for i in range(3):
#     for j in range(1,4):
#         print(j,end=' ')
#     print()

# num=1
# for i in range(3):
#     for j in range(3):
#         print(num,end=' ')
#         num+=1
#     print()

for i in range(1,4):
    for j in range(3):
        print(i,end=' ')
        i+=1
    print()

print("-"*30)

for i in range(1,4):
    num=i
    for j in range(3):
        print(num,end=' ')
        num+=1
    print()

print("-"*30)

rows=5
for i in range(1,rows+1):
    for j in range(i):
        print("*",end=' ')
    print()

print("-"*30)

for i in range(1,6):
    for j in range(i):
        print("*",end=' ')
    print()

print("-"*30)

a=65
for i in range(3):
    for j in range(3):
        print(chr(a), end=' ')
        a+=1
    print()