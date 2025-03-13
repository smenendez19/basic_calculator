# Modulos a utilizar
import os
import sys
from tkinter import (
    DISABLED,
    Button,
    E,
    Entry,
    Frame,
    Menu,
    N,
    S,
    StringVar,
    Tk,
    W,
    messagebox,
)

# Otras funciones


def mensajeInfo():
    messagebox.showinfo(
        "Acerca del programa",
        "Programa realizado por Santiago Menendez siguiendo el tutorial de Pildoras Informaticas, modificado para diferenciar de otros",
    )


# Ventana principal
root = Tk()
root.title("Calculadora")
root.geometry("260x270+500+200")
root.resizable(0, 0)
root.iconbitmap(os.path.join(os.path.dirname(sys.argv[0]), "src", "logo.ico"))
miFrame = Frame(root)
miFrame.pack()


# Variables globales necesarias
numeroPantalla = StringVar()
operacion = ""
flagOp = 0
resultado = 0

# Pantalla
pantalla = Entry(miFrame, textvariable=numeroPantalla, font=("arial", 15))
pantalla.grid(row=1, column=0, ipady=20, columnspan=4, sticky=W + E + N + S)
pantalla.config(state=DISABLED, justify="right", disabledbackground="black", disabledforeground="white")

# Menu
barraMenu = Menu(root)
root.config(menu=barraMenu)
ayudamenu = Menu(barraMenu, tearoff=0)
ayudamenu.add_command(label="Acerca de", command=mensajeInfo)
barraMenu.add_cascade(label="Ayuda", menu=ayudamenu)

# Funciones de la pantalla


def numeroPulsado(num):
    global operacion
    global flagOp
    if flagOp != 0:
        numeroPantalla.set(num)
        flagOp = 0
    else:
        if numeroPantalla.get() == "0" and num == "0":
            numeroPantalla.set("0")
        elif numeroPantalla.get() == "0" and num == ".":
            numeroPantalla.set(numeroPantalla.get() + num)
        elif numeroPantalla.get() == "0":
            numeroPantalla.set("" + num)
        else:
            cont = numeroPantalla.get().count(".")
            if cont >= 1 and num == ".":
                numeroPantalla.set(numeroPantalla.get())
            else:
                numeroPantalla.set(numeroPantalla.get() + num)


def sumar(num):
    global operacion
    global resultado
    global flagOp
    resultado += float(num)
    operacion = "suma"
    flagOp = 1
    numeroPantalla.set(resultado)


def restar(num):
    global operacion
    global resultado
    global flagOp
    if resultado == 0:
        resultado = float(num)
    else:
        resultado = resultado - float(num)
    operacion = "resta"
    flagOp = 1
    numeroPantalla.set(resultado)


def multiplicar(num):
    global operacion
    global resultado
    global flagOp
    if resultado == 0:
        resultado = float(num)
    else:
        resultado = resultado * float(num)
    operacion = "multiplicacion"
    flagOp = 1
    numeroPantalla.set(resultado)


def dividir(num):
    global operacion
    global resultado
    global flagOp
    if resultado == 0:
        resultado = float(num)
    else:
        resultado = resultado / float(num)
    operacion = "division"
    flagOp = 1
    numeroPantalla.set(resultado)


def elResultado():
    global resultado
    global operacion
    global flagOp
    if operacion == "suma":
        numeroPantalla.set(resultado + float(numeroPantalla.get()))
    elif operacion == "resta":
        numeroPantalla.set(resultado - float(numeroPantalla.get()))
    elif operacion == "multiplicacion":
        numeroPantalla.set(resultado * float(numeroPantalla.get()))
    elif operacion == "division":
        try:
            numeroPantalla.set(resultado / float(numeroPantalla.get()))
        except ArithmeticError:
            numeroPantalla.set("ERROR MATEMATICO")
    resultado = 0
    flagOp = 1
    operacion = "resultado"


# Botones
# Fila 1
boton7 = Button(miFrame, text="7", width=5, command=lambda: numeroPulsado("7"))
boton7.grid(row=2, column=0, ipadx=10, ipady=10)

boton8 = Button(miFrame, text="8", width=5, command=lambda: numeroPulsado("8"))
boton8.grid(row=2, column=1, ipadx=10, ipady=10)

boton9 = Button(miFrame, text="9", width=5, command=lambda: numeroPulsado("9"))
boton9.grid(row=2, column=2, ipadx=10, ipady=10)

botonMultiplicar = Button(miFrame, text="X", width=5, command=lambda: multiplicar(numeroPantalla.get()))
botonMultiplicar.grid(row=2, column=3, ipadx=10, ipady=10)

# Fila 2
boton4 = Button(miFrame, text="4", width=5, command=lambda: numeroPulsado("4"))
boton4.grid(row=3, column=0, ipadx=10, ipady=10)

boton5 = Button(miFrame, text="5", width=5, command=lambda: numeroPulsado("5"))
boton5.grid(row=3, column=1, ipadx=10, ipady=10)

boton6 = Button(miFrame, text="6", width=5, command=lambda: numeroPulsado("6"))
boton6.grid(row=3, column=2, ipadx=10, ipady=10)

botonDividir = Button(miFrame, text="/", width=5, command=lambda: dividir(numeroPantalla.get()))
botonDividir.grid(row=3, column=3, ipadx=10, ipady=10)

# Fila 3

boton1 = Button(miFrame, text="1", width=5, command=lambda: numeroPulsado("1"))
boton1.grid(row=4, column=0, ipadx=10, ipady=10)

boton2 = Button(miFrame, text="2", width=5, command=lambda: numeroPulsado("2"))
boton2.grid(row=4, column=1, ipadx=10, ipady=10)

boton3 = Button(miFrame, text="3", width=5, command=lambda: numeroPulsado("3"))
boton3.grid(row=4, column=2, ipadx=10, ipady=10)

botonSumar = Button(miFrame, text="+", width=5, command=lambda: sumar(numeroPantalla.get()))
botonSumar.grid(row=4, column=3, ipadx=10, ipady=10)

# Fila 4

boton0 = Button(miFrame, text="0", width=5, command=lambda: numeroPulsado("0"))
boton0.grid(row=5, column=0, ipadx=10, ipady=10)

botonComa = Button(miFrame, text=".", width=5, command=lambda: numeroPulsado("."))
botonComa.grid(row=5, column=1, ipadx=10, ipady=10)

botonRestar = Button(miFrame, text="-", width=5, command=lambda: restar(numeroPantalla.get()))
botonRestar.grid(row=5, column=2, ipadx=10, ipady=10)

botonResultado = Button(miFrame, text="=", width=5, command=lambda: elResultado())
botonResultado.grid(row=5, column=3, ipadx=10, ipady=10)

root.mainloop()
