import csv
data1 = []
with open("dataset_1.csv","r") as f:
    reader = csv.reader(f)
    for i in reader:
        data1.append(i)
headers1 = data1[0]
planetinfo1 = data1[1:]
data2 = []
with open("sorteddataset.csv","r") as f:
    reader = csv.reader(f)
    for i in reader:
        data2.append(i)
headers2 = data2[0]
planetinfo2 = data2[1:]

headers = headers1+headers2
planetinfo=[]
for i,v in enumerate(planetinfo1):
    planetinfo.append(planetinfo1[i]+planetinfo2[i])

with open("final.csv","a+") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(planetinfo)