import tkinter as tk

form = tk.Tk()
form.geometry("800x600")
form.title("Calculadora de Compras")

# Variáveis
nome_produto = tk.StringVar()  
quantidade = tk.IntVar()  
preco_unitario = tk.DoubleVar() 
total = tk.DoubleVar() 

def calcular_total():
    valor_quantidade = quantidade.get()  # Pega a quantidade
    valor_preco = preco_unitario.get()  # Pega o preço unitário
    
    total_calculado = valor_quantidade * valor_preco
    
    total.set(total_calculado)  


label_nome = tk.Label(form, text="Nome do Produto:")
label_nome.grid(row=0, column=0, padx=10, pady=5)
nom_prod = tk.Entry(form, textvariable=nome_produto)  
nom_prod.grid(row=0, column=1, padx=10, pady=5)

label_preco = tk.Label(form, text="Preço Unitário:")
label_preco.grid(row=1, column=0, padx=10, pady=5)
prec_unic = tk.Entry(form, textvariable=preco_unitario) 
prec_unic.grid(row=1, column=1, padx=10, pady=5)

label_quantidade = tk.Label(form, text="Quantidade:")
label_quantidade.grid(row=1, column=50, padx=10, pady=5)
quant = tk.Entry(form, textvariable=quantidade) 
quant.grid(row=1, column=80, padx=10, pady=5)

Tot_label = tk.Label(form, text="Total :")
Tot_label.grid(row=3, column=0, padx=10, pady=5)

label_resultado = tk.Label(form, textvariable=total)  
label_resultado.grid(row=3, column=1, padx=10, pady=5)

btn_compra = tk.Button(form, text="Calcular Total", command=calcular_total)
btn_compra.grid(row=4, column=0, columnspan=2)

form.mainloop()