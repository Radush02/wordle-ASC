from urllib.request import urlopen
import random
data=urlopen("https://cs.unibuc.ro/~crusu/asc/cuvinte_wordle.txt")

cuvinte=[]
for line in data:
    cuvinte.append(str(line)[2:7])

cuvinte=cuvinte[:len(cuvinte)-1]
deGhicit=cuvinte[random.randint(0,len(cuvinte)-1)]

#print(deGhicit)
x=input("Cuvant: ")
while x != deGhicit:
    rez=""
    for i in range(0,5):
        if x[i]==deGhicit[i]:
            rez+="2"
        elif deGhicit.find(x[i]) != -1:
            rez+="1"
        else:
            rez+="0"
    print(str(rez))
    #print(deGhicit)
    x=input("Cuvant: ")
else:
    print(f"Cuvantul era {deGhicit}")