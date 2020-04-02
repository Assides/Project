import pickle
import os
import sys

 
def Pack(direct,binary_file):
	data = list()
	for Obj in os.listdir(direct):
		with open(direct + "//" + Obj,"rb") as file:
			data.append(Obj)
			data.append(file.read())
	with open(binary_file + ".asbin","wb") as file:
		count = len(data)
		number = 0;
		for i in data:
			number += 1
			pickle.dump(i,file)
			if number == count:
				pickle.dump("EndBinaryFile",file)

def Unpack(filename):
	data = list()
	if ".asbin" in filename:
		with open(filename,"rb") as file:
			while True:
				name = pickle.load(file)
				if name != "EndBinaryFile":
					data.append([name,pickle.load(file)])
				else:
					break 
		for i in data:
			with open(i[0],"wb") as file:
				file.write(i[1])
	else:
		print("Invalid file format")


def Help():
	print("====================================================")
	print("| -h:Outputs a list of arguments                   |")
	print("| -p:Pack files(-p directory_files binary_filename |")
	print("| -u:Unpack files(-u binary_filename)              |")
	print("====================================================")

if __name__ == "__main__":
	if len(sys.argv) > 1:
		if sys.argv[1] == "-h":
			Help()
		elif sys.argv[1] == "-p":
			Pack(sys.argv[2],sys.argv[3])
		elif sys.argv[1] == "-u":
			Unpack(sys.argv[2])
	else:
		print("Add the argument -h to get a list of arguments")


	
