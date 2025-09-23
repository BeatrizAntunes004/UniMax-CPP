import tkinter as tk
class MeuFormulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemplo de Formulário")

# Criando um botão
        self.botao = tk.Button(root, text="Clique Aqui", command=self.on_click)
        self.botao.pack()

# Criando uma label para mostrar o texto do evento
        self.label = tk.Label(root, text="Esperando o clique...")
        self.label.pack()
    def on_click(self):
        self.label.config(text="Botão clicado!")
# Criando a janela principal
root = tk.Tk()
formulario = MeuFormulario(root)
# Rodando a aplicação
root.mainloop()
