from personajes import *
from utils import *
from texto import acertijos

print('+++++++++++++++++++++++++++++++++++')
print('Bienvenido a Magic Forest Quest!')
print('+++++++++++++++++++++++++++++++++++')
nombre_usuario = input('Cual es tu nombre? ')

# --------------------------------------------------------------------------------------
# Crear personajes 
# --------------------------------------------------------------------------------------
player = Jugador(nombre_usuario, 'humano', 'valiente, entusiasta y alegre', 'encontrar el arbol magico para obtener su sabiduria', 'sacar adelante a mi puebloa  traves de la magia', 'Acompanhame en esta aventura') 

anciano = Anciano ('Alatar', 'humano', 'sabio, amable y protector', 'llevar la voz de la magia al mundo', 'creo que la magia salvara muchas vidas si se la lleva al lugar correcto',  'Bienvenido, explorador') 

sabio_mentor = SabioMentor ('Isidore', 'humano', 'intelectual, sereno y enigmático', 'evaluar a los exploradores para determinar si son dignos de mi confianza', 'proteger el arbol magico de personas peligrosas', 'Que empiece la prueba')

sabio_rival = SabioRival('Halim', 'elfo oscuro', 'egoista, inteligente y astuto.', 'evitar que cualquiera llegue al Árbol Mágico.', 'probar mi propia habilidad paras proteger el arbol', '¿Quién se atreve a desafiarme?')

protector1 = Protector('Talara', 'ninfa', 'amigable, curiosa y protectora.', 'investigar por qué los humanos están causando daño en el bosque mágico.', 'ayudar a los humanos a comprender el valor del bosque mágico y a protegerlo.', 'Saludos, aventurero') 

# protector2 = 

# --------------------------------------------------------------------------------------
# INICIAR EL JUEGO 
# --------------------------------------------------------------------------------------

print('-----------------------------------')
print('INICIA EL JUEGO: ')
print('-----------------------------------')


# El jugador se encuentra con el anciano, quien le presenta su mision. 
print('>> Anciano del Bosque: ')
anciano.convocar_al_jugador()

print(f'\n>> {player.nombre}: \nMuchas gracias por convocarme! Pero tu quien eres? ')

print('\n>> Anciano')
anciano.presentarse()


# El jugador inicia su aventura, encontrandose con un protector del bosque. Este le hace una pregunta y recibe su dinero.
print('<< Inicia la aventura. A los pocos pasos de despedirse del anciano, el jugador se encuentra con una tranquila criatura. Por amabilidad, decide presentarse. >> ') 

print('\n>> Jugador')
player.presentarse() 

print(f'\n>> {protector1.nombre} (Protector del Bosque)')
protector1.presentarse()

print(f'\n>> {protector1.nombre} (Protector del Bosque)')
protector1.hacer_pregunta()
player.responder_pregunta()
protector1.ofrecer_dinero(player)


# El jugador se encuentra con uno de los sabios. 
print(f'\n>> {sabio_mentor.nombre} (Sabio)')
sabio_mentor.presentarse()
print('Estas listo para un desafio??')

while True: 
    acertijo = random.choice(acertijos)

    print(f'\n>> {sabio_mentor.nombre} (Sabio)')
    sabio_mentor.dar_acertijo(acertijo)

    respuesta_jugador = player.resolver_acertijo()

    if verificar_respuesta(respuesta_jugador, acertijo): 
        print('La respuesta es correcta!')
        break
    else: 
        print('La respuesta no es correcta. ')

        print('\n>> Anciano')
        aceptar = player.responder_pregunta
        
        if aceptar: 
            anciano.dar_pista(acertijo, player)
            print(acertijo['opciones'])
            respuesta_jugador = player.resolver_acertijo()

            if verificar_respuesta(respuesta_jugador, acertijo): 
                break 
            else: 
                print('Lo siento, fallaste de nuevo. Tendras que resolver otro acertijo.')
            
        else: 
            print(f'\n>> {sabio_mentor.nombre} (Sabio)')
            aceptar = sabio_mentor.sobornar_jugador()
            if aceptar:
                break 
