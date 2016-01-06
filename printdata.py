import base64

file = open("data/abc/98320.data" , 'r')
string = file.read(-1)
file.close()
# print "file read = %s" % string
s = base64.b64decode(string)
print "Base64 decode = ",s



