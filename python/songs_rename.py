import os, sys

if len(sys.argv) != 2:
	print "Please provide the directory containing songs that needs to be renamed"
	sys.exit()
	
dirPath = sys.argv[1]
print dirPath
#Open file
dirs = os.listdir(dirPath)

# List all files in path
count = 0
for file in dirs:
	oldfilename = file
	newfilename = oldfilename.lower()
	os.rename(dirPath + oldfilename, dirPath + newfilename)
	count += 1

print "Renamed " + str(count) + " files"
	

