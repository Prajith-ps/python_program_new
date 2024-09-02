# x=-2
# if x>0:
#     print("x is a positive number")
# elif x==0:
#     print("x is equal to 0")
# else:
#     print("x is a negative number")




# num=int(input("enter a number"))
# if num>0:
#       print("number is a positive number")
# elif num==0:
#         print("number is zero")
# else:
#       print("number is negative")



# x=int(input("enter a number"))
# if x % 2==0:
#     print("x is a even number")
# else:
#     print("x is odd number")



# x=int(input("enter a number"))
# b=int(input("enter a number"))
# a=x+b
# print(a)

# 1 transpose of matrix
# def transpose_matrix(matrix):
#     transposed=[[matrix[j][i]
#     for j in range(len(matrix))]
#     for i in range(len(matrix[0]))]
#     return transposed
# matrix=[
#    [1,2,3],
#    [4,5,6],
#    [7,8,9]
# ]       
# print("original matrix:")
# for row in matrix:
#    print(row)

# transposed=transpose_matrix(matrix)

# print("/transpose matrix:")
# for row in transposed:
#    print(row)

# 2 Write a program to find the sum of all the elements in a list.

# list1=[1,2,3,4,5]
# total_sum=sum(list1)
# print(total_sum)

#3 program to list comprehenion
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)
  

#4 to add a ket to dictonary

# d = {0: 10, 1: 20}
# print(d)
# d.update({2: 30})
# print(d)


#5  
# number=(1,2,3,4,5,6,7,8,)
# num = [x for x in number if x % 2 != 0]
# print(num)


#6 Write a Python program to sum all the items in a dictionary.

# def returnSum(myDict):
 
#     list = []
#     for i in myDict:
#         list.append(myDict[i])
#     final = sum(list)
 
#     return final
# dict = {'a': 100, 'b': 200, 'c': 300}
# print("Sum :", returnSum(dict))

#7 Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30

# def printValues():
#     # Create an empty list 'l'
#     l = list()
#     for i in range(1, 21):
#         l.append(i**2)
#     print(l[:5])
#     print(l[-5:])
# printValues()


#8Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized
# lines = []
# while True:
#     line = input()
#     if line == "":
#         break
#     lines.append(line)

# for line in lines:
#     print(line.upper())

#9 Define a class which has at least two methods one, to get a string from console  
# input and other is to print the string in uppercase.

# class StringManipulator:
#     def __init__(self):
#         self.text = ""

#     def get_input(self):
#         self.text = input("Enter a string: ")

#     def print_uppercase(self):
#         print(self.text.upper())
# obj=StringManipulator()
# obj.get_input()
# obj.print_uppercase()


# 10  Define a class, which have a class parameter and have a same instance parameter.
# class Example:
#     parameter = "Class Parameter"  # Class parameter

#     def __init__(self, parameter):
#         self.parameter = parameter  # Instance parameter

#     def show_parameters(self):
#         print(f"Class Parameter: {Example.parameter}")
#         print(f"Instance Parameter: {self.parameter}")
# obj = Example("Instance Parameter Value")
# obj.show_parameters()


#11 Define a class named Circle which can be constructed by radius. The Circle class has a method which can compute the area.
# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)
# x=int(input("enter the num"))
# my_circle = Circle(x)
# print("Area of the circle:", my_circle.area())


#12 Define a class named BankAccount. This class should contain methods withdraw() and deposit to calculate the balance amount remained in your account.

# class bankaccount:
#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.balance=balance
#     def display_balance(self):
#         print("balance:",self.balance)
#     def display_account_number(self):
#         print("account_number:",self.account_number)
# x=int(input("enter bank ac number"))
# b=bankaccount(x,566746)
# b.display_balance()
# b.display_account_number()



import csv

# Writing to a CSV file
def write_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Reading from a CSV file
def read_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        return list(reader)

# Example usage
data_to_write = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles']
]

filename = 'example.csv'

write_csv(filename, data_to_write)

read_data = read_csv(filename)
print(read_data)
