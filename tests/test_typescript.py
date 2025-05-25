#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test exhaustivo del analizador léxico con código TypeScript avanzado.
"""

import sys
import os

# Añadir la raíz del proyecto al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lexer import AnalizadorLexico
from tokens import Categoria

def test_analizador_typescript_completo():
    codigo_prueba = """
// Decorador de log
function Log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const originalMethod = descriptor.value;
    descriptor.value = function (...args: any[]) {
        console.log(`Llamando a ${propertyKey} con`, args);
        return originalMethod.apply(this, args);
    };
    return descriptor;
}

type Estado = "activo" | "inactivo" | "pendiente";

interface Usuario {
    id: number;
    nombre: string;
    email?: string;
    estado: Estado;
}

class Servicio<T extends Usuario> {
    private usuarios: T[] = [];

    @Log
    async agregarUsuario(usuario: T): Promise<boolean> {
        if (this.usuarios.find(u => u.id === usuario.id)) {
            throw new Error("Usuario ya existe");
        }
        this.usuarios.push(usuario);
        return true;
    }

    @Log
    async buscarUsuarios(filtro: Partial<T> & { estado?: Estado } = {}): Promise<T[]> {
        return this.usuarios.filter(u => {
            for (const key in filtro) {
                if (filtro[key as keyof T] !== undefined && u[key as keyof T] !== filtro[key as keyof T]) {
                    return false;
                }
            }
            return true;
        });
    }
}

// Uso de la clase
const servicio = new Servicio<Usuario>();
servicio.agregarUsuario({ id: 1, nombre: "Ana", estado: "activo" });
servicio.buscarUsuarios({ estado: "activo" }).then(console.log);
"""

    analizador = AnalizadorLexico()
    tokens, errores = analizador.analizar(codigo_prueba)

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
    test_analizador_typescript_completo() 