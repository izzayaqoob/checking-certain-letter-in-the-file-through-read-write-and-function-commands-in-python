def function():
	name=input("Enter name: ")
	reg=input("Enter reg no: ")
	f=open("file.txt","w+")
	f.write(str(name))
	f.write("\n")
	f.write(str(reg))
	f.close()
	
function()

def check():
	file=open("file.txt","r")
	count=0
	read=file.read()
	check=input("Enter variable to be checked: ")
	for i in read:
		if i==check:
			count=count+1
	print("Variable", check ,"in the file occurs", count,"times")

check()
