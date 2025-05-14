class IdentificadorAFD:
    """
    Autómata Finito Determinista para reconocer identificadores en JavaScript.
    
    Los identificadores en JavaScript deben:
    - Comenzar con una letra, guion bajo (_) o signo de dólar ($)
    - Luego pueden contener letras, números, guiones bajos o signos de dólar
    - Se limitan a un máximo de 10 caracteres
    """
    def __init__(self, max_length=10):
        """
        Inicializa el autómata con la longitud máxima para identificadores.
        
        Args:
            max_length: Longitud máxima permitida para los identificadores (por defecto 10)
        """
        self.max_length = max_length

    def analizar(self, texto, pos_inicial):
        """
        Analiza el texto a partir de la posición inicial para identificar un identificador válido.
        
        Args:
            texto: Cadena de texto a analizar
            pos_inicial: Posición desde donde comenzar el análisis
            
        Returns:
            Tupla de (es_valido, lexema, caracteres_consumidos):
            - es_valido: Booleano que indica si se encontró un identificador válido
            - lexema: El identificador encontrado (vacío si no se encontró)
            - caracteres_consumidos: Número de caracteres procesados
        """
        # Estados del autómata:
        # 0: Estado inicial
        # 1: Estado de aceptación (después de primer carácter válido)
        estado = 0
        lexema = ''  # Almacena el identificador que se va construyendo
        pos = pos_inicial  # Posición actual en el texto
        longitud = 0  # Contador de caracteres del identificador
        
        # Procesar mientras queden caracteres y no se exceda la longitud máxima
        while pos < len(texto) and longitud < self.max_length:
            c = texto[pos]  # Obtener carácter actual
            
            if estado == 0:  # Estado inicial: debe ser letra, _ o $
                if c.isalpha() or c == '_' or c == '$':
                    estado = 1  # Transición al estado de aceptación
                    lexema += c
                    pos += 1
                    longitud += 1
                else:
                    break  # No es un identificador válido
            
            elif estado == 1:  # Ya tenemos al menos un carácter válido
                if c.isalnum() or c == '_' or c == '$':  # Letras, números, _ o $
                    lexema += c
                    pos += 1
                    longitud += 1
                else:
                    break  # Fin del identificador
        
        # Verificar si el identificador es válido (debe tener al menos un carácter y comenzar correctamente)
        if len(lexema) > 0 and (lexema[0].isalpha() or lexema[0] == '_' or lexema[0] == '$'):
            return True, lexema, pos - pos_inicial
        else:
            return False, '', 0

if __name__ == "__main__":
    # Código de prueba que se ejecuta solo si se ejecuta este archivo directamente
    afd = IdentificadorAFD()
    pruebas = [
        "variable1",        # Identificador válido
        "_var",             # Identificador válido (comienza con guion bajo)
        "$dolar",           # Identificador válido (comienza con signo de dólar)
        "1noValido",        # No válido (comienza con número)
        "varConMuchosCaracteres",  # Válido pero truncado a 10 caracteres
        "abc123",           # Identificador válido
        "if",               # Válido como identificador (pero es palabra reservada)
        "var#",             # Solo "var" es reconocido (el # no es válido)
        ""                  # Cadena vacía (no válida)
    ]

    for prueba in pruebas:
        valido, lexema, consumidos = afd.analizar(prueba, 0)
        print(f"Entrada: '{prueba}' -> Válido: {valido}, Lexema: '{lexema}', Caracteres consumidos: {consumidos}")
