from urllib.request import urlopen
import random
import math
import os

cuvinte=[]
deGhicit=""
cnt_jocuri=0

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

lg_cuv=len(cuvinte)
if os.path.exists("IPC_Fisier/fin.txt"):
    os.remove("IPC_Fisier/fin.txt")
if os.path.exists("IPC_Fisier/fout.txt"):
    os.remove("IPC_Fisier/fout.txt")
if os.path.exists("solutii.txt"):
    os.remove("solutii.txt")

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
    fout = open("IPC_Fisier/fout.txt", "a+")
    print(rez,file=fout)
    fout.seek(0)
    rezultate_obt=fout.read().split()
    parseRezultat(rezultate_obt[len(rezultate_obt)-1],incercare,fisier)

def parseRezultat(rez,incercare,fisier):
    global cuvinte
    for i in range(5):
        if rez[i] == "0":
            cuvinte = ([cuv for cuv in cuvinte if incercare[i] not in cuv])
        elif rez[i] == "2":
            cuvinte = ([cuv for cuv in cuvinte if incercare[i] == cuv[i]])
        elif rez[i] == "1":
            cuvinte = ([cuv for cuv in cuvinte if incercare[i] in cuv and incercare[i] != cuv[i]])
    try:
        cuvinte.remove(incercare)
    except:
        pass
    incercare = getEntropie()
    print(incercare, file=fisier)
    fin = open("IPC_Fisier/fin.txt", "a+")
    print(incercare, file=fin)
    if incercare is deGhicit:
        fisier.seek(0)
        cuvinte_obtinute = fisier.read().split()
        print(*cuvinte_obtinute)
        fout = open("IPC_Fisier/fout.txt", "r")
        print(*fout.read().split())
        print(f"Cuvantul era {deGhicit}, ghicit in {meciuriJucate} incercari")
        exit()
    else:
        fin.seek(0)
        cuvinte_obtinute=fin.read().split()
        jocWordle(cuvinte_obtinute[len(cuvinte_obtinute)-1],fisier)
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
    f = open("solutii.txt", "a+")
    print(cuv_optim,file=f)
    init_cuvinte()
    jocWordle(cuv_optim,f)

if __name__=="__main__":
    main()