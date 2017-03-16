#!/usr/bin/python

def printtabs(f, i):
	if i < 1:
		return
	else:
		for i in range (0, i-1):
			fo.write("\t")
	return

index = 0;
fi = open("program.f90", r)
fo = open("program.py", w)


tokens = codeline.split(" ")

if tokens[0] == "IF":
	printtabs(f, index)
	fo.write("if")
	counter = 1
	while codeline[counter] != "THEN":
		fo.write(" " , codeline[counter])
		counter = counter + 1
	fo.write(":\n")
	index = index + 1
if tokens[0] == "ELSE":
	index = index - 1
	printtabs(f, index)
	fo.write("elif")
	counter = 2
	while codeline[counter] != "THEN":
		fo.write(" " , codeline[counter])
		counter = counter + 1
	fo.write(":\n")
	index = index + 1
if tokens[0] == "ENDIF":
	index = index - 1
	printtabs(f, index)
	fo.write(":\n")
