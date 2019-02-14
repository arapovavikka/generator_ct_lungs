import os 

startDir=r'yourDirectory'
targetExt='.dcm'

def suitableExt(filename):
	filename, file_extencion = os.path.splitext(filename)
	if file_extencion == targetExt:
		return True
	return False 

def divideDirAndFiles(path):
	folders=[]
	files=[]
	objects=os.listdir(path)
	for item in objects:
		if os.path.isdir(path + '/' + item):
			folders.append(path + '/' + item)
		if os.path.isfile(path + '/' + item):
			files.append(path + '/' + item)
	return files, folders

def selectPath(path):
	paths=[]
	files, folders=divideDirAndFiles(path)
	for file in files:
		paths.append(file)
	for folder in folders:
		paths.append(selectPath(folder))
	return paths
	
res = selectPath(startDir)
print(res)