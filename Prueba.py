import  unittest

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Empate" 
    elif (jugador == "Piedra" and computadora =="tijera") or (jugador == "papel" and computadora =="piedra") or (jugador == "tijera" and computadora =="papel"):
        return "Ganaste"
    else:
        return "Perdiste"
    
class TestJuego(unittest.TestCase):
    def test_empate(self):
        self.assertEqual(determinar_ganador("piedra","piedra"),"Empate")
        self.assertEqual(determinar_ganador("papel","papel"),"Empate")
        self.assertEqual(determinar_ganador("tijera","tijera"),"Empate")

        

    def test_ganar(self):
        self.assertEqual(determinar_ganador("piedra","tijera"),"Ganar")
        self.assertEqual(determinar_ganador("papel","piedra"),"Ganar")
        self.assertEqual(determinar_ganador("tijera","papel"),"Ganar")

    def test_perder(self):
        self.assertEqual(determinar_ganador("piedra","papel"),"Perder")
        self.assertEqual(determinar_ganador("papel","tijera"),"Perder")
        self.assertEqual(determinar_ganador("tijera","piedra"),"Perder")

    if __name__ == "__main__":
        unittest.main()