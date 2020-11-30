import random
from itertools import combinations
str1 = "kanan atas"
tile1 = "(user ?z1 ?z2 ?val1)" +" \n   "
tiles1 = "(unknown ?z1 ?z2 ?val1)" +" \n   "
assertTile1= "(assert (flag ?z1 ?z2))" +" \n   "
flag1 = "(flag ?z1 ?z2)" +" \n   "

str2 = "atas"
tile2 = "(user ?x ?z2 ?val2)" +" \n   "
tiles2 = "(unknown ?x ?z2 ?val2)" +" \n   "
assertTile2= "(assert (flag ?x ?z2))" +" \n   "
flag2 = "(flag ?x ?z2)" +" \n   "

str3 = "kiri atas"
tile3 = "(user ?z3 ?z2 ?val3)" +" \n   "
tiles3 = "(unknown ?z3 ?z2 ?val3)" +" \n   "
assertTile3= "(assert (flag ?z3 ?z2))" +" \n   "
flag3 = "(flag ?z3 ?z2)" +" \n   "

str4 = "kiri"
tile4 = "(user ?z3 ?y ?val4)" +" \n   "
tiles4 = "(unknown ?z3 ?y ?val4)" +" \n   "
assertTile4= "(assert (flag ?z3 ?y))" +" \n   "
flag4 = "(flag ?z3 ?y)" +" \n   "

str5 = "kiri bawah"
tile5 = "(user ?z3 ?z4 ?val5)" +" \n   "
tiles5 = "(unknown ?z3 ?z4 ?val5)" +" \n   "
assertTile5= "(assert (flag ?z3 ?z4))" +" \n   "
flag5 = "(flag ?z3 ?z4)" +" \n   "

str6 = "bawah"
tile6 = "(user ?x ?z4 ?val6)" +" \n   "
tiles6 = "(unknown ?x ?z4 ?val6)" +" \n   "
assertTile6= "(assert (flag ?x ?z4))" +" \n   "
flag6 = "(flag ?x ?z4)" +" \n   "

str7 = "kanan bawah"
tile7 = "(user ?z1 ?z4 ?val7)" +" \n   "
tiles7 = "(unknown ?z1 ?z4 ?val7)" +" \n   "
assertTile7= "(assert (flag ?z1 ?z4))" +" \n   "
flag7 = "(flag ?z1 ?z4)" +" \n   "

str8 = "kanan"
tile8 = "(user ?z1 ?y ?val8)" +" \n   "
tiles8 = "(unknown ?z1 ?y ?val8)" +" \n   "
assertTile8= "(assert (flag ?z1 ?y))" +" \n   "
flag8 = "(flag ?z1 ?y)" +" \n   "

listOfTile = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8]
listOfTiles = [tiles1, tiles2, tiles3, tiles4, tiles5, tiles6, tiles7, tiles8]
listOfAssert = [assertTile1, assertTile2, assertTile3, assertTile4, assertTile5, assertTile6, assertTile7, assertTile8]
listOfFlag = [flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8]
listOfNum = [0,1,2,3,4,5,6,7]

#n = int(input("Masukkan n: "))
f = open("file-rule-1.txt", "w")
f.close()
for n in range(1,5):
    comb = combinations(listOfNum, n)
    combinators = []
    ids = 1
    f = open("file-rule-1.txt", "a")
    for i in list(comb): 
        for idx in range(len(i)):
            #flag combinations
            idz = 1
            if(idx==0):
                isi = "(defrule rule-1-val" + str(n) +"-" + str(ids) + "-flag" + str(idx) +"-" + str(idz) +" \n   "
                isi += "(user ?x ?y " + str(n) +")" +" \n   "
                isi += "(lokasi1 ?x ?y)" +" \n   "
                for j in range (8):
                    if j not in i:
                        isi += listOfTile[j]
                for j in range(len(i)):
                    isi += listOfTiles[i[j]]  
                isi += "(test (= ?z1 (+ ?x 1)))" +" \n   "
                isi += "(test (= ?z3 (- ?x 1)))" +" \n   "
                isi += "(test (= ?z2 (+ ?y 1)))" +" \n   "
                isi += "(test (= ?z4 (- ?y 1)))" +" \n   "
                isi += "=> \n   "
                for j in range(len(i)):
                    isi += listOfAssert[i[j]]
                isi += ") \n\n"
                combinators.append(isi)
                idz +=1
            else:
                comb2 = combinations(i, idx)
                for v in list(comb2):
                    isi = "(defrule rule-1-val" + str(n) +"-" + str(ids) + "-flag" + str(idx) +"-" + str(idz) +" \n   "
                    isi += "(user ?x ?y " + str(n) +")" +" \n   "
                    isi += "(lokasi1 ?x ?y)" +" \n   "
                    for j in range(len(v)):
                        isi += listOfFlag[v[j]]
                    for j in range (8):
                        if j not in i:
                            isi += listOfTile[j]
                    for j in range(len(i)):
                        if i[j] not in v:
                            isi += listOfTiles[i[j]]        
                    isi += "(test (= ?z1 (+ ?x 1)))" +" \n   "
                    isi += "(test (= ?z3 (- ?x 1)))" +" \n   "
                    isi += "(test (= ?z2 (+ ?y 1)))" +" \n   "
                    isi += "(test (= ?z4 (- ?y 1)))" +" \n   "
                    isi += "=> \n   "
                    for j in range(len(i)):
                        if i[j] not in v:
                            isi += listOfAssert[i[j]]
                    isi += ") \n\n"
                    combinators.append(isi)
                    idz +=1
        ids += 1
    for i in combinators:
        f.write(i)
    f.close()
