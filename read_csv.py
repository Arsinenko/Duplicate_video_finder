import csv

with open("train.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print("uuid:" + row[1])
        print("upload_date:" + row[0])
        print("")