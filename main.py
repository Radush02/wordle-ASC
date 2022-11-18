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

cnt_jocuri=0
lg_cuv=len(cuvinte)
def jocWordle(incercare):
    try:
        global cuvinte
        global meciuriJucate
        while incercare != deGhicit:
            meciuriJucate += 1
            rez = ""
            for i in  range(5):
                if incercare[i] == deGhicit[i]:
                    rez += "2"
                elif incercare[i] in deGhicit:
                    rez += "1"
                else:
                    rez += "0"
            print(str(rez))
            print(f"d: {deGhicit}")
            for i in range(5):
                if rez[i]=="0":
                    cuvinte=([cuv for cuv in cuvinte if incercare[i] not in cuv])
                elif rez[i]=="2":
                    cuvinte=([cuv for cuv in cuvinte if incercare[i] == cuv[i]])
                elif rez[i]=="1":
                    cuvinte=([cuv for cuv in cuvinte if incercare[i] in cuv])
            try:
                cuvinte.remove(incercare)
            except:
                pass
            print(f"Cuvant optim: {getEntropie()}")
            incercare = str(input("Cuvant= "))
            incercare = incercare.upper()
        else:
            print(f"Cuvantul era {deGhicit}, ghicit in {meciuriJucate} incercari")
    except IndexError:
        incercare=incercare[:4]
        jocWordle(incercare)

meciuriJucate=0
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


def getEntropie():
    if os.path.exists("entropie.txt"):
        os.remove("entropie.txt")
    entropie = {}
    with open("entropie.txt","a") as f:
        for x in cuvinte:
            for i in back:
                back[i]=0
            for deGhicit in cuvinte:
                rez=""
                for i in range(5):
                            if x[i] == deGhicit[i]:
                                rez += "2"
                            elif x[i] in deGhicit:
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
            print(x,ent,file=f)
            entropie[x]=ent
    return max(entropie,key=entropie.get)


cuv_optim="TAREI"
def main():
    # x=str(input("Cuvant= "))
    # x=x.upper()
    jocWordle(cuv_optim)

if __name__=="__main__":
    main()
