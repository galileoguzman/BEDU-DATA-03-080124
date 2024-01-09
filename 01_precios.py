
IVA = 1.16

precios_sin_iva = [415, 90, 355, 385, 115, 100, 250, 660]

#Agregar el 16% del valor mediante iteración
for i in precios_sin_iva:
    print(f'Precio sin iva {i} - Precio con iva {i*IVA}')
#Mostrar precio original y precio con iva
