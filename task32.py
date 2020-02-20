list1 = ["a", "the", "at", "run", "to","and","are","or","for","an","this"]

def count_the_article(list):
    lst2 = []
    for i in list:
        for j in i:
            lst2.append(j)


count_the_article(list1)
