sourcefile = open("Book1.txt","r")
destnatefile = open("copybook.txt","w")
# a = sourcefile.read()
# print(a)

for i in sourcefile.read():
    destnatefile.write(i)
