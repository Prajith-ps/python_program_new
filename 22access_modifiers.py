#access modifiers
#PUBLIc
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)
# s=student("john",20)
# s.display()


#private

# class bankaccount:
#     def __init__(self,account_number,balance):
#         self.__account_number=account_number
#         self.__balance=balance
#     def __display_balance(self):
#         print("balance:",self.__balance)
# b=bankaccount(13265625656,566746)
# b.__display_balance()


#protect:
# class person:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#     def _display(self):
#         print("name:",self._name)
#         print("age:",self._age)
# class student(person):
#     def __init__(self,name,age,roll_number):
#         super().__init__(name,age)
#         self._roll_number=roll_number
#     def display(self):
#         self._display()
#         print("roll number:",self._roll_number)
# s=student("john",20,123)
# s.display()


