
r=open("Programming_Data_1.csv","r")

import csv

csv.field_size_limit(100000000)


bg_reader=csv.reader(r)
# r.read()
count = 0
language_types = {'py':0,"cpp":0,'npy':0,'sh':0,'bsh':0,'js':0,'coffee':0,'java':0}

comp =  open("complimentary_data_set.csv","w")
tmp = csv.writer(comp)
js_count = 0

for re in bg_reader:
	a,b = re
	if b in language_types:
		if b=='js':

			if js_count<=3200:
				tmp.writerow(re)
				js_count+=1
		elif b!='py':
			tmp.writerow(re)

	try:
			# print b
		language_types[b]+=1
	except KeyError:
		language_types[b]=1

for y in language_types:
	print "language : ",y,"          count : ",language_types[y]
comp.close()