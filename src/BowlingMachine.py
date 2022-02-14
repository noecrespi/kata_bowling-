class BowlingMachine:

    # CONSTRUCTOR
    def __init__(self):
        pass


    # METODOS ESTÁTICOS
    '''
    Dados los bolos derribados durante la partida (str), calcula el total de puntos (int)
    '''
    @staticmethod
    def calculaPuntosTotales(anotaciones: str) -> int:

        print('Calculando puntuación...')
        
        # validar anotaciones (str con la secuencia de bolos derribados en todas las tiradas)
        
        # recorrer las anotaciones e ir sumando los puntos
        # 

        pass


    @staticmethod
    def valida_anotaciones(anotaciones: str) -> bool:
        # 1: tiene que haber mínimo 12 tiradas
        # 2: tiene que haber máximo 20 tiradas
        if len(anotaciones) < 12 or len(anotaciones) > 20:
            return False

        # 3: sólo contiene dígitos del 1 al 9, y los caracteres '-', '/', y 'X'
        return True
