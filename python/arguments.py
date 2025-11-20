# def add(a,b,c):
#     return a+b


# print(add(20,30,40))


def student(name,age,roll):
    print("my name is",name)
    print("my age is",age)
    print("my roll is",roll)


# # student(age=24,name="hema",roll="c001")# key word argument


def student(name,age,roll,branch="CSE"):
    print("my name is",name)
    print("my age is",age)
    print("my roll is",roll)
    print("my branch is",branch)


# student(age=24,name="hema",roll="c001")# key word argument
# print()
# student(age=24,name="mahender",roll="c001",branch="AIML")# key word argument


def add(*a):# infinate required arg *->tuple
    print(a)
    print(type(a))# tuple
    return sum(a)


# print(add(10,20))
print(add(10,20,30,2,1,1,2,3,1,2,3,4,5,6,7,2,3))
# print(add(10,20,30,2,1,1))



def student(**b):#**-> dict
    print(b)

student(name="Mahender",rollno=30)
student(name="vivek",rollno=21,branch="AIML")
student(name="hema",rollno=26,branch="CSE",loc="madhapur")
