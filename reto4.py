from functools import reduce
rutinaContable=[ 
 [6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)],
 [6590, ("5236", 8, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)],
 [6591, ("7812", 2, 11.99), ("9652",11,18.99)]
]

def ordenes(rutinaContable):
    print('----------------- Inicio Registro diario --------------------------')
    
    for i in range(len(rutinaContable)):
        lista_x_codigo=rutinaContable[i]
        codigo_ref=lista_x_codigo[0]
        lista_x_codigo.pop(0)
        lista_precios=list(map(lambda x: x[2]*x[1], lista_x_codigo))
        total_pesos=reduce(lambda x,y: x+y, lista_precios)
        if (total_pesos<600000):
            total_pesos+=25000
        print(f'La factura {codigo_ref} tiene un total en pesos de {total_pesos:.2f}')
    print('----------------- Fin Registro diario -----------------------------')

ordenes(rutinaContable)