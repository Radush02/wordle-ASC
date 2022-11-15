from urllib.request import urlopen
import random
from multiprocessing import Process
import math
import time
import os
data=urlopen("https://cs.unibuc.ro/~crusu/asc/cuvinte_wordle.txt")

cuvinte=[]
for line in data:
    cuvinte.append(str(line)[2:7])
cuvinte=cuvinte[:len(cuvinte)-1]
deGhicit=cuvinte[random.randint(0,len(cuvinte)-1)]

lg_cuv=len(cuvinte)
apr=dict([(chr(i), 0) for i in range(65, 91)])
def jocWordle(x):
    try:
        while x != deGhicit:
            for i in deGhicit:
                apr[i]+=1
            rez = ""
            for i in  range(5):
                if x[i] == deGhicit[i]:
                    apr[x[i]]-=1
                    rez += "2"
                elif apr[x[i]] > 0 and x[i] in deGhicit:
                    rez += "1"
                    apr[x[i]]-=1
                else:
                    rez += "0"
                # print(apr)
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
    if os.path.exists("entropie.txt"):
        os.remove("entropie.txt")
    with open("entropie.txt","a") as f:
        for x in cuvinte:
            start=time.time()
            for i in back:
                back[i]=0
            for deGhicit in cuvinte:
                rez=""
                for i in range(5):
                            if x[i] == deGhicit[i]:
                                rez += "2"
                            elif x[i] in deGhicit[i:]:
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
    x=str(input("Cuvant= "))
    x=x.upper()
    jocWordle(x)
    # getEntropie()

if __name__=="__main__":
    main()


