from abc import ABCMeta, abstractmethod
import random 

from texto import *
from billeteras import * 

class Personaje (metaclass=ABCMeta):
    ''' Representa a todos los personajes del juego, agrupando las caracteristicas comunes minimas para interactuar entre ellos. '''

    def __init__(self, nombre, raza, caracter, objetivo, motivacion, mensaje):
        self.nombre = nombre
        self.descripcion = {
            'raza': raza, 
            'caracter': caracter, 
            'objetivo': objetivo, 
            'motivacion': motivacion, 
            'mensaje': mensaje
        }
        # self.billetera = Billetera()

    def presentarse (self):
        print(f"Hola, mi nombre es {self.nombre}. Mi objetivo principal es {self.descripcion['objetivo']}. Mi motivación es {self.descripcion['motivacion']}. Me considero un {self.descripcion['raza']} {self.descripcion['caracter']} ¡{self.descripcion['mensaje']}!")
    
class Jugador (Personaje): 
    '''Representa al jugador principal del juego, un explorador cuyo objetivo es encontrar el arbol magico'''\
    
    def __init__(self, nombre, raza, caracter, objetivo, motivacion, mensaje):
        super().__init__(nombre, raza, caracter, objetivo, motivacion, mensaje)
        puntaje = 0

    def resolver_acertijo(self):
        '''El jugador elige una de las opciones para resolver el acertijo. Se valida si la respuesta es valida, si no, se envia una respuesta generica incorrecta. '''
        print('Ingrese una opcion: ') 
        respuesta = input('>>> ').lower()

        if respuesta in ['a', 'b', 'c']: 
            return respuesta 
        else: 
            return 'x'
    
    def responder_pregunta(self): 
        '''El jugador responde a las preguntas de los curiosos Protectores del Bosque'''
        print('Ingrese una respuesta: ') 
        input('>>> ')
        
class Anciano (Personaje): 
    '''Representa a un agradable anciano, quien convoca al jugador  a la mision y lo aconseja durante todo su viaje. '''

    def __init__(self, nombre, raza, caracter, objetivo, motivacion, mensaje):
        super().__init__(nombre, raza, caracter, objetivo, motivacion, mensaje)
        self.billetera = BilleteraHorus()

    def convocar_al_jugador(self): 
        print ('¡Joven aventurero! Necesito de tus habilidades para encontrar el árbol mágico, una reliquia sagrada que ha perdido su poder y que es vital para el equilibrio de nuestro bosque. Tu valentía será esencial para encontrarlo y restaurar su magia. ¡Gracias por acudir a mi llamado!')

    def dar_consejo(self):
        '''Imprime en pantalla un consejo aleatorio para el jugador'''
        print("Antes de que te retires... recuerda siempre: "+random.choice(consejos_anciano))

    def dar_pista(self, acertijo): 
        '''Da al usuario una pista sobre el acertijo a resolver, a cambio de 3 billetes magicos '''
        pass 

class Sabio (Personaje, metaclass=ABCMeta): 
    '''Los sabios del bosque buscan desafiar al jugador con acertijos. '''
    def __init__(self, nombre, raza, caracter, objetivo, motivacion, mensaje):
        super().__init__(nombre, raza, caracter, objetivo, motivacion, mensaje)
        self.billetera = BilleteraHorus()

    @abstractmethod
    def dar_acertijo (self, acertijo):
        pass 

    @abstractmethod
    def ofrecer_coima(self): 
        pass

class SabioMentor(Sabio):
    '''El Sabio Mentor desafia al jugador con acertijos para comprobar si este merece su ayuda y confianza para llegar al arbol magico'''
    def dar_acertijo(self, acertijo):
        pass

    def ofrecer_coima(self):
        pass

class SabioRival(Sabio):
    '''El Sabio Rival desafia al jugador con acertijos, buscando desanimarlo en su mision. '''
    def dar_acertijo(self, acertijo):
        '''Desafia al jugador con un acertijo'''
        pass

    def ofrecer_coima(self):
        '''Ofrece al jugador una coima para dejar pasar la pregunta, pero si acepta, lo hostiga y molesta hasta que se vaya. '''
        pass

class Protector (Personaje):
    '''Los protectores del bosque son seres que cuidan el bosque. Estan muy interesados en la raza humana y en su comportamiento.'''
    def __init__(self, nombre, raza, caracter, objetivo, motivacion, mensaje):
        super().__init__(nombre, raza, caracter, objetivo, motivacion, mensaje)
        self.billetera = BilleteraFenix()

    def hacer_pregunta(self): 
        '''Los protectores del bosque hacen preguntas al jugador y le regalan billetes. '''
        pass

