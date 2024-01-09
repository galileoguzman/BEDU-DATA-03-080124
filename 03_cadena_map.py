cancion = '''
Deja decirte que te amo
Que nunca había sentido algo igual
Eres luz de un lindo amanecer
Y motivo por lo que hoy vive mi ser
Eres tú el aire al respirar
Y fortuna de saber lo que es amar
'''



# cancion_modificada = []
# for caracter in cancion:
#     temporal = caracter
#     if caracter in vocales:
#         temporal = caracter.upper()
#     cancion_modificada.append(temporal)

# print(cancion_modificada)
def resaltar_vocal(letra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    if letra in vocales:
        return letra.upper()
    return letra

cancion_modificada = list(map(resaltar_vocal, cancion))
print(cancion_modificada)