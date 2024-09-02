# import zipfile
# with zipfile.ZipFile("text.zip","w")as f:
#     f.write("file1.txt")
#     f.write("file2.txt")
# with zipfile.ZipFile ("text.zip","r")as f:
#     f.extractall('extracted')
 
import csv
with open('pamba.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "dish", "curry"])
    writer.writerow([1, "porotta", "beef"])
    writer.writerow([2, "chapathi", "chicken curry"])
import csv
with open('pamba.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "dish", "curry"])
    writer.writerow([1, "porotta", "beef"])
    writer.writerow([2, "chapathi", "chicken curry"])
import zipfile
with zipfile.ZipFile("text.zip",'w')as f:
    f.write("pamba.csv")
    f.write("pamba2.csv")

with zipfile.ZipFile("text.zip","r")as f:
    f.extractall("extracted")
    list1=f.namelist()
    print(list1)