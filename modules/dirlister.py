import os

def run(**args):
    
    files = os.listdir(".")
    print "[*] In dirlister module.",str(files)
    
    return str(files)
