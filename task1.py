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
    csvfile = open("Trails.csv","r")
    reader = csv.reader(csvfile)
    for item in reader:
        if reader.line_num == 1:
            continue
        
