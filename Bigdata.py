import re, string
from collections import Counter 

def procesar(cadena):
    print("In: "+str(cadena))
    cadena=" ".join(cadena)
    print("Join: "+str(cadena))
    cadena=cadena.lower()
    cadena=re.sub('[%s]' % re.escape(string.punctuation), ' ', cadena)
    cadena=cadena.split()
    print("Out: "+str(cadena))

def reducir(cadena):
    print("In: "+str(cadena))
    cadena=Counter(cadena)
    print("Out: "+ str(cadena)[8:-1])

print("Primer punto: \n")
a=["erase una vez una casa grande y blanca, con muchas ventanas"]
procesar(a)
print("\n")
print("Segundo punto: \n")
b=["Erase una vez una casa grande! y BLANCA, con muchas ventanas..."]
procesar(b)
print("\n")
print("Tercer punto: \n")
c=["una cosa o la otra,","la casa es grande","es un dia azul"]
procesar(c)
print("\n")
print("Cuarto punto: \n")
d=["una","casa","casa","casa","la","la","ayer"]
reducir(d)
