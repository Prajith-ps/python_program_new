#inheritance
# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#             print(self.firstname,self.lastname)
# class student(person):
#     def __init__(self,fname,lname):
#         person.__init__(self,fname,lname)
# x=student("mike","olson")
# x.printname()


##task
# class animal:
#     def __init__(self,name,age,colour):
#         self.age=age
#         self.colour=colour
#         self.name=name
#     def printname(self):
#         print(self.name,self.age,self.colour)
# class dog(animal):
#     def __init__(self,name,age,colour):
#         animal.__init__(self,name,age,colour)
# x=dog("tobbi","black",100)
# x.printname()


#METHOD OVELOADING

# class example:
#    def add(self, a, b):
#       x = a+b
#       return x
#    def add(self, a, b, c):
#       x = a+b+c
#       return x

# obj = example()

# print (obj.add(10,20,7))
# print (obj.add(10,20))