import csv

def verify_data():
    GOOD = []
    POOR = []
    MARGINAL = []
    csvfile = open("Trails.csv","r")
    reader = csv.reader(csvfile)
    for item in reader:
        if reader.line_num == 1:
            continue
        if item[9] == "GOOD":
            GOOD.append(item[1])
        if item[9] == "POOR":
            POOR.append(item[1])
        if item[9] == "MARGINAL":
            MARGINAL.append(item[1])
    print("GOOD: ",GOOD)
    print("POOR:",POOR)
    print("MARGINAL: ",MARGINAL)
    csvfile.close()
# verify_data()

def after2000():
    lst2000 = []
    csvfile = open("Trails.csv","r")
    reader = csv.reader(csvfile)
    for item in reader:
        if reader.line_num == 1:
            continue
        elif item[10] == '':
            continue
        intnum = int(item[10])
        if intnum >= 2000:
            lst2000.append(item[1])
    csvfile.close()
    print(lst2000)
    return lst2000
# after2000()

def count_trails():
    count0 = 0
    count1 = 0
    count2 = 0
    csvfile = open("Trails.csv","r")
    reader = csv.reader(csvfile)
    for item in reader:
        if reader.line_num == 1:
            continue
        if item[15] == "ACTIVE":
            count0 += 1
        elif item[12] == 'Yes':
            count1 += 1
        elif item[23] == "Yes":
            if item[25] == "Yes":
                count2 += 1
    csvfile.close()
    print("{} trails are currently Active".format(count0))
    print("{} have lighting".format(count1))
    print("{} are both 'Walking' and have 'Biking'".format(count2))
# count_trails()

def tuple_infor():
    lst = []
    csvfile = open("Trails.csv","r")
    reader = csv.reader(csvfile)
    for item in reader:
        if reader.line_num == 1:
            continue
        if item[24] == "Yes"
            if item[25] == "Yes"
                sub_tup = (item[2],item[9],item[12],item[15],item[24],item[25])
        lst.append(sub_tup)
    tup1 = tuple(lst)
    print(tup1)
    return tup1
