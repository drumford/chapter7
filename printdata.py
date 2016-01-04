import base64

file = open("data/abc/85979.data" , 'rb')
string = file.read(-1)
print "file read = %s" % string
s = base64.b64decode(string)
print "Base64 decode = ",s

file.close()





