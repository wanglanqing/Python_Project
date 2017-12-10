import sys
import os
import pdb

def update_recursively(path):
	try:
		#pdb.set_trace()
		try:
			os.chdir(path)
		except Exception as e:
			print(e)
			return
		dirs = os.listdir()
		if len(dirs) == 0:
			return
		if ".svn" in dirs:
			print("\33[1m========== ", path, " ==========\33[0m")
			os.system("svn update " )
		for dirname in dirs:
			if os.path.isdir(dirname):
				update_recursively(dirname)
	finally:
		os.chdir("..")

		

print("\33[32m\33[0m")
os.system("dir")
print("\33[2J")
dir_begin = "."
arglen = len(sys.argv)
if arglen == 2:
	dir_begin = sys.argv[1]
	if not os.path.isdir(dir_begin):
		print("error: Please input a directionary for update searching.")
		exit(2)
if arglen > 2:
	print("usage: svnupdateall <searching-path>")
	exit(1)

update_recursively(dir_begin)
