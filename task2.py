sourcefile = open("20k.txt","r")
destnatefile = open("copybook.txt","a")

def change_str1(line):
    for i in line:
        if 'o' in line:
            index1 = line.find('o')
            line = line[:index1] + '0' + line[index1+1:]
        elif 'O' in line:
            index2 = line.find('O')
            line = line[:index2] + '0' + line[index2+1:]
        elif 'a' in line:
            index3 = line.find('a')
            line = line[:index3] + '4' + line[index3+1:]
        elif 'A' in line:
            index4 = line.find('a')
            line = line[:index4] + '4' + line[index4+1:]
    return line

def change_str2(line):
    for i in line:
        if 'o' in line:
            index1 = line.find('o')
            line = line[:index1] + '0' + line[index1+1:]
        elif 'O' in line:
            index2 = line.find('O')
            line = line[:index2] + '0' + line[index2+1:]
        elif 'a' in line:
            index3 = line.find('a')
            line = line[:index3] + '4' + line[index3+1:]
        elif 'A' in line:
            index4 = line.find('a')
            line = line[:index4] + '4' + line[index4+1:]
    return line

count = 0
page1 = 25
pages = input("Please input how many pages you want to read: ")
print("Choose 1 - Replace o or O with 0(number) and a or A with 4")
print("Choose 2 - Replace e or E with 3 and i or I with 1")
print("Choose 3 - Words ending with (suffix) '-er' ends with '-xor' or '-zor' [ hacker -> h4x0r) ")
choose = input("Please choose the number that you want to make change: ")

for i in range(int(pages) * page1):
    line = sourcefile.readline()
    if choose == '1':
        line = change_str1(line)
    else:
        print("Choose wrong")
    if choose == '2':
        line = change_str2(line)
    else:
        print("Choose wrong")
    if choose == '3':
        line = change_str3(line)
    else:
        print("Choose wrong")
    destnatefile.write(line)
