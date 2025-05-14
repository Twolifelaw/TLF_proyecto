import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
import os

# Añadir la raíz del proyecto al path para importaciones
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analizadores.identificador import IdentificadorAFD
from lexer import AnalizadorLexico
from tokens import Categoria

class InterfazIdentificador:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico - JavaScript")
        self.root.geometry("800x600")  # Tamaño más grande
        
        # Configuración de la interfaz
        self.configure_ui()
        
        # Inicializar analizador léxico
        self.analizador = AnalizadorLexico()
        
    def configure_ui(self):
        """Configura todos los elementos de la interfaz gráfica"""
        # Frame principal con dos columnas
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Panel izquierdo para el editor
        left_frame = ttk.LabelFrame(main_frame, text="Código JavaScript")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Editor de texto con scroll
        self.editor = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, width=40, height=25)
        self.editor.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Panel derecho para resultados
        right_frame = ttk.LabelFrame(main_frame, text="Resultados del Análisis")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Botón de análisis
        btn_frame = ttk.Frame(right_frame)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.btn_analizar = ttk.Button(btn_frame, text="Analizar Código", command=self.analizar_codigo)
        self.btn_analizar.pack(side=tk.LEFT, padx=5)
        
        self.btn_limpiar = ttk.Button(btn_frame, text="Limpiar", command=self.limpiar)
        self.btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        # Tabla de resultados
        columns = ("lexema", "categoria", "fila", "columna")
        self.tabla = ttk.Treeview(right_frame, columns=columns, show="headings")
        
        # Configurar encabezados
        self.tabla.heading("lexema", text="Lexema")
        self.tabla.heading("categoria", text="Categoría")
        self.tabla.heading("fila", text="Fila")
        self.tabla.heading("columna", text="Columna")
        
        # Configurar columnas
        self.tabla.column("lexema", width=150)
        self.tabla.column("categoria", width=100)
        self.tabla.column("fila", width=50)
        self.tabla.column("columna", width=50)
        
        # Scrollbar para la tabla
        scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        
        # Empaquetar tabla y scrollbar
        self.tabla.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
             
    def analizar_codigo(self):
        """Analiza el código completo usando el analizador léxico"""
        # Limpiar tabla
        self.limpiar_tabla()
        
        # Obtener código
        codigo = self.editor.get("1.0", tk.END)
        if not codigo.strip():
            messagebox.showinfo("Aviso", "Por favor ingresa código para analizar.")
            return
            
        # Analizar el código con el analizador léxico
        tokens, errores = self.analizador.analizar(codigo)
        
        # Mostrar tokens en la tabla
        for token in tokens:
            self.tabla.insert("", "end", values=(
                token.lexema, 
                token.categoria,
                token.fila, 
                token.columna
            ))
        
        # Mostrar errores (si hay)
        if errores:
            for error in errores:
                self.tabla.insert("", "end", values=(
                    error.lexema,
                    "ERROR: Carácter no reconocido",
                    error.fila,
                    error.columna
                ))
            
            messagebox.showwarning(
                "Errores encontrados", 
                f"Se encontraron {len(errores)} errores léxicos en el código."
            )
    
    def limpiar_tabla(self):
        """Limpia la tabla de resultados"""
        for item in self.tabla.get_children():
            self.tabla.delete(item)
            
    def limpiar(self):
        """Limpia editor y tabla"""
        self.editor.delete("1.0", tk.END)
        self.limpiar_tabla()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazIdentificador(root)
    root.mainloop()