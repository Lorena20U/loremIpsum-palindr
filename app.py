import csv
import numpy as np

def histogra(n):
    result = ""
    for i in range(0, n):
            result += "*"
    return result

def rep(m, t):
    cont = 0
    for n in t:
        if n != '\n':
            if n != ' ':
                if m == n:
                    cont += 1
    return cont


def histograma(texto):
    top10 = np.array([['', 0],['', 0],['', 0],['', 0],['', 0],['', 0],['', 0],['', 0],
                    ['', 0],['', 0],['', 0],['', 0],['', 0],['', 0],['', 0],['', 0],
                    ['', 0],['', 0],['', 0],['', 0],['', 0],['', 0],['', 0],['', 0],['', 0],['', 0]])
    letras = "ABCDEFJHIJKLMNOPQRSTUVWXYZ"
    contador = 0
    i = 0
    txt = ""
    grande = 0
    for z in letras:
        contador = rep(z, texto)
        top10[i,0] = z.upper()
        top10[i,1] = contador
        txt += f"{top10[i,0]} {top10[i,1]} {histogra(contador)}\n"
        i = i + 1
    return txt

def palindromo():
    data = open("data.csv")
    lista = []
    respuesta = ""
    reader = csv.reader(data, delimiter = ',')
    for i in reader:
        lista[len(lista):] = i
    for j in lista:
        largo = 0
        palabra1 = ""
        palabra2 = ""
        for a in j:
            if a != ' ':
                largo += 1
                palabra1 += a
                palabra2 = a + palabra2
        if palabra1 == palabra2:
            respuesta += f"La palabra {palabra1} es un palindromo.\n"
        else:
            respuesta += f"La palabra {palabra1} no es un palindromo :( \n"
    return respuesta

#lorem ipsum
f = open("texto.txt", "r")
for linea in f:
    if linea != '\n':
        linea = linea.upper()
        print(histograma(linea.rstrip('\n')))
f.close()

#palindromo
print(palindromo())