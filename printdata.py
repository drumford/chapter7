import decimal

file = open("data/abc/8344.data" , 'rb')
string = file.read(-1)
print "file read = %s" % string
s = string[0]
h = int(decimal(s))
d = string[1]
print h,d

file.close()





