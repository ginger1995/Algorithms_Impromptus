#!/usr/bin/python
# coding = utf-8
'''
This program intends to shift circularly the elements of list 'a' towards the left by certain number of steps which is indicated by the variable offset.
'''
a = [1,2,3,4,5,6,7,8,9,0]
b = []
i = j = 0
offset = -13
offset = offset % len(a)
while(i < len(a)):
	if((i+offset) <= len(a) - 1):
		b.append(a[i + offset])
	i = i + 1
while(j <= offset - 1):
	b.append(a[j])
	j = j + 1
print(b)