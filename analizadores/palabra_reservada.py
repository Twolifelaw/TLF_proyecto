import sys
import os

# Añadir la raíz del proyecto al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tokens import PALABRAS_RESERVADAS

class PalabraReservadaAFD:
    def __init__(self):
        self.palabras_reservadas = PALABRAS_RESERVADAS
        
    def analizar(self, texto, pos_inicial):
        """
        Verifica si a partir de la posición inicial hay una palabra reservada.
        
        Args:
            texto: Cadena de texto a analizar
            pos_inicial: Posición desde donde comenzar el análisis
            
        Returns:
            Tupla de (es_valido, lexema, caracteres_consumidos)
        """
        # Buscar el fin de la palabra (espacio, operador, etc.)
        pos = pos_inicial
        lexema = ''
        
        while pos < len(texto) and (texto[pos].isalnum() or texto[pos] == '_' or texto[pos] == '$'):
            lexema += texto[pos]
            pos += 1
        
        # Verificar si es una palabra reservada
        if lexema in self.palabras_reservadas:
            return True, lexema, len(lexema)
        else:
            return False, '', 0

if __name__ == "__main__":
    # Pruebas
    afd = PalabraReservadaAFD()
    
    pruebas = [
        "if",
        "for",
        "while",
        "variable",
        "function",
        "class",
        "123",
        ""
    ]
    
    for prueba in pruebas:
        valido, lexema, consumidos = afd.analizar(prueba, 0)
        print(f"Entrada: '{prueba}' -> Válido: {valido}, Lexema: '{lexema}', Caracteres consumidos: {consumidos}") 