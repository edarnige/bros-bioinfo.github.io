# Arbres 


## Définitions

Un arbre est une structure de donnée A contenant des éléments, tous distincts, appelés sommets et muni des fonctions suivantes: 
+ la **fonction fils(A,p)**  qui prend en paramètre un arbre A et un sommet p de l'arbre A, et qui renvoie une liste de sommets de A. Ces sommets sont appelés les **fils** de p.
+ la **fonction pere(A,f)** qui prend en paramètre un arbre A, un sommet f de A et renvoie un sommet de A ou "None". Le sommet envoyé est appélé le **père** de f. 
+ la fonction racine(A) qui prends en paramètre un arbre A et renvoie un sommet de A appelé racine de A.

Pour que (A,racine,fils,pere) soit un arbre, il faut que les propriétés suivantes soient vérifiées : 
+ la fonction racine(A) prends en paramètre un arbre A et renvoie un sommet de A appelé racine ou None si A est vide.
+ Par convention on étend pere de sorte que pere(A,None) = None.
1. Une racine n'a pas de père : père(A,racine(*)) = None.
2. Tout sommet a un père à l'exception de la racine : **&forall;s &isin;A/{racine(A)}  pere(A,s)&isin;A** &rarr; Traduction : pour tout sommet s de A privé des éléments de l'ensemble qui ne contient que la racine A.


![Arbre](https://user.oc-static.com/files/166001_167000/166664.png)
Ref : [Openclassroom : Algo](https://openclassrooms.com/courses/algorithmique-pour-l-apprenti-programmeur/arbres?q=&hPP=8&idx=prod_v2_COURSES_en&p=0&fR%5Bcertificate%5D%5B0%5D=true&fR%5BisWeb%5D%5B0%5D=true)

3. Les fils d'un sommet s ont pour père s, et le pere p d'un sommet s admet s comme fils. 
 - **&forall;s &isin;A, &forall;f &isin;fils(A,s)  pere(A,f) = s** &rarr; Traduction : pour tout sommet de A, pour tout sommert appartenant aux fils de s, le pere de f est s.
 - **&forall;s &isin;&mu;, &forall;p &isin;pere(A,&mu;)  &mu;&isin;fils(A,p)**
4. Il ya un unique sommet s tels que pere(s) = None et le sommet est la racine.
5. A partir de tout sommet, on peut accéder à la racine par la relation de paternité. **&forall;s &isin;A, &ni;k&isin;N  pere<sup>k</sup>(A,s) = None**. Où pere<sup>k</sup> se définit récursivement par : 
    + pere<sup>0</sup>(A,s) = s
    + pere<sup>k</sup>(A,s) = pere(pere<sup>k-1</sup>(A,s))


*Exemple* : 

Est-ce que le quadruplet(A,racine,pere,fils) est un arbre ? Si oui dessinez le : 

+ A = {1,2,8,9,5,7}
+ pere : 
    - 9:1
    - 2:9
    - 5:9
    - 7:None
    - 1:2
    - 8:9
+ racine(A) = 7
+ fils : 
    - 1:{9}
    - 2:{1}
    - 9:{2,5}
    - 5:{}
    - 8:{}
    - 7:{}

Non ce n'est pas un arbre car la règle 5 n'est pas vérifiée : pere(pere(pere(2))) = 2. De plus la règle 3 n'est pas vérifiée non plus : pere(8)=9 et 8&notin;fils(9).

*Exercice* : 
Est-ce que le quadruplet(A,racine,pere,fils) est un arbre ? Si oui dessinez le : 

+ A = {a,1,'toto',9}
+ pere : 
    - a:1
    - 9:1
    - 1:'toto'
    - 'toto'=None
+ racine(A) = 'toto'
+ fils : 
    - a:{}
    - 1:{a,9}
    - 'toto':{1}
    - 9:{}

**Attention** : Pour l'instant nos arbres n'ont pas d'étiquettes !!

*Exercice* : 
Retranscrire un arbre en quadruplet : 

+ A{0,1,2,3,5,4}
+ pere : 
    - 0:None
    - 1:0
    - 2:0
    - 3:2
    - 5:2
    - 4:2
+ fils :
    - 0:{1,2}
    - 1:{}
    - 2:{3,5,4}
    - 3:{}
    - 4:{}
    - 5:{}

**Note** : un arbre vide renvoie None.

A = {}
racine(A) = None
pere(A,s) = {}
fils(A,p) = {}

*Arbre dans un arbre* : 

+ A = {a&rarr;(A={0,1,2};racine = 0 ; pere{0:None;1:0;2:0};fils : {0:{1,2};1:{};2:{}})}) ; b&rarr;(A = &empty;; racine = None, pere:{}; fils:{})}

**En python** : 

```py
def creer_arbre_vide():
    A=[]
    pere = {}
    fils = {}
    racine = None
    return [A,pere,fils,racine]

def ajouter_racine(T,s):
    #ajoute dans A un sommet
    #s et le définis comme une 
    #racine
    T[0].append(s)
    T([][s]) = None
    T([2][s]) = {}
    T([3][s]) = s

def ajouter_sommet(T,s,p):
    #ajoute dans T le sommets
    #et definit p comme son père
    #p existe dans T
    #s n'exsire pas dans T
```