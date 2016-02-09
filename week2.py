#Coursera course - Using Python to access web data - week 2
#Input files: regex_sum_42.txt, regex_sum_214932.txt

import re

file_name = raw_input('Enter file name:')
file_handle = open(file_name)

number_list_str = []
number_list_int = []

for line in file_handle:
    number_list_str += re.findall('[0-9]+', line)

for i in number_list_str:
    number_list_int.append(int(i))

print "Count:", len(number_list_str)
print "Sum:", sum(number_list_int)
