

lista_dic=[]
def AutoPartes(ventas: list):
    claves=['IdProducto', 'dProducto', 'pnProducto', 'cvProducto', 'sProducto', 'nComprador', 'cComprador', 'fVenta']  
    
    for i in range(len(ventas)):
        venta=list(ventas[i])
        dic={claves:venta for (claves,venta) in zip(claves,venta)}
        lista_dic.append(dic)  
    return lista_dic

ventas=lista_dic

    
def consultaRegistro(ventas, idProducto):
    lista_id=[]
    for i in range(len(ventas)):
        
        if idProducto==ventas[i]['IdProducto']:
            Producto=ventas[i]['IdProducto']
            Descripcion=ventas[i]['dProducto']
            Parte=ventas[i]['pnProducto']
            cv=ventas[i]['cvProducto']
            stock=ventas[i]['sProducto']
            comprador=ventas[i]['nComprador']
            doc=ventas[i]['cComprador']
            fecha=ventas[i]['fVenta']
            print(f'Producto consultado : {Producto} Descripción {Descripcion} #Parte {Parte} Cantidad vendida {cv} Stock {stock} Comprador {comprador} Documento {doc} Fecha Venta {fecha}')
        lista_id.append(ventas[i]['IdProducto'])
    
    if idProducto not in lista_id:
        print('No hay registro de venta de ese producto')

consultaRegistro(AutoPartes([
 (5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
 (3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
 (3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
 (8795,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')]), 2001)
print()