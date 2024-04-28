# grammar_esperanto
## Description
in this evidence i have to create a grammar that represents the lenguage Esperanto, make a model of that grammar, do the implementation, test it and realize the complexity analysis

Esperanto is a constructed lenguage created by Zamenhof in 1887. The word Esperanto translates into english as "the one who hopes". Esperanto was created with the idea to become the new universal lenguage, sadly that dream won't come true. 

## Model

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
## Implementation

## Test

## Analysis
