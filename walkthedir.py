import os

mode  = "r"

file_data = {'py':[],"cpp":[],'npy':[],'sh':[],'bsh':[],'js':[],'coffee':[],'java':[]}

csv_data = []

app = csv_data.append

failed_types = {r:0 for r in file_data.keys()}

for u in  os.walk("XXXXX"):
	a,b,files =  u
	# print b
	# print files
	for file in files:
		lst = file.split(".") 
		if len(lst)>=2:
			# open(a+"\\"+file)
			extension = lst[-1]
			if extension in file_data:
				try:
					data = open(a+"\\"+file,mode).read()
					# file_data[extension].append(data)
					app([data,extension])
				except IOError:
					failed_types[extension]+=1
print len(csv_data)
import csv
with open("Programming_Data.csv","w") as file_:
	lwriter = csv.writer(file_)
	for y in csv_data:
		lwriter.writerow(y)

