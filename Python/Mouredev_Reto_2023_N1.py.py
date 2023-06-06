
#https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%231%20-%20EL%20LENGUAJE%20HACKER%20%5BF%C3%A1cil%5D/ejercicio.md

""" Escribe un programa que reciba un texto y transforme lenguaje natural a
    "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
    se caracteriza por sustituir caracteres alfanuméricos.
    - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
    con el alfabeto y los números en "leet".
    (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")"""


Diccionario = { "A" :"@", "B" : "|-]", "C" : "<", "D" : "[)", "E" : "[-", "F" : "|=", "G" : "6", "H" : "|-|", 
"I" : "[]", "J" : "_|", "K" : "|<", "L" : "|_", "M" : "/V\ ","N" : " /\/", "O" : "oh", "P" : " []D", "Q" : "(_,)",
"R" : "I2", "S" : "$", "T" : "~|~", "U" : "|_|", "V" : "\/", "W" : "\/\/", "X" : "}{", "Y" : "'/", "Z" : "-/_",
"1" : "L", "2" : "R", "3" : "E", "4" : "A", "5" : "S", "6" : "b", "7 ": "T", "8" : "B", "9" : "g", "0" : "o" }

def Traductor (Texto):
    Texto_traducido = " "
    for i in range(len(Texto)):
        Letra = Texto.upper()[i]
        if Letra in Diccionario:
            Texto_traducido += Diccionario[Letra]
        else:
            Texto_traducido += Letra
    return Texto_traducido

Texto = input("Digita El Texto Que Deseas Convertir O Traducir: \n")
print(Traductor(Texto))