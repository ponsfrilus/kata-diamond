lettre = input("Entrez une lettre : ")

lettres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

if lettre.isupper():
    lettres = [lettre.upper() for lettre in lettres]
indexInput = lettres.index(lettre)
for i in range(indexInput):
    espaces = " " * (indexInput-i)
    spacesBetween = " " * (2 * i - 1)
    if i != 0:
        print(espaces + lettres[i] + spacesBetween + lettres[i])
    else:
        print(espaces + lettres[i])


for j in range(indexInput, -1, -1):
    espaces = " " * (indexInput-j)
    spacesBetween = " " * (2 * j - 1)
    if j != 0:
        print(espaces + lettres[j] + spacesBetween + lettres[j])
    else:
        print(espaces + lettres[j])