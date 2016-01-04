import os

def run(**args):
    
    files = os.listdir(".")
    print "[*] In dirlister module.",files
    
    return str(files)
