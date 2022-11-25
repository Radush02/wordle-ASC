# Echipa

Cordunianu Radu - Grupa 133  
Tilica Gabriel - Grupa 133  
## Descriere
Folosindu-ne de entropia Shannon, calculam cantitatea de informatie obtinuta de fiecare rezultat.
Initial s-a calculat pentru toate cuvintele din lista data, rezultatul fiind <b>TAREI</b>.
<br><br>Dupa ce am obtinut cuvantul ce ne ofera numarul maxim de biti de informatie, acesta va fi citit dintr-un fisier pentru a observa rezultatul jocului.
Rezultatul obtinut pentru cuvantul cu nr. maxim de biti va fi transmis intr-un alt fisier.
<br><br>
Pe baza rezultatului obtinut vor fi 3 cazuri:<br>
<ul>
<li>Cazul 0: Litera <b>nu</b> este in cuvant. Se vor sterge toate cuvintele ce contin acea litera.</li>
<li>Cazul 1: Litera este in cuvant, dar nu este pe pozitia corecta. Se vor pastra doar cuvintele ce contin acea litera oriunde in cuvant, insa se vor sterge toate cuvintele ce au litera respectiva pe pozitia indicata.</li>
<li>Cazul 2: Litera este in cuvant si este pe pozitia corecta. Se vor pastra doar cuvintele ce contin litera respectiva pe pozitia respectiva.</li>
</ul>

Se va rula programul pana cand va ramane un singur cuvant in lista de cuvinte, cel ce trebuie ghicit.
## Rezultate obtinute
Cuvantul cu entropia maxima este <b>TAREI</b>  
![Entropie maxima](https://cdn.discordapp.com/attachments/954523115055120455/1043996015117733950/tarei.png)

<a href="https://gist.githubusercontent.com/Radush02/65941f6ea83ba117d7d9e203df0552af/raw/8553de5050b741e9889ade49509839587de96e0d/gistfile1.txt">Lista cu numarul de incercari obtinut pentru fiecare cuvant</a><br>
Numarul mediu de incercari: 4.373 
<img src="https://cdn.discordapp.com/attachments/954523115055120455/1045785583617851513/optimizat.png" width=60% height=60% style="display: block; margin-left: auto; margin-right: auto;">


## Referinte
<a href="https://www.youtube.com/watch?v=v68zYyaEmEA">Solving Wordle using information theory - 3Blue1Brown on Youtube</a><br>
<a href="https://towardsdatascience.com/information-theory-applied-to-wordle-b63b34a6538e"> Information Theory Applied to Wordle - Diego Unzueta</a><br>
<a href="https://cs.unibuc.ro/~crusu/asc/Arhitectura%20Sistemelor%20de%20Calcul%20(ASC)%20-%20Curs%200x02.pdf">Introducere In Teoria Informatiei - Cristian Rusu</a>