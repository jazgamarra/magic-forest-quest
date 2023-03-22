def transaccion_dinero (emisor, receptor, monto): 
    if emisor.billetera.pagar(monto): 
        receptor.billetera.recibir_dinero(monto)
        print(f'{receptor.nombre} ha recibido {monto} de {emisor.nombre}')
        return True 
    else:
        print(emisor.billetera.cantidad_dinero, emisor.__class__)
        print('No se ha podido realizar la transaccion')
        return False 
    

def verificar_respuesta (respuesta_jugador, acertijo): 
    return respuesta_jugador == acertijo['respuesta'] 

    