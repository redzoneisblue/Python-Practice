print("Hello world!! \n")

#this is a practile file

with open('newfile.txt','r+') as nf:
	
	nf.seek(0)
	reader =  nf.read()

	if not reader :
		print("empty file")		
	else :
		print('Current content in the file : \n',reader,'\n')
		uinput = input("Enter something to store in the file: \n \n")
		nf.write(uinput)
		nf.seek(0)
		reader =  nf.read()
	print("--------------------------------------------------")
	print('content after writing the file :\n',reader)