import os

print(f"Current Working Directory: {os.getcwd()}")

os.chdir("day7")

print(f"Now your dir is  {os.getcwd()}")
#os.rmdir("songs")
#os.mkdir("songs")

os.chdir("..")
print(f"Now Current Working Directory: {os.getcwd()}")

print(os.listdir()) # list of files and directories in the current working directory
