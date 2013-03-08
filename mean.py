import sys

sum=0
n=0

#Sum input values.
for num in open('data_2.txt'):
	sum += float(num)
	n+=1

print sum/n
