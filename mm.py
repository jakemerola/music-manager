## PROVIDED WITH ABSOLUTELY NO WARRANTY OF ANY KIND ##

validExtensions=[".mp3",".m4a",".wav",".wma",".aiff",".ogg"]
import os
import re

def main():
	while 1:
		if (getArtistAlbum("Artist: ") == -1):
			print("Starting over...")
		elif (getArtistAlbum("Album: ") == -1):
			os.chdir("..")
			print("Starting over...")
		elif (getAndPlayTrack() == -1):
			os.chdir("..")
			os.chdir("..")
			print("Starting over...")
		else:
			break

def printValidExtensions():
	for x in range(0, len(validExtensions)-2):
		print("%s," % validExtensions[x]),
	print("%s." % validExtensions[len(validExtensions)-1])

def sort(input):
	#future implementation would require >python 2.7 to examine mp3 tags
	input.sort()
	return(input)

def getListOfDirectories():
	returnList=[f for f in os.listdir('.') if os.path.isdir(f)]
	sort(returnList)
	return(returnList)

def getListOfFiles(): 
	returnList=[f for f in os.listdir('.') if os.path.isfile(f) and isValidExtension(f)]
	sort(returnList)
	return(returnList)

def getArtistAlbum(prompt):
	dirs=getListOfDirectories()
	print("\n" + prompt)
	for i in range(0,len(dirs)): 
		print("[%02d]   %s" % (i+1,dirs[i]))
	if (len(dirs)==0):
		print("Directory is empty.")
	selection=getInteger(len(dirs))-1
	if (selection==-2): #remember, -1
		return(-1)
	else:
		os.chdir(dirs[selection])
		return(0)

def getAndPlayTrack():
	files=getListOfFiles();	
	print("\nTrack:")
	for i in range(0,len(files)): 
		print("[%02d]   %s" % (i+1,files[i]))
	if (len(files)==0):
		print("Directory does not contain any of the following filetypes:"),
		printValidExtensions()
		print("To modify this list, edit validExtensions[] at the top of this script.")
	selection=getInteger(len(files))-1
	if (selection==-2): #-1 minus 1
		return(-1)
	else:
		print("Opening Rhythmbox..."); os.system("rhythmbox-client")
		print("Sending stop command..."); os.system("rhythmbox-client --stop")
		print("Clearing queue..."); os.system("rhythmbox-client --clear-queue")

		for x in range(selection, len(files)):
			fileName=os.getcwd() + "/" + files[x]
			fileName=fileName.replace("\'","'\\''")
			fileName=fileName.replace("\"","\"")
			print("[%02d/%02d] Adding %s..." % (x-selection+1,len(files)-selection,files[x]))
			os.system("rhythmbox-client --enqueue \'" + fileName + "\'")
		print("Sending play command..."); os.system("rhythmbox-client --play")
		print("Complete.")
		
def isValidExtension(input):
	#see top of file for valid extension definitions.
	fileName, fileExtension=os.path.splitext(input)
	if fileExtension in validExtensions:
		return(True)
	else:
		return(False)

def getInteger(maxValInclusive):
	while 1:
		temp=raw_input("? ")
		if (temp==".."):
			return(-1)
		try:
			val=int(temp)
		except ValueError:
			print("Invalid input")
			continue
		if (val > 0 and val <= maxValInclusive):
			return(val)
		else:
			print("Invalid input")
			continue

main()
