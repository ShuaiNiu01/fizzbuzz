


def unique_words():
    book1 = open("Book1.txt","r")
    book2 = open("Book2.txt","r")
    book3 = open("Book3.txt","r")
    file = open("20k.txt","r")
    count1 = 0
    lst = []
    for i in book1:
        for j in file:

            bookline = book1.readline()
            textline = file.readline()
            if textline in bookline:
                lst.append(textline)
                
