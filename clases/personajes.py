from abc import ABCMeta, abstractmethod
import random 
from inicializaciones.texto import consejos_anciano, preguntas_protectores
from clases.billeteras import * 
from mecanicas_juego import *

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
        self.billetera = Billetera()

    def presentarse (self):
        print(f"Hola, mi nombre es {self.nombre}. Mi objetivo principal es {self.descripcion['objetivo']}. Mi motivación es {self.descripcion['motivacion']}. Me considero un {self.descripcion['raza']} {self.descripcion['caracter']} ¡{self.descripcion['mensaje']}!")

class Jugador (Personaje): 
    '''Representa al jugador principal del juego, un explorador cuyo objetivo es encontrar el arbol magico'''
    
    def __init__(self, nombre, raza, caracter, objetivo, motivacion, mensaje):
        super().__init__(nombre, raza, caracter, objetivo, motivacion, mensaje)
        self.__puntaje = 0

    def resolver_acertijo(self):
        '''El jugador elige una de las opciones para resolver el acertijo. Se valida si la respuesta es valida, si no, se envia una respuesta generica incorrecta. '''
        respuesta_jugador = input('Ingrese una opcion: ')

        if respuesta_jugador.lower() in ['a', 'b', 'c']: 
            return respuesta_jugador 
        else: 
            return 'x'
    
    def responder_pregunta(self): 
        input('Responde: ')

    def realizar_pago(self): 
        '''El jugador decide si realizar o no el pago '''
        respuesta = input('Responda "si" o "no": ')

        return respuesta.lower() == 'si' 
    
    def sumar_puntaje(self, puntos): 
        self.__puntaje += puntos

class Anciano (Personaje): 
    '''Representa a un agradable anciano, quien convoca al jugador  a la mision y lo aconseja durante todo su viaje. '''

    def __init__(self, nombre, raza, caracter, objetivo, motivacion, mensaje):
        super().__init__(nombre, raza, caracter, objetivo, motivacion, mensaje)
        self.billetera = BilleteraHorus()
        self.__consejos = consejos_anciano 

    def convocar_al_jugador(self): 
        print ('¡Joven aventurero! Estoy muy agradecido porque has acudido a mi llamado. Escuche que estas en busqueda de algo que pueda sacar adelante a tu pueblo, y creo poder ayudarte con eso. Hace decadas, existia una leyenda que hablaba de que el arbol magico se encontraba en esta parte del bosque. Existen sabios muy celosos por esta zona. Ellos saben en donde esta el arbol, pero no te lo diran facilmente. Emprendamos juntos esta aventura! ')

    def dar_consejo(self):
        '''Imprime en pantalla un consejo aleatorio para el jugador'''
        print("Antes de que te retires... recuerda siempre: "+random.choice(self.__consejos))

    def dar_pista(self, acertijo, jugador): 
        '''Da al usuario una pista sobre el acertijo a resolver, a cambio de 3 billetes magicos '''

        jugador_acepta_pagar = jugador.realizar_pago() 

        if (jugador_acepta_pagar): 
            jugador_acepta_pagar = transaccion_dinero
            if transaccion_dinero(jugador, self, 5):
                print('La pista es la siguiente: '+acertijo['pista']) 

        return jugador_acepta_pagar 

class Sabio (Personaje, metaclass=ABCMeta): 
    '''Los sabios del bosque buscan desafiar al jugador con acertijos. '''
    def __init__(self, nombre, raza, caracter, objetivo, motivacion, mensaje):
        super().__init__(nombre, raza, caracter, objetivo, motivacion, mensaje)
        self.billetera = BilleteraHorus()

    @abstractmethod
    def dar_acertijo (self, acertijo):
        pass 

    @abstractmethod
    def sobornar_jugador(self): 
        pass

