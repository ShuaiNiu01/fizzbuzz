import csv

def verift_data():
    GOOD = []
    POOR = []
    MARGINAL = []
    csvfile = open("Trails.csv","r")
    reader = csv.reader(csvfile1)
    for item in reader:
        if reader1.line_num == 1:
            continue
        if item[9] == "GOOD":
            GOOD.append(item[1])
        if item[9] == "POOR":
            POOR.append(item[1])
        if item[9] == "MARGINAL":
            MARGINAL.append(item[1])
    print(GOOD)
    print(POOR)
    print(MARGINAL)
