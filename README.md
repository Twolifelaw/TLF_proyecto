# Analizador Léxico para JavaScript

Este proyecto implementa un analizador léxico para el lenguaje JavaScript utilizando Autómatas Finitos Deterministas (AFD).

## Estructura del Proyecto

```
analizador_lexico/
├── main.py                     # Punto de entrada (GUI)
├── gui/
│   └── interfaz.py             # Ventana con texto, botón y tabla de resultados
├── analizadores/
│   ├── identificador.py        # AFD Identificador
│   ├── numero_natural.py       # AFD para números naturales
│   ├── numero_real.py          # AFD para reales (pendiente)
│   ├── palabra_reservada.py    # Comparación directa con lista (pendiente)
│   ├── cadena.py               # AFD para strings con escape (pendiente)
│   ├── comentario_linea.py     # AFD comentario línea (pendiente)
│   └── comentario_bloque.py    # AFD comentario bloque (pendiente)
├── lexer.py                    # Orquesta todos los AFDs y gestiona el análisis
├── tokens.py                   # Definición de categorías y clase Token
└── utils.py                    # Funciones auxiliares (pendiente)
```

## Requisitos

- Python 3.6 o superior
- Tkinter (incluido en la mayoría de instalaciones de Python)

En sistemas basados en Debian/Ubuntu, si Tkinter no está instalado:

```bash
sudo apt-get install python3-tk
```

## Ejecución

Para ejecutar el analizador léxico:

```bash
python3 main.py
```

## Analizadores Implementados

Hasta el momento, se han implementado los siguientes analizadores:

- **Identificador**: Reconoce identificadores válidos en JavaScript (letras, números, `_` y `$`), con un máximo de 10 caracteres.
- **Número Natural**: Reconoce números naturales (enteros positivos).

## Interfaz Gráfica

La interfaz incluye:

1. Un editor de texto para ingresar código JavaScript
2. Un botón para analizar el código
3. Una tabla que muestra los tokens reconocidos (lexema, categoría, fila, columna)

## Implementación

Cada analizador está implementado como un Autómata Finito Determinista (AFD), con un método `analizar` que recibe un texto y una posición inicial, y devuelve si el token es válido, el lexema reconocido y la cantidad de caracteres consumidos.

El analizador léxico principal (`lexer.py`) orquesta todos los AFDs, aplicando el principio de máxima coincidencia: cuando varios analizadores reconocen un token, se elige el que consume más caracteres.

## Contribuciones

Para contribuir a este proyecto, sigue estos pasos:

1. Implementa uno de los analizadores pendientes en la carpeta `analizadores/`
2. Asegúrate de que devuelva una tupla `(es_valido, lexema, caracteres_consumidos)`
3. Añade pruebas unitarias al final del archivo
4. Actualiza `lexer.py` para incluir tu nuevo analizador

## Licencia

Este proyecto está bajo la licencia MIT. 