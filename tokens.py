#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Definición de categorías de tokens y clase Token para el análisis léxico de TypeScript.
"""

# Categorías de tokens en TypeScript
class Categoria:
    IDENTIFICADOR = "IDENTIFICADOR"
    NUMERO_NATURAL = "NUMERO_NATURAL"
    NUMERO_REAL = "NUMERO_REAL"
    CADENA = "CADENA"
    PALABRA_RESERVADA = "PALABRA_RESERVADA"
    COMENTARIO_LINEA = "COMENTARIO_LINEA"
    COMENTARIO_BLOQUE = "COMENTARIO_BLOQUE"
    
    # Nuevas categorías para TypeScript
    TIPO = "TIPO"  # Para tipos como number, string, boolean, etc.
    DECORADOR = "DECORADOR"  # Para @decorators
    GENERICO = "GENERICO"  # Para <T>, <K,V>, etc.
    MODIFICADOR_ACCESO = "MODIFICADOR_ACCESO"  # Para public, private, protected
    
    # Operadores
    OPERADOR_ARITMETICO = "OPERADOR_ARITMETICO"
    OPERADOR_COMPARACION = "OPERADOR_COMPARACION"
    OPERADOR_LOGICO = "OPERADOR_LOGICO"
    OPERADOR_ASIGNACION = "OPERADOR_ASIGNACION"
    OPERADOR_INCREMENTO = "OPERADOR_INCREMENTO"
    OPERADOR_DECREMENTO = "OPERADOR_DECREMENTO"
    OPERADOR_ACCESO = "OPERADOR_ACCESO"  # Para el punto (.)
    SIGNO_INTERROGACION = "SIGNO_INTERROGACION" # Para el ? (operador ternario)
    OPERADOR_OPTIONAL_CHAINING = "OPERADOR_OPTIONAL_CHAINING" # Para ?. 
    OPERADOR_NULISH_COALESCING = "OPERADOR_NULISH_COALESCING" # Para ??
    
    # Delimitadores
    PARENTESIS_APERTURA = "PARENTESIS_APERTURA"
    PARENTESIS_CIERRE = "PARENTESIS_CIERRE"
    LLAVE_APERTURA = "LLAVE_APERTURA"
    LLAVE_CIERRE = "LLAVE_CIERRE"
    CORCHETE_APERTURA = "CORCHETE_APERTURA"
    CORCHETE_CIERRE = "CORCHETE_CIERRE"
    DOS_PUNTOS = "DOS_PUNTOS"
    ANGULAR_APERTURA = "ANGULAR_APERTURA"  # Para tipos genéricos <
    ANGULAR_CIERRE = "ANGULAR_CIERRE"      # Para tipos genéricos >
    
    # Otros
    TERMINAL = "TERMINAL"           # Punto y coma (;)
    SEPARADOR = "SEPARADOR"         # Coma (,)
    
    # Errores
    ERROR = "ERROR"

class Token:
    def __init__(self, lexema, categoria, fila, columna):
        """
        Inicializa un nuevo token.
        
        Args:
            lexema: El texto del token
            categoria: La categoría del token (usar constantes de la clase Categoria)
            fila: Número de fila donde comienza el token (1-indexado)
            columna: Número de columna donde comienza el token (1-indexado)
        """
        self.lexema = lexema
        self.categoria = categoria
        self.fila = fila
        self.columna = columna
    
    def __str__(self):
        """Representación en string del token."""
        return f"Token({self.lexema}, {self.categoria}, {self.fila}, {self.columna})"
    
    def __repr__(self):
        """Representación en string del token para depuración."""
        return self.__str__()

# Palabras reservadas de TypeScript
PALABRAS_RESERVADAS = [
    # Declaraciones básicas (heredadas de JavaScript)
    "var", "let", "const", "function", "class",
    
    # Control de flujo (heredadas de JavaScript)
    "if", "else", "switch", "case", "default", "break", 
    "continue", "return", "while", "for", "do",
    
    # Operadores/Palabras clave (heredadas de JavaScript)
    "new", "this", "super", "delete", "typeof", "instanceof",
    "void", "yield", "await", "in", "of",
    
    # Valores literales (heredadas de JavaScript)
    "true", "false", "null", "undefined", 
    
    # Manejo de excepciones (heredadas de JavaScript)
    "try", "catch", "finally", "throw",
    
    # Nuevas palabras reservadas específicas de TypeScript
    "interface", "type", "enum", "namespace",
    "public", "private", "protected", "readonly",
    "abstract", "implements", "extends",
    "any", "void", "never", "unknown",
    "as", "is", "keyof", "typeof",
    "declare", "module", "export", "import",
    "readonly", "static", "async", "await"
]

# Tipos predefinidos de TypeScript
TIPOS_PREDEFINIDOS = [
    "number", "string", "boolean", "any", "void",
    "never", "unknown", "object", "symbol", "bigint",
    "undefined", "null"
] 