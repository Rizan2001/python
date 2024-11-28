# f = open("shanthappan.csv","x")

import csv
with open("shanthappan.csv","w", newline='')as file:
    w1 = csv.writer(file)
    w1.writerow(["car","movie","travel"])
    w1.writerow(["bentley","premalu","usa"])
    w1.writerow(["porsche","black","switzerland"])

# read file

import csv
with open("shanthappan.csv","r") as file:
    r1 = csv.reader(file)
    for row in r1:
        print(row)





