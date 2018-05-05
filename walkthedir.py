import os

mode  = "r"

file_data = {'py':[],"cpp":[],'npy':[],'sh':[],'bsh':[],'js':[],'coffee':[],'java':[]}

csv_data = []

app = csv_data.append

failed_types = {r:0 for r in file_data.keys()}
q=0
for u in  os.walk("C:\\"):
	a,b,files =  u
	for file in files:
		lst = file.split(".") 
		if len(lst)>=2:
# 			# open(a+"\\"+file)
			extension = lst[-1]
			if extension in file_data:
				q+=1
				try:
					data = open(a+"\\"+file,mode).read()
					# file_data[extension].append(data)
					app([data,extension])
				except IOError:
					failed_types[extension]+=1
print len(csv_data)
import csv
with open("Programming_Data_1.csv","w") as file_:
	lwriter = csv.writer(file_)
	for y in csv_data:
		lwriter.writerow(y)

# print q