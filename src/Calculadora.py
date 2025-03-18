import tkinter as tk
import os
import sys
from math import isfinite


class Calculator:
    """Clase principal de la calculadora"""

    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self._setup_theme()
        self._setup_ui()
        self._bind_keyboard()

        # Variables de estado
        self.expression = ""
        self.result_shown = False
        self.dark_mode = True

    def _setup_theme(self, dark=True):
        """Configuramos los colores y estilos visuales"""
        if dark:
            self.bg_color = '#2c3e50'
            self.entry_bg = '#34495e'
            self.btn_bg = '#415b76'
            self.btn_active_bg = '#3d5266'
            self.text_color = '#ecf0f1'
            self.special_btn = '#5b7fa3'
        else:
            self.bg_color = '#f0f3f5'
            self.entry_bg = '#ffffff'
            self.btn_bg = '#e1e5e9'
            self.btn_active_bg = '#d4d8dc'
            self.text_color = '#2c3e50'
            self.special_btn = '#7fa3b5'
        self.root.configure(bg=self.bg_color)

    def _setup_ui(self):
        """Configura los componentes de la interfaz grafica"""
        self._create_display()
        self._create_buttons()

    def _create_display(self):
        """Crea el display de la calculadora"""
        self.display_var = tk.StringVar()

        self.display = tk.Entry(
            self.root,
            font=('Fira Code', 28, 'bold'),
            textvariable=self.display_var,
            justify='right',
            bd=0,
            relief='flat',
            insertbackground=self.text_color,
            fg=self.text_color,
            bg=self.entry_bg,
            readonlybackground=self.entry_bg,
            state='readonly'
        )
        self.display.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=10,
            pady=(20, 10),
            sticky='nsew',
            ipady=15
        )

    def _create_buttons(self):
        """Crea los botones de la calculadora"""
        buttons = [
            {'text': 'AC', 'command': self.clear_all, 'grid': (1, 0)},
            {'text': 'C', 'command': self.clear, 'grid': (1, 1)},
            {'text': '⌫', 'command': self.backspace, 'grid': (1, 2)},
            {'text': '/',
                'command': lambda: self.add_to_expression('/'), 'grid': (1, 3)},
            {'text': '7', 'command': lambda: self.add_to_expression(
                '7'), 'grid': (2, 0)},
            {'text': '8', 'command': lambda: self.add_to_expression(
                '8'), 'grid': (2, 1)},
            {'text': '9', 'command': lambda: self.add_to_expression(
                '9'), 'grid': (2, 2)},
            {'text': '×', 'command': lambda: self.add_to_expression(
                '*'), 'grid': (2, 3)},
            {'text': '4', 'command': lambda: self.add_to_expression(
                '4'), 'grid': (3, 0)},
            {'text': '5', 'command': lambda: self.add_to_expression(
                '5'), 'grid': (3, 1)},
            {'text': '6', 'command': lambda: self.add_to_expression(
                '6'), 'grid': (3, 2)},
            {'text': '-',
                'command': lambda: self.add_to_expression('-'), 'grid': (3, 3)},
            {'text': '1', 'command': lambda: self.add_to_expression(
                '1'), 'grid': (4, 0)},
            {'text': '2', 'command': lambda: self.add_to_expression(
                '2'), 'grid': (4, 1)},
            {'text': '3', 'command': lambda: self.add_to_expression(
                '3'), 'grid': (4, 2)},
            {'text': '+',
                'command': lambda: self.add_to_expression('+'), 'grid': (4, 3)},
            {'text': '0', 'command': lambda: self.add_to_expression(
                '0'), 'grid': (5, 0, 1, 2)},
            {'text': '.', 'command': lambda: self.add_to_expression(
                '.'), 'grid': (5, 2)},
            {'text': '=', 'command': self.calculate, 'grid': (5, 3)},
            {'text': '☀️', 'command': self.toggle_theme, 'grid': (0, 4, 6, 1)},
        ]
        for btn in buttons:
            cols = btn['grid'] if len(
                btn['grid']) == 4 else (btn['grid'][0], btn['grid'][1], 1, 1)
            btn_obj = tk.Button(
                self.root,
                text=btn["text"],
                font=('Fira Code', 16 if btn['text']
                      not in ['=', '☀️'] else 14),
                command=btn['command'],
                bg=self.btn_bg,
                activebackground=self.btn_active_bg,
                fg=self.text_color,
                bd=0,
                relief='flat',
                padx=10,
                pady=10,
                activeforeground=self.text_color
            )
            btn_obj.grid(
                row=cols[0],
                column=cols[1],
                rowspan=cols[2],
                columnspan=cols[3],
                sticky='nsew',
                padx=2,
                pady=2
            )

        # Configuramos pesos de filas y columnas
        for i in range(6):
            self.root.rowconfigure(i, weight=1)
        for i in range(5):
            self.root.columnconfigure(i, weight=1)

    def _bind_keyboard(self):
        """Configura los atajos de teclado"""
        self.root.bind('<Return>', lambda e: self.calculate())
        self.root.bind('<BackSpace>', lambda e: self.backspace())
        self.root.bind('<Escape>', lambda e: self.clear_all())

        for char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '.']:
            self.root.bind(char, lambda e, c=char: self.add_to_expression(c))

    def add_to_expression(self, value):
        """Anade un valor a la expression actual"""
        if self.result_shown and value not in '+-*/':
            self.expression = ''
            self.result_shown = False

        self.expression += value
        self.display_var.set(self.expression)
        self.result_shown = False

    def clear(self):
        """Limpia la entrada actual"""
        self.expression = ''
        self.display_var.set('')
        self.result_shown = False

    def clear_all(self):
        "Reinicia cimpletamente la calculadora"
        self.clear()
        self.display_var.set('0')

    def backspace(self):
        """Elimina el ultimo caracter de la expresion"""
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression or 0)
        self.result_shown = False

    def calculate(self):
        """Evalua la expresion matematica"""
        try:
            # Remplazamos simbolos para la evaluacion segura
            expression = self.expression.replace('×', '*')
            result = eval(expression)

            if not isfinite(result):
                raise ValueError("Resultado no finito")

            self.expression = str(int(result) if result ==
                                  int(result) else result)
            self.display_var.set(self.expression)
            self.result_shown = True

        except ZeroDivisionError:
            self.display_var.set("Error: Division por cero")
            self.expression = ''
        except Exception as e:
            self.display_var.set("Error en expresion")
            self.expression = ''
        finally:
            self.result_shown = True

    def toggle_theme(self):
        """Cambia entre modo claro y oscuro"""
        self.dark_mode = not self.dark_mode
        self._setup_theme(self.dark_mode)
        self._setup_ui()


def resource_path(relative_path):
    """Gestión de recursos para empaquetado"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    root = tk.Tk()

    try:
        icon_path = resource_path('assets/icons/icon.ico')
        root.iconbitmap(icon_path)
    except Exception as e:
        print(f"Error loading icon: {e}")

    Calculator(root)
    root.mainloop()
