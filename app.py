from inicializaciones.crear_personajes import *
from mecanicas_juego import *
from inicializaciones.texto import acertijos 

import time 
import os


print('++++++++++++++++++++++++++++++++++++++++++++++++++')
print('          Bienvenido a Magic Forest Quest!')
print('++++++++++++++++++++++++++++++++++++++++++++++++++')
nombre_usuario = input('Cual es tu nombre? ')
player.nombre = nombre_usuario

# --------------------------------------------------------------------------------------
# INICIAR EL JUEGO 
# --------------------------------------------------------------------------------------

print('\n\n       ***  INICIA EL JUEGO *** ')
time.sleep(1)
os.system('clear')


# El jugador se encuentra con el anciano, quien le presenta su mision. 
print('>> Anciano del Bosque: ')
anciano.convocar_al_jugador()
time.sleep(3)

print(f'\n>> {player.nombre}: \nMuchas gracias por convocarme! Pero tu quien eres? ')

print('\n>> Anciano')
anciano.presentarse()
time.sleep(5)
os.system('clear')


# El jugador inicia su aventura, encontrandose con un protector del bosque. Este le hace una pregunta y recibe su dinero.
print('\n\n<< Inicia la aventura. A los pocos pasos de despedirse del anciano, el jugador se encuentra con una tranquila criatura. Por amabilidad, decide presentarse. >> ') 

print('\n>> Jugador')
player.presentarse() 
time.sleep(4)


print(f'\n>> {protector1.nombre} (Protector del Bosque)')
protector1.presentarse()
time.sleep(4)


print(f'\n>> {protector1.nombre} (Protector del Bosque)')
protector1.hacer_pregunta()
player.responder_pregunta()
protector1.ofrecer_dinero(player)
time.sleep(5)
os.system('clear')


# El jugador se encuentra con uno de los sabios. 
print(f'\n>> {sabio_mentor.nombre} (Sabio)')
sabio_mentor.presentarse()
print('Estas listo para un desafio??')
time.sleep(3)

while True: 
    acertijo = random.choice(acertijos)

    print(f'\n>> {sabio_mentor.nombre} (Sabio)')
    respuesta_acertijo = sabio_mentor.dar_acertijo(acertijo, player)
    time.sleep(3)

    if respuesta_acertijo: 
        print('La respuesta es correcta!')
        break
    else: 
        print('La respuesta no es correcta. ')

        print('\n>> Anciano')
        print('Veo que no conoces la respuesta. Desea una pista?')
        aceptar = anciano.dar_pista(acertijo, player) 
        
        if aceptar: 
            print(acertijo['opciones'])
            respuesta_jugador = player.resolver_acertijo()

            if verificar_respuesta(respuesta_jugador, acertijo): 
                print('La respuesta es correcta!')
                break 
            else: 
                print('Lo siento, fallaste de nuevo. Tendras que resolver otro acertijo.')
            
        else: 
            print(f'\n>> {sabio_mentor.nombre} (Sabio)')
            aceptar = sabio_mentor.sobornar_jugador(player)
            if aceptar:
                break 

print('... esta aventura continuara')
time.sleep(2)