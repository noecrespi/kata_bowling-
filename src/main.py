from BowlingMachine import BowlingMachine


def main():
    '''
        Crea un programa que, dada una secuencia de tiradas de bolos, devuelva el total de puntos del juego. Estas son las reglas del juego:

        - Cada jugada, o line, incluye 10 turnos, o "frames", para el jugador.

        - En cada "frame", el jugador tiene dos intentos para tirar todos los bolos.

        - Si en dos intentos el jugador no tira todos los bolos, su puntuación será el total de bolos que haya tirado en los dos intentos.

        - Si en dos intentos el jugador tira todos los bolos, esto se llama "spare" y su puntuación es de 10 + el número de bolos que tire en la siguiente tirada (en el siguiente turno).

        - Si en el primer intento el jugador tira todos los bolos, esto se llama "strike". Su turno termina y su puntuación es de 10 + el total de bolos que tire en las siguientes dos rondas.

        - Si el jugador obtiene un "spare" o un "strike" en el último "frame", tira una o dos veces más en el mismo turno respectivamente. Si con la tirada bonus tira todos los bolos, el proceso no se repite.

        - La puntuación final del juego es el total de la suma de puntuaciones de todos los "frames".
    '''


    # Ejemplo de cálculo de los puntos totales obtenidos en una partida:
    print('Demo del programa que calcula los puntos totales de una partida de bolos.')

    anotaciones = '12345123451234512345'
    print('Anotaciones de la partida: {}'.format(anotaciones))

    maquina_bolos = BowlingMachine()
    
    print('Puntos totales: {}'.format(
        maquina_bolos.calculaPuntosTotales(anotaciones))
    )




if __name__ == '__main__':
    main()
