from urllib.request import urlopen
import random
from multiprocessing import Process


data=urlopen("https://cs.unibuc.ro/~crusu/asc/cuvinte_wordle.txt")
cuvinte=[]
for line in data:
    cuvinte.append(str(line)[2:7])
cuvinte=cuvinte[:len(cuvinte)-1]
deGhicit=cuvinte[random.randint(0,len(cuvinte)-1)]

apr=[]
for i in range(5):
    apr.append(dict([(chr(i), 0) for i in range(65, 91)]))
for c in cuvinte:
    for i in range(5):
        apr[i][c[i]]+=1

def jocWordle(x):
    try:
        aux=deGhicit
        while x != deGhicit:
            rez = ""
            for i in range(0, 5):
                if x[i] == deGhicit[i]:
                    rez += "2"
                else:
                    rez += "0"
            print(str(rez))
            x = str(input("Cuvant= "))
            x = x.upper()
        else:
            print(f"Cuvantul era {deGhicit}")
    except IndexError:
        x=x[:4]
        jocWordle(x)

def main():
    for i in range(5):
        apr[i]=dict(sorted(apr[i].items(),reverse=True, key=lambda item: item[1]))
        print(apr[i])

if __name__=="__main__":
    main()


