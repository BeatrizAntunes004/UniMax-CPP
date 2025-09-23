import tkinter as tk

class MeuFormulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemplo de Formulário")
        
        # Definindo o tamanho fixo do formulário
        self.root.geometry("800x600")  # Tamanho fixo de 800x600 pixels
        
        # Criando a label que será atualizada com o resultado das operações
        self.label = tk.Label(root, text="Resultado: 0", font=("Arial", 14))
        self.label.place(relx=0.5, rely=0.3, anchor='center')  # Posiciona a label no meio da tela
        
        # Criando o botão Somar com largura fixa
        self.botao_somar = tk.Button(root, text="Somar", width=10, command=self.somar)
        self.botao_somar.place(x=200, y=500)  # Posiciona o botão de Somar na posição x=200, y=500
        
        # Criando o botão Limpar com largura fixa
        self.botao_limpar = tk.Button(root, text="Limpar", width=10, command=self.limpar)
        self.botao_limpar.place(x=350, y=500)  # Posiciona o botão de Limpar na posição x=350, y=500
        
        # Criando o botão Sair com largura fixa
        self.botao_sair = tk.Button(root, text="Sair", width=10, command=self.sair)
        self.botao_sair.place(x=500, y=500)  # Posiciona o botão de Sair na posição x=500, y=500

    def somar(self):
        # Operação de soma
        resultado = 5 + 3  # Exemplo de operação (a soma de 5 e 3)
        self.label.config(text=f"Resultado: {resultado}")  # Atualiza a label com o resultado

    def limpar(self):
        # Limpar a label (zerando o resultado)
        self.label.config(text="Resultado: 0")

    def sair(self):
        # Fecha a aplicação
        self.root.quit()

# Criando a janela principal
root = tk.Tk()
formulario = MeuFormulario(root)

# Rodando a aplicação
root.mainloop()
