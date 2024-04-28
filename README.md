# grammar_esperanto
## Description
in this evidence i have to create a grammar that represents the lenguage Esperanto, make a model of that grammar, do the implementation, test it and realize the complexity analysis

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
To do the implementation of my grammar and to be sure that what i do is correct i use the library of python "nltk" to create a tree of how is constructed each sentence. I also put a .txt file with a lot of sentences of esperanto.
## Test

## Analysis
