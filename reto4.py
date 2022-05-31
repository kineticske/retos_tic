from functools import reduce
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
        print(f'La factura {codigo_ref} tiene un total en pesos de {total_pesos:,.2f}')
    print('----------------- Fin Registro diario -----------------------------')

