import random

def obtener_eleccion_computadora():
    opciones = ["piedra","papel","tijera"]
    return random.choice(opciones)

def determinar_ganador(jugador,computadora):
    if jugador == computadora:
        return "Empate"
    elif (jugador == "piedra" and computadora == "tijera") or \
    (jugador == "papel" and computadora == "piedra") or \
    (jugador == "tijera" and computadora == "papel"):
        return "Ganaste"
    else : 
        return "Perdiste"
    
    