'''
for n in range(1,9):
    comb = combinations(listOfNum, n)
    combinators = []
    idx = 1
    f = open("file-rule-1.txt", "a")
    for i in list(comb): 
        isi = "(defrule rule-1-val" + str(n) +"-" + str(idx) +" \n   "
        isi += "(user ?x ?y " + str(n) +")" +" \n   "
        isi += "(lokasi1 ?x ?y)" +" \n   "
        for j in range (8):
            if j not in i:
                isi += listOfTile[j]
        if 0 not in i or 6 not in i or 7 not in i:
            isi += "(test (= ?z1 (+ ?x 1)))" +" \n   "
        if 2 not in i or 3 not in i or 4 not in i:
            isi += "(test (= ?z3 (- ?x 1)))" +" \n   "
        if 0 not in i or 1 not in i or 2 not in i:
            isi += "(test (= ?z2 (+ ?y 1)))" +" \n   "
        if 4 not in i or 5 not in i or 6 not in i:
            isi += "(test (= ?z4 (- ?y 1)))" +" \n   "
        isi += "=> \n   "
        for j in range(len(i)):
            isi += listOfAssert[i[j]]
        isi += ") \n\n"
        combinators.append(isi)
        idx += 1
    for i in combinators:
        f.write(i)
    f.close()
'''
'''
for i in range(len(list(comb))):
    check = []
    isi = "(defrule rule-1-val" + str(n) +"-" + str(i+1) +" \n   "
    isi += "(user ?x ?y " + str(n) +")" +" \n   "
    for j in range (8-n):
        rand = random.choice(listOfTile)
        while listOfTile.index(rand) not in check:
            rand = random.choice(listOfTile)
        check.append(listOfTile.index(rand))
        isi += rand
    if 0 not in check or 6 not in check or 7 not in check:
        isi += "(test (= ?z1 (+ ?x 1)))" +" \n   "
    if 2 not in check or 3 not in check or 4 not in check:
        isi += "(test (= ?z3 (- ?x 1)))" +" \n   "
    if 0 not in check or 1 not in check or 2 not in check:
        isi += "(test (= ?z2 (+ ?y 1)))" +" \n   "
    if 4 not in check or 5 not in check or 6 not in check:
        isi += "(test (= ?z4 (- ?y 1)))" +" \n   "
    for item in listOfTile:
        if listOfTile.index(item) not not in check:
            check.append(listOfTile.index(item))
            isi += listOfTiles[listOfTile.index(item)]
    isi += "=> \n   "
    for j in range(n):
        isi += listOfAssert[check[len(check)-j-1]]
    isi += ") \n"
    while check in combinatorsNum:
        isi = "(defrule rule-1-val" + str(n) +"-" + str(i+1) +" \n   "
        isi += "(user ?x ?y " + str(n) +")" +" \n   "
        for j in range (8-n):
            rand = random.choice(listOfTile)
            while listOfTile.index(rand) not in check:
                rand = random.choice(listOfTile)
            check.append(listOfTile.index(rand))
            isi += rand
        if 0 not in check or 6 not in check or 7 not in check:
            isi += "(test (= ?z1 (+ ?x 1)))" +" \n   "
        if 2 not in check or 3 not in check or 4 not in check:
            isi += "(test (= ?z3 (- ?x 1)))" +" \n   "
        if 0 not in check or 1 not in check or 2 not in check:
            isi += "(test (= ?z2 (+ ?y 1)))" +" \n   "
        if 4 not in check or 5 not in check or 6 not in check:
            isi += "(test (= ?z4 (- ?y 1)))" +" \n   "
        for j in range (n):
            for item in listOfTile:
                if listOfTile.index(item) not not in check:
                    check.append(listOfTile.index(item))
                    isi += listOfTiles[listOfTile.index(item)]
        isi += "=> \n   "
        for j in range(n):
            isi += listOfAssert[check[len(check)-j-1]]
        isi += ") \n"
    combinatorsNum.append(check)
    combinators.append(isi)
for i in combinators:
    print(i)
print(len(combinators))
'''