import tkinter as tk


if __name__ == "__main__":
    print("Hello")
    # Configuración de la ventana principal
    ventana_calculadora = tk.Tk()
    ventana_calculadora.title('Calculadora')
    ventana_calculadora.configure(bg='#2c3e50')

    # Configuración del icono
    ruta_icono_ventana = "assets/icons/icono_ventana_calculadora.ico"
    ventana_calculadora.iconbitmap(ruta_icono_ventana)

    # Variable para el visor
    texto_en_pantalla = tk.StringVar()

    # Configuración del visor
    pantalla = tk.Entry(ventana_calculadora,
                        font=("Helvetica", 24),
                        justify="right",
                        bd=0,
                        fg="white",
                        bg="#34495e",
                        insertbackground="white",
                        relief="solid",
                        highlightthickness=0,
                        width=16,
                        textvariable=texto_en_pantalla)

    pantalla.grid(row=0, column=0, columnspan=4, ipadx=20, ipady=20)

    # Lista de botones
    lista_simbolos_botones = [
        ('/', 1, 0), ('FV', 1, 1), ('C', 1, 2), ('AC', 1, 3),
        ('*', 2, 0), ('7', 2, 1), ('8', 2, 2), ('9', 2, 3),
        ('-', 3, 0), ('4', 3, 1), ('5', 3, 2), ('6', 3, 3),
        ('+', 4, 0), ('1', 4, 1), ('2', 4, 2), ('3', 4, 3),
        ('0', 5, 2), (',', 5, 3)
    ]

    # Crear los botones
    for (texto, fila, columna) in lista_simbolos_botones:
        boton = tk.Button(ventana_calculadora,
                          text=texto,
                          font=("Helvetica", 18),
                          fg="white",
                          bg="#2c3e50",
                          activebackground="#34495e",
                          relief="solid",
                          bd=2,
                          width=5,
                          height=2,
                          # Asignar función
                          command=lambda t=texto: btn_press(t))
        boton.grid(row=fila, column=columna)

    # Botón especial "F+V"
    boton_FV = tk.Button(ventana_calculadora,
                         text="LV",
                         font=("Helvetica", 18),
                         fg="#ecf0f1",
                         bg="#5b7fa3",
                         activebackground="#16a085",
                         relief="solid",
                         bd=2,
                         width=5,
                         height=2,
                         command=lambda t="VF": btn_press(t))
    boton_FV.grid(row=1, column=1)

    # Botón "=" (sin funcionalidad aún)
    boton_resultado = tk.Button(ventana_calculadora,
                                text='=',
                                font=("Helvetica", 18),
                                fg="white",
                                bg="#2c3e50",
                                activebackground="#34495e",
                                relief="solid",
                                bd=2,
                                width=5,
                                height=2)
    boton_resultado.grid(row=5, column=0, columnspan=2, ipadx=40)

    # Configuración de la grilla
    for i in range(6):
        ventana_calculadora.grid_rowconfigure(i, weight=1)

    for i in range(4):
        ventana_calculadora.grid_columnconfigure(i, weight=1)

    ventana_calculadora.mainloop()
