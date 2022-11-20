from urllib.request import urlopen
import random
from multiprocessing import Process
import math
import time
import os


cuvinte=[]
deGhicit=""
def init_cuvinte():
    try:
        global cuvinte,deGhicit,lg_cuv
        data = urlopen("https://cs.unibuc.ro/~crusu/asc/cuvinte_wordle.txt")
        cuvinte=[]
        for line in data:
            cuvinte.append(str(line)[2:7])
        cuvinte=cuvinte[:len(cuvinte)-1]
        lg_cuv = len(cuvinte)
        deGhicit=cuvinte[random.randint(0,len(cuvinte)-1)]
    except:
        print("Nu exista conexiune la internet pt a lua lista de cuvinte.")
        exit()

cnt_jocuri=0
lg_cuv=len(cuvinte)
fin=open("fin.txt","w")
fout=open("fout.txt","w")
def jocWordle(incercare,fisier):
    global cuvinte,meciuriJucate,meciuriTotale
    meciuriJucate += 1
    rez = ""
    for i in range(5):
        if incercare[i] == deGhicit[i]:
            rez += "2"
        elif incercare[i] in deGhicit:
            rez += "1"
        else:
            rez += "0"
    print(rez,file=fout)
    parseRezultat(rez,incercare,fisier)

def parseRezultat(rez,incercare,fisier):
    global cuvinte
    for i in range(5):
        if rez[i] == "0":
            cuvinte = ([cuv for cuv in cuvinte if incercare[i] not in cuv])
        elif rez[i] == "2":
            cuvinte = ([cuv for cuv in cuvinte if incercare[i] == cuv[i]])
        elif rez[i] == "1":
            cuvinte = ([cuv for cuv in cuvinte if incercare[i] in cuv])
    try:
        cuvinte.remove(incercare)
    except:
        pass
    incercare = getEntropie()
    print(incercare, file=fisier)
    print(incercare, file=fin)
    if incercare is deGhicit:
         print(f"Cuvantul era {deGhicit}, ghicit in {meciuriJucate} incercari")
         exit()
    else:
         jocWordle(incercare,fisier)
meciuriJucate=0
meciuriTotale=0
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
    entropie = {}
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
        entropie[x]=ent
    return max(entropie,key=entropie.get)


cuv_optim="TAREI"
def main():
    global meciuriJucate
    if os.path.exists("solutii.txt"):
        os.remove("solutii.txt")
    f = open("solutii.txt", "a")
    print(cuv_optim,file=f)
    init_cuvinte()
    jocWordle(cuv_optim,f)

if __name__=="__main__":
    main()