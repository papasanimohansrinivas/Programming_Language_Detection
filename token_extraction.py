import re

import csv


data_ = open("Programming_Data.csv","r")

data_set = open("cleaned_data_set.csv","w")


data_set_writer  = csv.writer(data_set)

object_ = csv.reader(data_)

csv.field_size_limit(100000000)

pattern = r"""[\w']+|[""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""\\]"""

# l = 0 
x_leng = 0
tokenised_source_codes = []
for u in object_:

	code,type_ = u

	x_leng+=1

	tokens = re.findall(pattern,code)
	data_set_writer.writerow(tokens+[type_])

	# print type(tokenised_source_codes.append(re.findall(pattern,code)))
import json 
print x_leng

data_set.close()

