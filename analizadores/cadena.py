class CadenaAFD:
    def __init__(self):
        pass
        
    def analizar(self, texto, pos_inicial):
        """
        Analiza si a partir de la posición inicial hay una cadena de texto.
        Una cadena comienza con " y termina con ", y puede contener secuencias de escape \.
        
        Args:
            texto: Cadena de texto a analizar
            pos_inicial: Posición desde donde comenzar el análisis
            
        Returns:
            Tupla de (es_valido, lexema, caracteres_consumidos)
        """
        # Estados del autómata:
        # 0: Inicial
        # 1: Después de la comilla de apertura
        # 2: Después de una barra invertida (escape)
        # 3: Después de la comilla de cierre (estado final)
        
        estado = 0
        lexema = ''
        pos = pos_inicial
        
        while pos < len(texto):
            c = texto[pos]
            
            if estado == 0:  # Estado inicial
                if c == '"':
                    estado = 1
                    lexema += c
                    pos += 1
                else:
                    break  # No empieza con comilla
                    
            elif estado == 1:  # Dentro de la cadena
                if c == '"':
                    estado = 3  # Comilla de cierre, terminó la cadena
                    lexema += c
                    pos += 1
                    break  # Terminar análisis
                elif c == '\\':
                    estado = 2  # Encontramos un escape
                    lexema += c
                    pos += 1
                else:
                    lexema += c  # Cualquier otro carácter es parte de la cadena
                    pos += 1
                    
            elif estado == 2:  # Después de escape
                lexema += c  # El carácter después del escape siempre se toma literal
                estado = 1  # Volver al estado dentro de la cadena
                pos += 1
        
        # Verificar si terminamos con una cadena válida
        if estado == 3:
            return True, lexema, len(lexema)
        else:
            return False, '', 0

if __name__ == "__main__":
    # Pruebas
    afd = CadenaAFD()
    
    pruebas = [
        '"Hola mundo"',
        '"Cadena con \\"escape\\""',
        '"Cadena sin cerrar',
        'No es cadena',
        '"Cadena con\\nSalto"',
        '"Cadena\\tTabulador"',
        '"Cadena\\\\Barra"',
        '',
    ]
    
    for prueba in pruebas:
        valido, lexema, consumidos = afd.analizar(prueba, 0)
        print(f"Entrada: '{prueba}' -> Válido: {valido}, Lexema: '{lexema}', Caracteres consumidos: {consumidos}") 