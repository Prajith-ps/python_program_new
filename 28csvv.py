# import csv
# with open('beef.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "dish", "curry"])
#     writer.writerow([1, "porotta", "beef"])
#     writer.writerow([2, "chapathi", "chicken curry"])
import csv

with open('beef.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)