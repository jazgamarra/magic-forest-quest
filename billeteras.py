
class Billetera:
    '''Representa una billetera estandar, que puede enviar y recibir dinero'''

    def __init__(self):
        self.cantidad_dinero = 0

    def pagar(self, monto):
        '''Permite realizar pagos.'''
        if self.cantidad_dinero >= monto:
            self.cantidad_dinero -= monto
            return True
        else:
            return False

    def recibir_dinero(self, cantidad):
        '''Permite recibir dinero. '''
        self.cantidad_dinero += cantidad 
        return True
        
class BilleteraHorus(Billetera):
    '''Es un tipo de billetera especial, que solo puede recibir dinero'''
    def __init__(self):
        super().__init__()
        self.cantidad_dinero = 0

    def pagar(self, cantidad):
        print('Este metodo no esta disponible para esta billetera') 
        return False 

class BilleteraFenix(Billetera):
    '''Es un tipo de billetera especial, que solo puede enviar dinero.'''
    def __init__(self):
        super().__init__()
        self.cantidad_dinero = 100

    def recibir_dinero(self, cantidad):
        print('Este metodo no esta disponible para esta billetera') 
        return False        
