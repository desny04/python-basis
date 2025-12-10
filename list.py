l=[1,2,3,4]
# for i in l:
#     print(i)


# l.append(5)
# print(l)

# l.append([5,6,7])
# print(l)

# l.extend([5,6,7])
# print(l)

# l.insert(2,10)
# print(l)

number=int(input("Enter number of students that you want add:"))
students=[]
for i in range(1,number+1):
    print('Student:',i)
    name=input("Enter name of the student:")
    age=int(input("Enter age of the student:"))
    students.append([name,age])
print(students)


