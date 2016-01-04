import os

def run(**args):
    print "[*] In environment module.  %s" % str(os.environ)
    return str(os.environ)
