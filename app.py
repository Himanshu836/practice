# PYTHON BASICS TILL OOPS CONCEPT






# year = input("birth year ?")
# year = int(year)
# print(type(year))
# course = ('''
#
# mflsfldslf,;lds,f;lsd,f
# ds;fmsdklfm
# 4lkdfndskl
# naedfkedn
#
# '''
#           )
# print(course)
# hell = "hell"
# print((hell[2]))
# ------------------------------------------------------------------------->
# string formatting
# a = "hello"
# b="Chintu ji"
# msg1 = a + ',' +b
# msg2 = f'{a},{b}'
# print(msg1 + "........ " + msg2)
# print(len(a))
# print(a.upper())
# a="this is python 3"
# print("this is the value of a i.e %s"%a)
#
# s=10
# print(s%2)
# (a.find("b"))
# print(a.replace("beginning","Beginning"))
# print("Beginning" in a)


# math operators----------------------------------->
# x=20.5
# print(round(x)) round()
# print(abs(-7.6)) returns always +ve

# print(2==2) comparison opr
# print(2!=3)
# print(2
# # a="this is just the Beginning"
# # print<3)
# print("hello")


# conditional students

# a,b,c=5,3,1
# print(c)
# if a<b:
#     print("a is bigger")
# elif a<c:
#     print("b is greater")
# else:
#     print("c is the smallest")
#
# if a != b:
#     print("they r not equal")
# else:
#     print("equal")

# light = input("light :")
# if light=="red":
#     print("stop")
# elif light=="yellow":
#     print("be ready")
# elif light== "green":
#     print("go")
# else:
#     print("KILL")

# marks = input("enter marks")
# print(type(marks))
# if 60 < int(marks) < 90:
#     print(f"Your marks are : {marks}")


# TERNARY OPERATOR------------------------------------------------------->
# Food=input("Food: ")
# Eat = "yes" if Food=="cake" else "no"
# print(Eat)

# print("Chintu ji") if Food == "Cake" or Food == "Bread" else print(f"{Food}")

# a="hello"
# print(a[0])
# b=a.replace("h","H")
# print(len(a))
# print(a)
# print(b)
# conditional programs---------------------------->----------------------------------------------

# number = int(input("Enter a number: "))
# if number%7==0:
#     print("Yes,it is divisible by 7" + " "+f"And the number is {number}")
# else:
#     print("not divisible by 7"+" "+f"the number being : {number}")
# number1 = int(input("Enter a number: "))
# number2 = int(input("Enter a number: "))
# number3 = int(input("Enter a number: "))
# if number1 > number2 and number1>number3:
#     print(f"{number1} is the biggie")
# elif number2 >number1 and number2 > number3:
#     print(f"{number2} is the biggie")
# else:
#     print(f"{number3} is the biggie")

# LISTS & TUPLES----------------------------------------------------------------------->

# marks=[94.4,56.12,78.93,66.88]
# print(marks[3])
# print(type(marks))
# print(len(marks))
# print(marks[1:-1])
# print(marks[-4:-1])



# ......................................................list methods
# data = [14,21,1,1566]
# print(data[-4:-1])
# data.append(7)
# print(data)
# data.sort()
# print(data)
# data.sort(reverse=True)
# print(data)
# data.reverse()
# print(data)



# .........................................................>
# data2 = ["apple","cat","banana","owl"]
# data2.sort()
# print(data2)
# data2.reverse()
# print(data2)
# data2.sort(reverse=True)
# print(data2)
# data2.insert(2,"Lion")
# print(data2)


# data3 = [2,5,2,6,6]
# data3.remove(2)
# print(data3)
# data3.remove()
# print(data3)
# data3.append(7)
# data3.insert(0,7)
# print(data3)
# print(data3.append(8))
# data3.pop(5)
# print(data3)
# data3.remove(7)
# data3[0]=7
# print(data3)
# list1 = ["NARAYANA" ,"TECH" ,"HOUSE"]
# print(list1[2:])


# my_string = "apple,banana,cherry"
# fruits = my_string.split(",")
# print(fruits)
# print(type(fruits))

# ........................................>tuples
# tup = (1,2,3,4,5,6)
#
# print(tup[1:-1])
#
# print(tup.count(1))
# print(tup.index(6))
# num1=int(input("enter a num : "))
# num2=int(input("enter a num : "))
# num3=int(input("enter a num : "))
# List=[]
# List.append(num1)
# List.append(num2)
# List.append(num3)
# print(List)
# List=[1,2,3,2,1,4]
# print(List)
# list2=List.copy()
# list2.reverse()
# print(list2)
# if list2 == List:
#     print("Palindrome")
# else:
#     print("NO,its not")
# tup =("a","b","c","a","c")
# print(tup.count("a"))
# List = ["z","b","c"]
# List.sort()
# print(List)


# .........................................Dictionary..................
# dict1={
#     "name":"Himanshu",
#     "marks":696,
#     "grade":"A",
#     "is_adult":False,
#     "subjects":["python,Java"],
#     "address":("address","address2")
# }
# print(dict1)
# print(type(dict1))
# print(type(dict1["subjects"]))
# print(dict1["address"])
# dict1["address"]="Bdk","BP"
# print(dict1)
# dict1["surname"]="Sahoo"
# print(dict1)

