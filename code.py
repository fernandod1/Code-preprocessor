# DESCRIPTION:
# This script executes 2 actions:
# 1.) removes all code between '#>>>>>> and '#<<<<<< tags from a file.
# 2.) search for tags like '#include "file.ext" and replace them with its files content.

# REQUIREMENTS:
# - Python v3
# - Python module re

# USAGE:
# Replace "original" variable with the name of your original file.
# Replace "destination" variable with the name of your desired output file.
# Execute script using command: "python code.py"
# If using under Linux/UNIX, include #!/usr/bin/python in first line of script.

import re

original = "original.txt"
destination = "destination.txt"

def write_to_file(content,filename):
    try:
        f = open(filename,"w")
        content = content.replace("\n\n\n\n","\n\n")
        f.write(content)  
        f.close()
    except:
        print("Error: can not open "+filename+" destination file.")           

def read_from_file(filename):
    try:
        f = open(filename,"r")
        content = f.read()
        f.close()
        return content
    except:
        print("Error: can not open "+filename+" original file.")

def search_and_replace(content):
    content = re.sub(r"\'#>>>>>>((.|\n)*?)\'#<<<<<<", "", content)
    filesvbs_to_import=re.findall(r"\'#include \"(.*)\"", content)
    for filevbs_to_import in filesvbs_to_import:
        try:
            f = open(filevbs_to_import,"r") 
            content_to_include = f.read()
            content = content.replace('\'#include "'+filevbs_to_import+'"',content_to_include)
            f.close()
        except:
            print("Error: can not find "+filevbs_to_import+" required by main file. This piece of code wont be included.")
    return content

try:
    content = read_from_file(original)
    content_final = search_and_replace(content)    
    write_to_file(content_final,destination)
    print("DONE. Ckeck "+destination+" file to view result.")
except:
    print("Error: can not execute script.")   

