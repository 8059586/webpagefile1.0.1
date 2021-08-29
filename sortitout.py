import csv
data = []
with open("dataset_2.csv","r") as f:
    reader = csv.reader(f)
    for i in reader:
        data.append(i)
headers = data[0]
planetinfo = data[1:]
for i in planetinfo:
    i[2]=i[2].lower()
planetinfo.sort(key = lambda planetinfo: planetinfo[2])

with open("sorteddataset.csv","a+") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(planetinfo)