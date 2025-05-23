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
    
jugador = input("Elige piedra, papel o tijera: \n").lower()
computadora = obtener_eleccion_computadora()

print(f"Tú elegiste: {jugador}")
print(f"La computadora eligió: {computadora}")

resultado = determinar_ganador(jugador, computadora)
print(f"Resultado: {resultado}")
