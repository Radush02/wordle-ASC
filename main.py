import math,os

cuvinte=[]
deGhicit=""
current_try=[]
lg_cuv=len(cuvinte)
meciuriJucate=0
meciuriTotale=0
cuv_optim="TAREI"

def init_cuvinte(i):
    global cuvinte,deGhicit,lg_cuv,current_try
    lista_cuv=open("Cuvinte_wordle.txt","r")
    cuvinte=lista_cuv.read().split()
    lg_cuv = len(cuvinte)
    deGhicit=cuvinte[i]
    current_try=[]
    lista_cuv.close()

if os.path.exists("IPC_Fisier/fin.txt"):
    os.remove("IPC_Fisier/fin.txt")
if os.path.exists("IPC_Fisier/fout.txt"):
    os.remove("IPC_Fisier/fout.txt")
if os.path.exists("solutii.txt"):
    os.remove("solutii.txt")

def jocWordle(incercare,fisier):
    global cuvinte,meciuriJucate,meciuriTotale
    meciuriJucate += 1
    current_try.append(incercare)
    if incercare != deGhicit:
        rez = ""
        for i in range(5):
            if incercare[i] == deGhicit[i]:
                rez += "2"
            elif incercare[i] in deGhicit:
                rez += "1"
            else:
                rez += "0"
        fout = open("IPC_Fisier/fout.txt", "w+")
        print(rez,file=fout)
        fout.seek(0)
        rezultate_obt=fout.read().split()
        fout.close()
        parseRezultat(rezultate_obt[len(rezultate_obt)-1],incercare,fisier)
    else:
        meciuriTotale+=meciuriJucate
        fout = open("IPC_Fisier/fout.txt", "r")
        print(f"{deGhicit}, {', '.join(current_try)}",file=fisier)
        fout.close()
        return

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
    fin = open("IPC_Fisier/fin.txt", "w+")
    print(incercare, file=fin)
    fin.seek(0)
    cuvinte_obtinute=fin.read().split()
    fin.close()
    jocWordle(cuvinte_obtinute[len(cuvinte_obtinute)-1],fisier)


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


def main():
    global meciuriJucate
    f = open("solutii.txt", "a+")
    lg_cuv = 11454
    for i in range(0,lg_cuv):
        meciuriJucate=0
        init_cuvinte(i)
        jocWordle(cuv_optim,f)
        print(deGhicit,*current_try,meciuriJucate)
    print(f"Medie: {meciuriTotale/lg_cuv}")

if __name__=="__main__":
    main()