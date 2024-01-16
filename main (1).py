import csv
f = open("example.csv","r")
data=csv.reader(f)
sum=0
next(f)
for i in data:
    sum = sum + int(i[2])
print("total marks are",sum)

