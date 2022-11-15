from urllib.request import urlopen
import random
from multiprocessing import Process
import math
import time
data=urlopen("https://cs.unibuc.ro/~crusu/asc/cuvinte_wordle.txt")

cuvinte=[]
for line in data:
    cuvinte.append(str(line)[2:7])
cuvinte=cuvinte[:len(cuvinte)-1]
deGhicit=cuvinte[random.randint(0,len(cuvinte)-1)]

lg_cuv=len(cuvinte)
apr=[]
inf=[]
for i in range(5):
    apr.append(dict([(chr(i), 0) for i in range(65, 91)]))
    inf.append(dict([(chr(i), 0) for i in range(65, 91)]))
for c in cuvinte:
    for i in range(5):
        apr[i][c[i]]+=1

def getInformatie(apr):#apartia fiecare litere in totalul de cuvinte
    temp = 0
    for x in apr:
        total=len(cuvinte)
        for k in x:
            try:
                inf[temp][k]=math.log2(total/x[k])
            except ZeroDivisionError:
                inf[temp][k]=0
        temp+=1
    for i in range(5):
        inf[i]=dict(sorted(inf[i].items(), key=lambda item: item[1]))
        print(inf[i])



def jocWordle(x):
    try:
        aux=deGhicit
        while x != deGhicit:
            rez = ""
            for i, litera in enumerate(x):
                if x[i] == deGhicit[i]:
                    rez += "2"
                elif litera in deGhicit[i:]:
                    rez += "1"
                else:
                    rez += "0"
            print(str(rez))
            print(f"d: {deGhicit}")
            x = str(input("Cuvant= "))
            x = x.upper()
        else:
            print(f"Cuvantul era {deGhicit}")
    except IndexError:
        x=x[:4]
        jocWordle(x)


back={}
a = [None] * 5
def afis(a,n):
    b=""
    for i in range(n):
        b+=a[i]
    back[b]=0
def genlist(n,a,i):
    if i==n:
        afis(a,n)
        return
    a[i]="0"
    genlist(n,a,i+1)
    a[i]="1"
    genlist(n,a,i+1)
    a[i]="2"
    genlist(n,a,i+1)
genlist(5,a,0)
entropie={}
print("Citit fisier!")


def getEntropie():
    with open("entropie.txt","a") as f:
        for x in cuvinte:
            start=time.time()
            for i in back:
                back[i]=0
            for deGhicit in cuvinte:
                rez=""
                for i, litera in enumerate(x):
                            if x[i] == deGhicit[i]:
                                rez += "2"
                            elif litera in deGhicit[i:]:
                                rez += "1"
                            else:
                                rez += "0"
                back[rez]+=1
            ent=0
            for i in back:
                p_i=back[i]/lg_cuv
                try:
                    ent+=p_i*math.log2(1/p_i)
                except ZeroDivisionError:
                    ent+=0
            print(time.time()-start)
            print(x,ent,file=f)
            entropie[x]=back
def main():
    # x=str(input("Cuvant= "))
    # x=x.upper()
    # jocWordle(x)
    # for i in range(5):
    #       apr[i]=dict(sorted(apr[i].items(),reverse=True, key=lambda item: item[1]))
    #       print(apr[i])
    #getInformatie(apr)
    getEntropie()

if __name__=="__main__":
    main()