class SabioMentor(Sabio):
    '''El Sabio Mentor desafia al jugador con acertijos para comprobar si este merece su ayuda y confianza para llegar al arbol magico'''
    def dar_acertijo(self, acertijo, jugador):
        print('Joven explorador, resuelve este acertijo y ganaras un poco mas mi corazon. ')
        print(acertijo['adivinanza'])
        print(acertijo['opciones'])

        respuesta_jugador = jugador.resolver_acertijo() 

        respuesta_es_correcta = verificar_respuesta(respuesta_jugador, acertijo)
        
        if not respuesta_es_correcta: 
            jugador.sumar_puntaje(-5)
           
        return respuesta_es_correcta

    def sobornar_jugador(self, jugador):
        print ('Veo que no conoces la respuesta. Podria dejarte pasar... a cambio de que me pagues el almuerzo de hoy. Aceptas? ')

        jugador_acepta_pagar = jugador.realizar_pago() 

        if (jugador_acepta_pagar): 
            if transaccion_dinero(jugador, self, 5):
                print('Muchas gracias! Hoy almorzare un delicioso sandwich de hongos. ')
        else: 
            print('No hay problema, pero aqui va otra pregunta!')

        return jugador_acepta_pagar 

class SabioRival(Sabio):
    '''El Sabio Rival desafia al jugador con acertijos, buscando desanimarlo en su mision. '''
    def dar_acertijo(self, acertijo, jugador ):
        '''Desafia al jugador con un acertijo'''
        print('Joven, resuelve este acertijo si eres digno de la sabiduria del arbol magico. ')
        print(acertijo['adivinanza'])
        print(acertijo['opciones'][0], acertijo['opciones'][1], acertijo['opciones'][2])
        respuesta_jugador = jugador.resolver_acertijo() 

        respuesta_es_correcta = verificar_respuesta(respuesta_jugador, acertijo)

        if respuesta_es_correcta: 
            jugador.sumar_puntaje(3)
           
        return respuesta_es_correcta
    
    def sobornar_jugador(self, jugador ):
        '''Ofrece al jugador una coima para dejar pasar la pregunta, pero si acepta, lo hostiga y molesta hasta que se vaya. '''
        
        print ('Veo que no conoces la respuesta. Podria dejarte en paz... si no fueses un intruso en nuestro bosque. Podria dejarte pasar por 10 billetes. Aceptas?')
        jugador_acepta_pagar = jugador.realizar_pago() 

        if (jugador_acepta_pagar): 
            if transaccion_dinero(jugador, self, 10):
                print('¡Ja! ¡Qué ingenuo fuiste al creer que tu dinero me compraría! Aceptar tu soborno fue fácil, pero eso no significa que tengas mi respeto. Al contrario, demuestras ser un cobarde que busca solucionar sus problemas a base de dinero. ')
        else: 
            print('Aqui va otra pregunta: ')
            
        return jugador_acepta_pagar 

class Protector (Personaje):
    '''Los protectores del bosque son seres que cuidan el bosque. Estan muy interesados en la raza humana y en su comportamiento.'''
    def __init__(self, nombre, raza, caracter, objetivo, motivacion, mensaje):
        super().__init__(nombre, raza, caracter, objetivo, motivacion, mensaje)
        self.billetera = BilleteraFenix()
        self.__preguntas = preguntas_protectores 

    def hacer_pregunta(self): 
        '''Los protectores del bosque hacen preguntas al jugador'''
        print('Joven, hace mucho tiempo me vengo haciendo una pregunta. He visto y estudiado como se comportan ustedes los humanos. Podria usted responderme una pregunta y solo una?') 
        print(random.choice(self.__preguntas))

    def ofrecer_dinero(self, jugador): 
        '''A veces, cuando el jugador responde una pregunta, los Protectores deciden regalarle billetes'''

        print(f'\n>> {self.nombre} (Protector del Bosque)')
        print('Me encuentro muy satisfecho con su respuesta. Acepte, por favor, estos billetes que le ofrecere.')
        recompensa = random.randint(1, 10) 
        transaccion_dinero (self, jugador, recompensa)

    def agradecer_respuesta(self): 
        print('Muchas gracias por su respuesta. Me encuentro en desacuerdo con el actuar de los humanos. Espero que Ud. sea distinto, ya que lo estamos dejando entrar a nuestro bosque.')