# student = {
#     "name":"Himanshu sekhar",
#     "marks":{
#         "math":59,
#         "english":66,
#         "science":61
#     },
#     "grade":"B",
#     "address":["Bdk","BP"]
# }
# # print(student)
# # print(student["marks"]["math"])
# # print(student.keys())
# # print(list(student.values()))
# # print(student.items())
# print(student["marks"])
# student.update({"city":"delhi"})
# print(student)

# ............................................>sets
# set = {"a",12,56.7}
# print(type(set))
# a=12
# print(f"{a}")

# set2={"hi","hi",1,5,6,1,6}
# print(set2)
# print(len(set2))

# EMPTY SET
# collection = set()
# print(type(collection))
#
# collection.add("chintu")
# collection.add(1)
# collection.add(2)
# print(collection)
# collection.remove("chintu")
# print(collection)
#
# print(collection.pop())
# print(collection)

# set1={1,2,3}
# set2={2,3,4}
# set3=set1.union(set2)
# print(set3)
# set4=set1.intersection(set2)
# print(set4)
# print(set1)

# dict1={
#     "table":'"furniture",figures',
#     "cat":"a small animal"
# }
# print(dict1)
# print(type(dict1))
# dict2=dict1["table"]
# print(type(dict2))
# colll={"java","python","c++","java","c++","c"}
# print(colll)

# marks={}
# data=int(input("enter your marks"))
# marks.update({"mark":data})
# data =int(input("enter your marks"))
# marks.update({"marks":data})
# print(marks)
# abc={9,9.0}
# print(abc)
# print(type(abc))



# LOOPS---------------------------------------------------------------->
# while Loop
# ex-1
# i=1
# while i<=5:
#     print("Hello")
#     i+=1
# print(i)

# ex-2
# n=int(input("Enter a number: "))
# i=1
# while i<=10:
#     mul=n*i
#     print(mul)
#     i+=1

# ex-3
# List = [1,4,9,8,7,6]
# length = len(List)
# print(length)
# i=0
# while i<length:
#     print(List[i])
#     i+=1

# ex-4
# tup=(1,4,9,8,5,6,7)
# num=7
# i=0
# while i<len(tup):
#     print(tup[i])
#     if num == tup[i]:
#         print(f"Here is your {num}")
#         i+=1
#         break


# -----------------BREAK & CONTINUE-------------------------
#
# i=0
# while i<=5:
#     if i==3:
#         i=4
#         continue #skip
#     print(i)
#     i+=1


#----------------------------------------------For loops------------>

# lists=[1,2,3,4,5,6,7,8,9,"apple","banana"]
# for value in lists:
#     print(value)
# tup = (1,2,3,4,5,6)
# for value in tup:
#     print("Good Morning dear " ,value)
# data = "apple"
# for dataE in data:
#     print(dataE)
# else:
#     print("End")

# elements=[1,4,9,16,25,36,89]
# for every_element in elements:
#     print(every_element)
#
# elements = (1,4,9,78,25,36,64,81)
# x=int(input("Enter a num: "))
# i=0
# for every_element in  elements:
#     if every_element == x:
#         print("found the number : ",every_element)
#         break
#     else:
#         print("Searching...",i)
#         i += 1
# n=int(input("enter a num: "))
# for i in range(1,11):
#     print(n*i)

# for i in range(5):
#     pass
# print("printed")

# n=int(input("enter a number: "))
# i=1
# Sum=0
# while i<=n:
#     Sum+=i
#     i+=1
# print(Sum)

# n=int(input("enter a number: "))
# fact=1
# for i in range(1,n+1):
#     fact = i*fact #fact*=i
# print(fact)

# functions---------------------------------------------------->

# def calc_sum(a,b):
#     total = a+b
#     print(total)
#     return total
#
# data=calc_sum(37,25)
# print(data)
# calc_sum(29,78)

# def average(a,b,c):
#     return (a+b+c)/3
#
# avg=average(5,3,56)
# print(avg)

# def length_of_list(a):
#     b=len(a)
#     print(b)
# length_of_list([1,2,3])

# heroes=["srk","salman","hritik","prabhas","mahesh"]

# def oneliner(a):
#     for eachvalue in a:
#         print(eachvalue,end=" ")
#
# oneliner(heroes)


# factorial
# n=int(input("num: "))
#
# def fact(n):
#     sum=1
#     for i in range(1,n+1):
#         sum*=i
#     return sum
#
# output=fact(n)
# print(output)

# usd to inr

# dollar=int(input("Enter dollar value: "))
# def convert_dollar_to_inr(v):
#     inr=88
#     afterconv=v*inr
#     return afterconv
# After=convert_dollar_to_inr(dollar)
# print(After)

# def even_odd():
#     num=int(input("Enter a number: "))
#     if num%2==0:
#         print("EVEN")
#     else:
#         print("ODD")
# even_odd()

# file i/o----------------------------------------------------------------->
# f=open("demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()
# f=open("demo.txt","w")
#
# f.write("I am Himanshu sekhar sahoo.I want to learn javascript")
# f.close()

# f=open("demo.txt","a")
#
# f.write("I do possess basic knowledge of javascript but i want to take my skills to the next level in python.\n After that i will learn node js.")
#
# f.close()

# f= open("sample.txt","a")
# f.close()

# f= open("sample.txt","r+") #over-writes from beginning
# f.write("Greetings,")
# f.close()

# f=open("demo.txt","a")
# data=f.write("abc")
# print(data)
# f.close()
# f=open("demo.txt","a+")
# data=f.read()
# print(data)
# f.close()







