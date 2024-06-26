# grammar_esperanto
## Description
in this evidence i have to create a grammar that represents the lenguage Esperanto, make a model of that grammar, do the implementation, test it and realize the complexity analysis. There is not an specific program paradigm for this problem.

Esperanto is a constructed lenguage created by Zamenhof in 1887. The word Esperanto translates into english as "the one who hopes". Esperanto was created with the idea to become the new universal lenguage, sadly that dream won't come true. 

## Model
Some rules of the esperanto grammar are represented in this grammar, at the followings points i'm going to explain that rules in the parts of my grammar. 
```
    E -> Sin | Plu | Mat
    Sin -> SNom | SAcu
    Plu -> PNom | PAcu
    SNom -> SSS | SSS V | ASS SSS | ASS SSS V
    PNom -> SPS | SPS V | APS SPS | APS SPS V
    SAcu -> SSO | SSO V | ASO SSO | ASO SSO V
    PAcu -> SPO | SPO V | APO SPO | APO SPO V
    V -> Vpr | Vfu | Vpa  

    Mat -> N Op Mat | N
    N -> Nu | Nd | Nc | Nd Nu | Nc Nd Nu

    SSS -> 'vulpo' | 'viro' | 'kato'
    SSO -> 'vulpon' | 'viron' | 'katon'
    SPS -> 'vulpoj' | 'viroj' | 'katoj'
    SPO -> 'vulpojn' | 'virojn' | 'katojn'
    ASS -> 'granda' | 'forta' | 'malbela'
    ASO -> 'grandan' | 'fortan' | 'malbelan'
    APS -> 'grandaj' | 'fortaj' | 'malbelaj'
    APO -> 'grandajn' | 'fortajn' | 'malbelajn'
    Vpr -> 'laboras' | 'programas' | 'skulpas'
    Vfu -> 'laboros' | 'programos' | 'skulpos'
    Vpa -> 'laboris' | 'programis' | 'skulpis'

    Op -> 'plus' | 'minus' | 'por' | 'inter'
    Nu -> 'unu' | 'du' | 'tri' | 'kvar' | 'kvin' | 'ses' | 'sep' | 'ok' | 'nau'
    Nd -> 'dek' | 'dudek' | 'tridek' | 'kvardek' | 'kvindek' | 'sesdek' | 'sepdek' | 'okdek' | 'naudek'
    Nc -> 'cent' | 'ducent' | 'tricent' | 'kvarcent' | 'kvincent' | 'sescent' | 'sepcent' | 'okcent' | 'naucent'
```
All starts with E, that represents any sentences. In esperanto we have two posibilities to write a subject and a adjective, nominative and accusative. I also create the grammar to represent a simple math operation, but we are going to see that in a moment.
``` 
    E -> Sin | Plu | Mat
    Sin -> SNom | SAcu
    Plu -> PNom | PAcu
```
Each subject and adjective can only be together with those of the same type, so for each subject and acjective i use this strcture: SSS/APO = "Subject/Adjective Singular/Plural Subject/Object" in order to organaze them. In some cases the sentence is followed by a verb, and that verb can be in present, future or past.
```
    SNom -> SSS | SSS V | ASS SSS | ASS SSS V
    PNom -> SPS | SPS V | APS SPS | APS SPS V
    SAcu -> SSO | SSO V | ASO SSO | ASO SSO V
    PAcu -> SPO | SPO V | APO SPO | APO SPO V
    V -> Vpr | Vfu | Vpa  
```
To represent a methematical expresion i used recurtion, because we can construct a sentence with almost infinite components and it will be correct. An expretion is made by numbres and operations, and the numbers are made by units, dozens and hundreds. 
```
    Mat -> N Op Mat | N
    N -> Nu | Nd | Nc | Nd Nu | Nc Nd Nu
```
Finally to represent each word into the grammar we have to construct them in each rule. 
```
    SSS -> 'vulpo' | 'viro' | 'kato'
    SSO -> 'vulpon' | 'viron' | 'katon'
    SPS -> 'vulpoj' | 'viroj' | 'katoj'
    SPO -> 'vulpojn' | 'virojn' | 'katojn'
    ASS -> 'granda' | 'forta' | 'malbela'
    ASO -> 'grandan' | 'fortan' | 'malbelan'
    APS -> 'grandaj' | 'fortaj' | 'malbelaj'
    APO -> 'grandajn' | 'fortajn' | 'malbelajn'
    Vpr -> 'laboras' | 'programas' | 'skulpas'
    Vfu -> 'laboros' | 'programos' | 'skulpos'
    Vpa -> 'laboris' | 'programis' | 'skulpis'

    Op -> 'plus' | 'minus' | 'por' | 'inter'
    Nu -> 'unu' | 'du' | 'tri' | 'kvar' | 'kvin' | 'ses' | 'sep' | 'ok' | 'nau'
    Nd -> 'dek' | 'dudek' | 'tridek' | 'kvardek' | 'kvindek' | 'sesdek' | 'sepdek' | 'okdek' | 'naudek'
    Nc -> 'cent' | 'ducent' | 'tricent' | 'kvarcent' | 'kvincent' | 'sescent' | 'sepcent' | 'okcent' | 'naucent'
```
## Implementation
To do the implementation of my grammar and to be sure that what i do is correct i use the library of python "nltk" to create a tree of how is constructed each sentence. I also put a .txt file with a lot of correct sentences of esperanto.
[Esperanto](https://github.com/El3Du4Rd0/grammar_esperanto/blob/main/Esperanto.py)
[test](https://github.com/El3Du4Rd0/grammar_esperanto/blob/main/test.txt)
## Test
to test my grammar i'm going to put some valid an some other invalids sentences, for example in my file "Esperanto.py" i use this sentence "unu minus unu minus unu minus unu" that represents a math sentence and is correct. 
```
                E                
                |                 
               Mat               
  ______________|____             
 |    |             Mat          
 |    |     _________|____        
 |    |    |    |        Mat     
 |    |    |    |     ____|____   
 |    |    |    |    |    |   Mat
 |    |    |    |    |    |    |  
 N    |    N    |    N    |    N 
 |    |    |    |    |    |    |  
 Nu   Op   Nu   Op   Nu   Op   Nu
 |    |    |    |    |    |    |  
unu minus unu minus unu minus unu
```
We can also try some other sentences that represent a Singular Nominative case, like "granda vulpo laboras".
```
         E          
         |           
        Sin         
         |           
        SNom        
   ______|______     
  |      |      V   
  |      |      |    
 ASS    SSS    Vpr  
  |      |      |    
granda vulpo laboras
```
And in the other hand we can try the Plural Acusative case, like "fortajn virojn skulpas"
```
          E           
          |            
         Plu          
          |            
         PAcu         
    ______|_______     
   |      |       V   
   |      |       |    
  APO    SPO     Vpr  
   |      |       |    
fortajn virojn skulpas
```
Here are some examples for correct sentences for the grammar:
- vulpo laboras
- viron laboris
- katoj laboros
- vulpojn laboris
- granda kato
- grandan vulpon

Here are some examples for incorrect sentences for the grammar:
- laboras vulpo
- granda granda
- vulpo vulpo
- tri tri tri tri
- unu por por unu
- katon forta laboros

In my file LL1 i represent a LL(1) parsing for my grammar, here i reflect in whitch cases my not terminals elements goes to a terminal element or to an other not terminal element to construct the grammar.
[LL1](https://github.com/El3Du4Rd0/grammar_esperanto/blob/main/LL1.pdf)

In the LL(1) table i use a simplified syntax, i don't use the arrows to indicate from where is constructed the grammar because it won't fit in a pdf file, and because any not terminal element in my parser is directly connected to a terminal element 
## Analysis
This kind of grammar is into the third level of the Chomsky Hierarchy Extended Level, because in this level is where the regular grammars are and them can generate regular lenguages that esperanto is one. This kind of grammar can't be in any other lower level because it is recursive and it wont fit in the criteria for a context-free grammar, that is the level two.

The time complexity of the grammar is O(n), witch n is the number fo characters in a given string, because it is a non ambiguous grammar, but in the worst cases it could be an O(n^3) because it is a free-context grammar and because it has a lot of diferent rules, first a mathematical expretion that is recursive and can lead to deeper parse trees, second a plural and a singular that can have nominative, and accusative forms, along with adjectives and verbs.

According to analyse witch other solutions can solve the problem we can also try using an automaton, because you can check each word as a letter of an alphabet of the automaton and check if the result of testign the full sentence is a correct word or not. Another posible solution is using a regular expretion, because as the automaton you can construct each posible correct case one by one, and its rules. Finally analysing all this posible solution i can conclude that using a context-free grammar is the most eficient solution of this problem, most because you can express the rules more clearly and briefly than using a regular expretion or an automaton.

## References
Aprender esperanto  |   El curso más rápido para aprender lo imprescindible. (n.d.). https://esperanto12.net/es/ 
