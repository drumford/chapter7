import os

def run(**args):
    
    files = os.listdir("/")
    print "[*] In dirlister module."
    files2 = "DirLister = " + files
    
    return str(files2)
