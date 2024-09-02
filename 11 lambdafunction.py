# x=lambda:print("hellow world")
# x()

#function with an argument

# x=lambda name:print('my name is',name)
# x('prajith')

#maping

# list1=[1,2,3,4,5,6,]
# x=list(map(lambda y:y**2,list1))
# for i in x:
#     print(i)


#filter

# list1=[1,2,3,4,5,6]
# x=list(filter(lambda y: y%2==0,list1))
# for i in x:
#     print(i)


#reduce
# list1=[1,2,3,4,5]
# from functools import reduce
# product= reduce(lambda x,y:x+y,list1) 
# print(product)

#functoin
# def x():
#     print("hello how are you")
# x()

#ARGUMENT FN
# def x(y):
#     print(y+"john")
# x("emil")
# x("tobiyas")
# x("liniyas")

#FUNCTION ARGUMNETS
# def add_number(a,b):
#     sum=a+b
#     print('sum:',sum)
# add_number(2,3)

#default argument

# def x(a=7,b=5):
#     sum=a+b
#     print('sum',sum)
# x(3,5)
# x(a=2)
# x()

#KEYWORD ARGUMENT
# def x(fname,lastname):
#     print('fname',fname)
#     print('lastname',lastname)
# x(lastname='cartman',fname='eric')

#to find sum of multiple numbers
# def x(*numbers):
#     result=0
#     for num in numbers:
#         result=result+num
#     print("sum=",result)
# x(1,3,5)
# x(4,5)    

