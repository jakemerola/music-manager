## PROVIDED WITH ABSOLUTELY NO WARRANTY OF ANY KIND ##

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

def getListOfDirectories():
	returnList=[f for f in os.listdir('.') if os.path.isdir(f)]
	returnList.sort()
	return(returnList)

def getListOfFiles():
	returnList=[f for f in os.listdir('.') if os.path.isfile(f)]
	returnList.sort()
	return(returnList)

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

def getArtistAlbum(prompt):
	dirs=getListOfDirectories()
	print("\n" + prompt)
	for i in range(0,len(dirs)): 
		print("[%02d]   %s" % (i+1,dirs[i]))
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
			print("[%02d/%02d] Adding %s..." % (x-selection+1,len(files)-selection,fileName))
			os.system("rhythmbox-client --enqueue \'" + fileName + "\'")
		print("Sending play command..."); os.system("rhythmbox-client --play")
		print("Complete.")
		
main()
