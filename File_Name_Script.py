'''
	Manotej Meka
	12/20/2015
	- Changes all the file extensions to lowercase
	- Addes a '_' for space for all elements in directory
'''
import os
import string

# Extracting the information in the directory
def folderFiles(path_name):	
	for filename in os.listdir(path_name):
		print filename
		# If it is directory
		if os.path.isdir(os.path.join(path_name,filename)) and not filename.startswith('.'):
			print "			Folder"
			if ' ' in filename:
				filename = containsSpace(filename,True, path_name)
				
			file_path = os.path.join(path_name,filename)
			folderFiles(file_path);
		# If it is a file
		elif not filename.startswith('.'):
			print "				File"
			if ' ' in filename:
				containsSpace(filename,False, path_name)
			else:
				temp = ExtCaps(filename);
				os.rename(os.path.join(path_name,filename),os.path.join(path_name,temp))
		print "\n......................................."

# When the name contains space then replacing with '_'
def containsSpace(filename, folder, path_name):
	tempName = filename.replace(' ','_')
		
	if folder:
		os.rename(os.path.join(path_name,filename),os.path.join(path_name,tempName))
		return tempName
	else:
		temp = ExtCaps(tempName)
		os.rename(os.path.join(path_name,filename),os.path.join(path_name,temp))
		return temp

# Chaning the extension to lowercase				
def ExtCaps(tempName):
	vector = tempName.split('.')
	temp = ''
	for i in range(0,len(vector)-1):
		temp += vector[i]+'.'
	return temp + vector[-1].lower()


# Main starting commands	
input_path = raw_input("Please input a folder path: ")
folderFiles(input_path)
print "Finished"