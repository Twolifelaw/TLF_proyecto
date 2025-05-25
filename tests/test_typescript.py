#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test exhaustivo del analizador léxico para TypeScript.
"""

import sys
import os

# Añadir la raíz del proyecto al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lexer import AnalizadorLexico
from tokens import Categoria

def test_analizador_typescript_exhaustivo():
    # Casos de prueba
    casos_prueba = [
        # Caso 1: Código TypeScript básico
        """
        interface Usuario {
            id: number;
            nombre: string;
            email?: string;
            estado: "activo" | "inactivo";
        }
        """,
        # Caso 2: Código TypeScript con errores léxicos
        """
        interface Usuario {
            id: number;
            nombre: string;
            email?: string;
            estado: "activo" | "inactivo";
            error: @; // Error: carácter no reconocido
        }
        """,
        # Caso 3: Código TypeScript con genéricos y decoradores
        """
        @Injectable()
        class Servicio<T extends Usuario> {
            private usuarios: T[] = [];
            async getUsuario(id: number): Promise<T> {
                return this.usuarios.find(u => u.id === id)!;
            }
        }
        """,
        # Caso 4: Código TypeScript con tipos unión e intersección
        """
        type UsuarioAdmin = Usuario & {
            permisos: string[];
        };
        function procesarDato(dato: string | number): void {
            if (typeof dato === 'string') {
                console.log(dato.toUpperCase());
            } else {
                console.log(dato.toFixed(2));
            }
        }
        """,
        # Caso 5: Código TypeScript con comentarios y cadenas
        """
        // Comentario de línea
        /* Comentario de bloque */
        const mensaje = "Hola, mundo!";
        const otroMensaje = 'Hola, TypeScript!';
        const template = `Hola, ${mensaje}!`;
        """
    ]

    analizador = AnalizadorLexico()

    for i, codigo in enumerate(casos_prueba, 1):
        print(f"\n=== CASO DE PRUEBA {i} ===")
        tokens, errores = analizador.analizar(codigo)

        print("\n=== TOKENS ENCONTRADOS ===")
        for token in tokens:
            print(f"Token: {token.lexema:<20} Categoría: {token.categoria}")

        print("\n=== ERRORES ENCONTRADOS ===")
        for error in errores:
            print(f"Error: {error.lexema} en línea {error.fila}, columna {error.columna}")

        # Resumen de categorías relevantes
        tipos = [t for t in tokens if t.categoria == Categoria.TIPO]
        genericos = [t for t in tokens if t.categoria == Categoria.GENERICO]
        decoradores = [t for t in tokens if t.categoria == Categoria.DECORADOR]
        cadenas = [t for t in tokens if t.categoria == Categoria.CADENA]
        operadores_union = [t for t in tokens if t.lexema == '|']
        operadores_interseccion = [t for t in tokens if t.lexema == '&']
        asyncs = [t for t in tokens if t.lexema == 'async']
        privates = [t for t in tokens if t.lexema == 'private']
        arrobas = [t for t in tokens if t.lexema == '@']

        print("\n=== RESUMEN ===")
        print(f"Tipos encontrados: {len(tipos)}")
        print(f"Genéricos encontrados: {len(genericos)}")
        print(f"Decoradores encontrados: {len(decoradores)}")
        print(f"Cadenas encontradas: {len(cadenas)}")
        print(f"Operadores unión (|): {len(operadores_union)}")
        print(f"Operadores intersección (&): {len(operadores_interseccion)}")
        print(f"Palabras 'async': {len(asyncs)}")
        print(f"Palabras 'private': {len(privates)}")
        print(f"Símbolos '@': {len(arrobas)}")

if __name__ == "__main__":
    test_analizador_typescript_exhaustivo() 