sourcefile = open("Book1.txt","r")
destnatefile = open("copybook.txt","a")
# a = sourcefile.read()
# print(a)
count = 0
page1 = 25
pages = input("Please input how many pages you want to read: ")
print("Choose 1 - Replace o or O with 0(number) and a or A with 4")
print("Choose 2 - Replace e or E with 3 and i or I with 1")
print("Choose 3 - Words ending with (suffix) '-er' ends with '-xor' or '-zor' [ hacker -> h4x0r) ")
choose = input("Please choose the number that you want to make change: ")

for i in range(int(pages) * page1):
    line = sourcefile.readline()
    destnatefile.write(line)
