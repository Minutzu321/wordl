
# :large_orange_diamond: Wordle - Proiect Arhitectura Sistemelor de Calcul

Proiectul este facut in framework-ul **Django**.\
Acesta consta intr-un joc de tip wordle si un bot care rezolva jocul folosind teoria informatiei.\
Acesta are **interfata grafica** si poate fi jucat de o persoana sau controlul poate fi dat algoritmului care incearca sa il rezolve.\
:bangbang: Incarcarea partii de frontend dureaza aproximativ **50 de secunde** intrucat se genereaza lista de posibilitati pentru fiecare cuvant.\
:bangbang: Din cauza naturii limbajului javascript si a incarcarii cuvintelor care ocupa multa memorie RAM, se poate cauza un crash al paginii daca nu este destula memorie pentru tab-ul browserului.


## :notebook_with_decorative_cover: Cuprins
- [Alcatuire](https://github.com/Minutzu321/wordl#hammer_and_wrench-alcatuirea-proiectului)
- [Comunicare](https://github.com/Minutzu321/wordl#speech_balloon-comunicarea)
- [Executare](https://github.com/Minutzu321/wordl#pray-executarea-programului)
- [Rezultate](https://github.com/Minutzu321/wordl#memo-rezultate)
- [Surse](https://github.com/Minutzu321/wordl/#eyes-surse)
- [Echipa](https://github.com/Minutzu321/wordl#busts_in_silhouette-echipa)


### :hammer_and_wrench: Alcatuirea proiectului
 - Primul program se afla pe serverul de python si actioneaza ca backend pentru joc. Aici se aplica logica si se da un feedback programului care incearca sa rezolve jocul.
 - Al doilea program care actioneaza ca frontend este servit tot de serverul de python insa sub forma de html, js si css. Algoritmul de rezolvare prin aplicarea teoriei informatiei este scris in javascript si incarca cu ajutorul unor "Workeri" o lista foarte mare de cuvinte care contine toate permutarile patternurilor unui cuvant.


### :speech_balloon: Comunicarea
Comunicarea intre cele doua programe se face prin intermediul unui API care la request are cuvantul ghicit iar ca raspuns are patternul dat de raspunsul adevarat si cel ghicit.
```
Exemplu
Patternul dintre AAAAB(cuvant corect) si AAABC(cuvant ghicit) este "22210"
2 - litera pe pozitie buna
1 - litera se afla in cuvant dar nu e pe pozitia buna
0 - litera nu se afla in cuvant
```
### :pray: Executarea programului
Pentru a instala framework-ul, comanda este
```
pip install -r requirements.txt
```
Pentru a porni serverul web, comanda este
```
python manage.py runserver
```
iar adresa la care raspunde serverul este
```
http://127.0.0.1:8000/
```
### :memo: Rezultate
Medie incercari: **4.52**\
Fisier cuvinte: [https://github.com/Minutzu321/wordl/blob/master/rezultate.txt](https://github.com/Minutzu321/wordl/blob/master/rezultate.txt)

### :eyes: Surse
 - [3Blue1Brown - Solving Wordle using information theory](https://www.youtube.com/watch?v=v68zYyaEmEA&ab_channel=3Blue1Brown)
 - [https://github.com/GillesVandewiele/Wordle-Bot](https://github.com/GillesVandewiele/Wordle-Bot)
 - [https://github.com/atoppi/simple-wordle-solver](https://github.com/atoppi/simple-wordle-solver)

### :busts_in_silhouette: Echipa
- Chiruș Mina-Sebastian - Grupa 142
- Dobromirescu Mihaela - Grupa 142
- Iacob Victor-Gabriel - Grupa 142
- Pincu Iulia Maria Andreea - Grupa 142
