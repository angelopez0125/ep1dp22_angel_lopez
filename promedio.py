import tkinter

ventana = tkinter.Tk()
ventana.geometry("700x700")
resultado = 0.0

def prom():
    resultado = (float(txt_valor1.get()) + float(txt_valor2.get()) + float(txt_valor3.get()) + float(txt_valor4.get()) + float(txt_valor5.get())) // 5
    lbl_resultado["text"]= resultado

lbl_Titulo = tkinter.Label(ventana, text="PROMEDIO", font=("Arial", 24))
lbl_Titulo.pack()

lbl_valor1 = tkinter.Label(ventana, text="Valor 1", font=("Arial", 24))
lbl_valor1.pack(fill = tkinter.X)
txt_valor1 = tkinter.Entry(ventana, font=("Arial", 24))
txt_valor1.pack(fill = tkinter.X) 

lbl_valor2 = tkinter.Label(ventana, text="Valor 2", font=("Arial", 24))
lbl_valor2.pack(fill = tkinter.X)
txt_valor2 = tkinter.Entry(ventana, font=("Arial", 24))
txt_valor2.pack(fill = tkinter.X) 

lbl_valor3 = tkinter.Label(ventana, text="Valor 3", font=("Arial", 24))
lbl_valor3.pack(fill = tkinter.X)
txt_valor3 = tkinter.Entry(ventana, font=("Arial", 24))
txt_valor3.pack(fill = tkinter.X) 

lbl_valor4 = tkinter.Label(ventana, text="Valor 4", font=("Arial", 24))
lbl_valor4.pack(fill = tkinter.X)
txt_valor4 = tkinter.Entry(ventana, font=("Arial", 24))
txt_valor4.pack(fill = tkinter.X) 

lbl_valor5 = tkinter.Label(ventana, text="Valor 5", font=("Arial", 24))
lbl_valor5.pack(fill = tkinter.X)
txt_valor5 = tkinter.Entry(ventana, font=("Arial", 24))
txt_valor5.pack(fill = tkinter.X) 


btn_promedio = tkinter.Button(ventana, text="Promedio", font=("Arial Black", 24), bg="blue", command= prom)
btn_promedio.pack(fill = tkinter.X)

lbl_resultado = tkinter.Label(ventana, text="Resultado", font=("Arial", 24))
lbl_resultado.pack(fill = tkinter.X)



ventana.mainloop()