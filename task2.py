sourcefile = open("Book1.txt","r")
destnatefile = open("copybook.txt","a")
# a = sourcefile.read()
# print(a)
count = 0
page1 = 25
pages = input("Please input how many pages you want to read: ")



for i in range(int(pages) * page1):
    line = sourcefile.readline()
    destnatefile.write(line)
