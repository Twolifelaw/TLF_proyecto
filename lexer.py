#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analizador léxico principal para JavaScript.
Orquesta todos los autómatas para analizar el código fuente.
"""

from tokens import Token, Categoria
from analizadores.identificador import IdentificadorAFD
from analizadores.numero_natural import NumeroNaturalAFD
from analizadores.palabra_reservada import PalabraReservadaAFD
from analizadores.numero_real import NumeroRealAFD
from analizadores.simbolo import SimboloAFD
from analizadores.cadena import CadenaAFD
from analizadores.comentario_linea import ComentarioLineaAFD
from analizadores.comentario_bloque import ComentarioBloqueAFD
# TODO: Importar el resto de analizadores a medida que se implementen

class AnalizadorLexico:
    def __init__(self):
        # Inicializar todos los analizadores
        self.analizadores = {
            "identificador": IdentificadorAFD(),
            "numero_natural": NumeroNaturalAFD(),
            "palabra_reservada": PalabraReservadaAFD(),
            "numero_real": NumeroRealAFD(),
            "simbolo": SimboloAFD(),
            "cadena": CadenaAFD(),
            "comentario_linea": ComentarioLineaAFD(),
            "comentario_bloque": ComentarioBloqueAFD(),
            # TODO: Añadir el resto de analizadores
        }
    
    def analizar(self, codigo_fuente):
        """
        Analiza el código fuente completo y devuelve una lista de tokens.
        
        Args:
            codigo_fuente: String con el código fuente a analizar
            
        Returns:
            Lista de objetos Token
        """
        tokens = []
        errores = []
        
        lineas = codigo_fuente.split('\n')
        for num_linea, linea in enumerate(lineas, 1):
            pos = 0
            
            while pos < len(linea):
                # Ignorar espacios en blanco
                if linea[pos].isspace():
                    pos += 1
                    continue
                
                # Analizar con cada analizador
                mejor_consumo = 0
                mejor_lexema = ""
                mejor_categoria = None
                
                # Probar comentarios de bloque (/* ... */)
                valido, lexema, consumidos = self.analizadores["comentario_bloque"].analizar(linea, pos)
                if valido and consumidos > mejor_consumo:
                    mejor_consumo = consumidos
                    mejor_lexema = lexema
                    mejor_categoria = Categoria.COMENTARIO_BLOQUE
                
                # Probar comentarios de línea (//)
                valido, lexema, consumidos = self.analizadores["comentario_linea"].analizar(linea, pos)
                if valido and consumidos > mejor_consumo:
                    mejor_consumo = consumidos
                    mejor_lexema = lexema
                    mejor_categoria = Categoria.COMENTARIO_LINEA
                
                # Probar cadenas (para reconocer texto entre comillas)
                valido, lexema, consumidos = self.analizadores["cadena"].analizar(linea, pos)
                if valido and consumidos > mejor_consumo:
                    mejor_consumo = consumidos
                    mejor_lexema = lexema
                    mejor_categoria = Categoria.CADENA
                
                # Probar símbolos (operadores, paréntesis, etc.)
                valido, lexema, consumidos = self.analizadores["simbolo"].analizar(linea, pos)
                if valido and consumidos > mejor_consumo:
                    mejor_consumo = consumidos
                    mejor_lexema = lexema
                    # Obtener la categoría específica del símbolo
                    categoria_simbolo = self.analizadores["simbolo"].obtener_categoria(lexema)
                    if categoria_simbolo:
                        mejor_categoria = categoria_simbolo
                
                # Probar palabra reservada
                valido, lexema, consumidos = self.analizadores["palabra_reservada"].analizar(linea, pos)
                if valido and consumidos > mejor_consumo:
                    mejor_consumo = consumidos
                    mejor_lexema = lexema
                    mejor_categoria = Categoria.PALABRA_RESERVADA
                
                # Probar número real (antes que natural para evitar confusión)
                valido, lexema, consumidos = self.analizadores["numero_real"].analizar(linea, pos)
                if valido and consumidos > mejor_consumo:
                    mejor_consumo = consumidos
                    mejor_lexema = lexema
                    mejor_categoria = Categoria.NUMERO_REAL
                
                # Probar número natural
                valido, lexema, consumidos = self.analizadores["numero_natural"].analizar(linea, pos)
                if valido and consumidos > mejor_consumo:
                    mejor_consumo = consumidos
                    mejor_lexema = lexema
                    mejor_categoria = Categoria.NUMERO_NATURAL
                
                # Probar identificador
                valido, lexema, consumidos = self.analizadores["identificador"].analizar(linea, pos)
                if valido and consumidos > mejor_consumo:
                    mejor_consumo = consumidos
                    mejor_lexema = lexema
                    mejor_categoria = Categoria.IDENTIFICADOR
                
                # TODO: Probar el resto de analizadores
                
                # Si se encontró un token
                if mejor_consumo > 0:
                    token = Token(mejor_lexema, mejor_categoria, num_linea, pos+1)
                    tokens.append(token)
                    pos += mejor_consumo
                else:
                    # Error: carácter no reconocido
                    error = Token(linea[pos], Categoria.ERROR, num_linea, pos+1)
                    errores.append(error)
                    pos += 1
        
        return tokens, errores

if __name__ == "__main__":
    # Prueba básica
    analizador = AnalizadorLexico()
    
    codigo_prueba = """
    // Declaración de variables
    var contador = 123;
    
    /* Definición de constantes
       en varias líneas */
    const PI = 3.14159;
    
    // Ejemplos de números reales
    let temperatura = 10.5e-3;
    let notacion = 1e10;
    let decimal = .5;
    
    // Condicional simple
    if (contador > 0) {
        // Imprimir un mensaje
        console.log("Positivo");  // Cadena de texto
    }
    """
    
    tokens, errores = analizador.analizar(codigo_prueba)
    
    print("=== TOKENS ===")
    for token in tokens:
        print(token)
        
    print("\n=== ERRORES ===")
    for error in errores:
        print(error) 