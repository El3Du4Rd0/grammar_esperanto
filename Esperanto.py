import nltk
from nltk import CFG

# Download required NLTK data
nltk.download('punkt')

# Define the context-free grammar (CFG) for Esperanto
grammar = CFG.fromstring("""
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
""")

# Create a chart parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Define the input sentence
sentence = "unu minus unu minus unu minus unu"

# Tokenize the input sentence
tokens = nltk.word_tokenize(sentence)

# Parse and pretty print the parse trees
for tree in parser.parse(tokens):
    tree.pretty_print()
