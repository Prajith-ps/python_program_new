# f=open("demo.txt","r")
# print(f.read())

# f=open("C:/Users/Python/Documents/My Tableau Repository/Logs","r")
# print(f.read())


# f = open("C:/Users/Python/Desktop/fast.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()
# f = open("C:/Users/Python/Desktop/fast.txt", "r")
# print(f.read()) 

# f = open("C:/Users/Python/Desktop/fast.txt", "a")
# f.write("Now the file has more content!")
# f.close()
# f = open("C:/Users/Python/Desktop/fast.txt", "r")
# print(f.read())


# f = open("C:/Users/Python/Desktop/food.txt", "a")
# f.write("Woops! I have deleted the content!")
# f.close()
# f = open("C:/Users/Python/Desktop/food.txt", "r")
# print(f.readlines())



# f = open("C:/Users/Python/Desktop/food.txt", "a")
# f.write("Woops! I have deleted the content!")
# f.close()
# f = open("C:/Users/Python/Desktop/food.txt", "r")
# print(f.readlines())

#writeline

f = open("demofile1.txt", "a")
f.writelines(["\nSee you soon!", "\nOver and out."])
f.close()

#open and read the file after the appending:
f = open("demofile1.txt", "r")
print(f.read()) 