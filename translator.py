#!/usr/bin/python

#function to print the tabs at the beginning of the lines
def printtabs(f, i):
	if i < 1:
		return
	else:
		for i in range (0, i-1):
			fo.write("\t")
	return

#variables; fi should probably be set as a command line argument
index = 0;
fo = open("program.py", w)

#getting the line and splitting it into tokens

with open("program.f90",'rb') as fi:
	while True:
        	line=f.readline()
		if not line: break
		codeline = fi.getline()
		tokens = codeline.split(" ")
		#if statement controls
		if (tokens[0] == "IF") or (tokens[0] == "if"):
			printtabs(f, index)
			fo.write("if")
			counter = 1
			while (codeline[counter] != "THEN") and (codeline[counter] != "then") and (codeline[counter] != "EXIT") and (codeline[counter] != "exit"):
				fo.write(" " , codeline[counter])
				counter = counter + 1
			if (codeline[counter] == "THEN") or (codeline[counter] == "then"):
				fo.write(":\n")
			elif (codeline[counter] == "EXIT") or (codeline[counter] == "exit"):
				fo.write(": break\n")
			index = index + 1
		if (tokens[0] == "EXIT") or (tokens[0] == "exit"):
			fo.write("break\n")
		if (tokens[0] == "CONTINUE") or (tokens[0] == "continue"):
			fo.write("continue\n")
		if (tokens[0] == "ELSE") or (tokens[0] == "else"):
			index = index - 1
			printtabs(f, index)
			fo.write("elif")
			counter = 2
			while (codeline[counter] != "THEN") and (codeline[counter] != "then") and (codeline[counter] != "EXIT") and (codeline[counter] != "exit"):
				fo.write(" " , codeline[counter])
				counter = counter + 1
			fo.write(":\n")
			index = index + 1
		if (tokens[0] == "ENDIF") or (tokens[0] == "endif"):
			index = index - 1
			printtabs(f, index)
			fo.write(":\n")
		#do loop controls
		if (tokens[0] == "DO") or (tokens[0] == "do"):
			printtabs(f, index)
			fo.write("for ", tokens[2], " in range(", tokens[4], tokens[5], ":")
			index = index + 1
		if (tokens[0] == "ENDDO") or (tokens[0] == "enddo"):
			index = index - 1
			printtabs(f, index)
			fo.write("\n")
		if (tokens[0] == "END") or (tokens[0] == "end"):
			#some loops use "end for" or "end do" rather than run together
			index = index - 1
			printtabs(f, index)
			fo.write("\n")	
