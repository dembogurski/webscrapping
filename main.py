import tkinter as tk
from tkinter import Frame, IntVar

def procesar_texto():
    # Obtén el texto del área de texto
    texto = area_texto.get("1.0", "end-1c")

    # Procesa el texto (por ejemplo, muestra un mensaje con el texto)
    print(f"Texto procesado: {texto}")
    # Asegúrate de utilizar .get() para obtener el valor actual de la variable de control
    print(f"Valor seleccionado: {valor_seleccionado.get()}")

ventana = tk.Tk()
ventana.geometry("640x480")
ventana.title("Qubit Web Scrapping Program")

# Inicializa la variable de control después de crear la ventana
valor_seleccionado = IntVar()

marco_radio_buttons = Frame(ventana)
marco_radio_buttons.pack()

# Crea un Radio Button para la opción "Opción 1"
radio_button_1 = tk.Radiobutton(marco_radio_buttons, text="Visao Vip", variable=valor_seleccionado, value=1)
radio_button_1.pack(side=tk.LEFT)

# Crea un Radio Button para la opción "Opción 2"
radio_button_2 = tk.Radiobutton(marco_radio_buttons, text="Otra Pagina (A Desarrollar)", variable=valor_seleccionado, value=2)
radio_button_2.pack(side=tk.LEFT)

# Crea un área de texto
area_texto = tk.Text(ventana, width=60, height=8)
area_texto.pack()

boton_cancelar = tk.Button(ventana, text="Cancelar", command=ventana.destroy)
boton_cancelar.pack(side=tk.LEFT)

boton_procesar = tk.Button(ventana, text="Procesar", command=procesar_texto)
boton_procesar.pack(side=tk.RIGHT)

ventana.mainloop()
