import os, shutil

mu = open("kb\\audio.txt", "r")
vi = open("kb\\video.txt", "r")
do = open("kb\\doc.txt", "r")
co = open("kb\\compressed.txt", "r")
pi = open("kb\\picture.txt", "r")
pr = open("kb\\program.txt", "r")

musicExt = mu.read().splitlines()
videoExt = vi.read().splitlines()
docExt = do.read().splitlines()
compExt = co.read().splitlines()
picExt = pi.read().splitlines()
progExt = pr.read().splitlines()


user = os.getlogin()

defaultFolder = {'Music': 'C:/Users/'+user+'/Downloads/Music',
				 'Video': 'C:/Users/'+user+'/Downloads/Video', 
				 'Documents': 'C:/Users/'+user+'/Downloads/Documents', 
				 'Programs' : 'C:/Users/'+user+'/Downloads/Programs',
				 'Compressed' : 'C:/Users/'+user+'/Downloads/Compressed',
				 'Pictures' : 'C:/Users/'+user+'/Downloads/Pictures'
				 }

notInTheList = [];


os.system('cls')
folder = os.getcwd()

print("Folder: "+folder+"\n")
ch = input("Change directory?\n(Y/N): ")

while(1):
	if(ch == 'Y' or ch == 'y' ):
		folder = input("Type the address (ex: C:\\Users\\username\\Documents): ")

		while(not os.path.exists(folder)):
			print("Error! No such folder\n")
			folder = input("Type the address (ex: C:\\Users\\username\\Documents): ")
		
		os.system('cls')
		print("Folder: "+folder+"\n")
		ch = input("Change directory again?\n(Y/N): ")
	else:
		break


files = (file for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file)))

for file in files:
	ext = os.path.splitext(file)[-1].lower()

	if any(ext == mext for mext in musicExt):
		if(not os.path.exists(defaultFolder['Music'])):
			os.mkdir(defaultFolder['Music'])
		try:
			shutil.move(folder+'/'+file, defaultFolder['Music']+'/'+file)
		except IOError as e:
			print("Error: "+e.strerror)
		else:
			print(">> \""+file+"\" succesfully removed into Music folder!")

	elif any(ext == vext for vext in videoExt):
		if(not os.path.exists(defaultFolder['Video'])):
			os.mkdir(defaultFolder['Video'])
		try:
			shutil.move(folder+'/'+file, defaultFolder['Video']+'/'+file)
		except IOError as e:
			print("Error: "+e.strerror)
		else:
			print(">> \""+file+"\" succesfully removed into Video folder!")

	elif any(ext == dext for dext in docExt):
		if(not os.path.exists(defaultFolder['Documents'])):
			os.mkdir(defaultFolder['Documents'])
		try:
			shutil.move(folder+'/'+file, defaultFolder['Documents']+'/'+file)
		except IOError as e:
			print("Error: "+e.strerror)
		else:
			print(">> \""+file+"\" succesfully removed into Documents folder!")

	elif any(ext == cext for cext in compExt):
		if(not os.path.exists(defaultFolder['Compressed'])):
			os.mkdir(defaultFolder['Compressed'])
		try:
			shutil.move(folder+'/'+file, defaultFolder['Compressed']+'/'+file)
		except IOError as e:
			print("Error: "+e.strerror)
		else:
			print(">> \""+file+"\" succesfully removed into Compressed folder!")

	elif any(ext == pext for pext in progExt):
		if(not os.path.exists(defaultFolder['Programs'])):
			os.mkdir(defaultFolder['Programs'])
		try:
			shutil.move(folder+'/'+file, defaultFolder['Programs']+'/'+file)
		except IOError as e:
			print("Error: "+e.strerror)
		else:
			print(">> \""+file+"\" succesfully removed!")

	elif any(ext == gext for gext in picExt):
		if(not os.path.exists(defaultFolder['Pictures'])):
			os.mkdir(defaultFolder['Pictures'])
		try:
			shutil.move(folder+'/'+file, defaultFolder['Pictures']+'/'+file)
		except IOError as e:
			print("Error: "+e.strerror)
		else:
			print(">> \""+file+"\" succesfully removed Picture folder!")

	else:
		if(ext not in notInTheList):
			notInTheList.append(ext)


mu = open("kb\\audio.txt", "a")
vi = open("kb\\video.txt", "a")
do = open("kb\\doc.txt", "a")
co = open("kb\\compressed.txt", "a")
pi = open("kb\\picture.txt", "a")
pr = open("kb\\program.txt", "a")

if(notInTheList):
	for ext in notInTheList:
		print()
		print("I\'m sorry, I don\'t know what kind of this extension: "+ext) 
		a = input("Do you want to add \""+ext+"\" to my dictionary?\n(Y/N): ")

		if(a == 'Y' or a == 'y'):
			print("1. Music\n2. Video\n3. Documents\n4. Programs\n5. Pictures\n6. Compressed")
			b = input("Where would I categorize this \""+ext+"\" ?\n(1/2/3/4/5/6): ")

			if(b == '1'):
				mu.write(ext+'\n')
				print("\""+ext+"\" has been added to my Music dictionary")
			elif(b == '2'):
				vi.write(ext+'\n')
				print("\""+ext+"\" has been added to my Video dictionary")
			elif(b == '3'):
				do.write(ext+'\n')
				print("\""+ext+"\" has been added to my Documents dictionary")
			elif(b == '4'):
				pr.write(ext+'\n')
				print("\""+ext+"\" has been added to my Programs dictionary")
			elif(b == '5'):
				pi.write(ext+'\n')
				print("\""+ext+"\" has been added to my Pictures dictionary")
			elif(b == '6'):
				co.write(ext+'\n')
				print("\""+ext+"\" has been added to my Compressed dictionary")


mu.close()
vi.close()
do.close()
co.close()
pi.close()
pr.close()