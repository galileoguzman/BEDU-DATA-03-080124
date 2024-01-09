# Constante IVA
IVA = 1.16

def aplicar_iva(number):
    resultado = number * IVA
    return resultado

precios_sin_iva = [415, 90, 355, 385, 115, 100, 250, 660]

# precios_con_iva = []
# for precio in precios_sin_iva:
#     # print(precio)
#     # print(aplicar_iva(precio))
#     precio_individual_con_iva = aplicar_iva(precio)
#     precios_con_iva.append(precio_individual_con_iva)
# print(precios_con_iva)


# Modulo map
precios_con_iva = list(map(aplicar_iva, precios_sin_iva))
print(precios_con_iva)