import tkinter as tk

class MeuFormulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemplo de Formulário")
        
        # Definindo o tamanho fixo do formulário
        self.root.geometry("800x600")  # Tamanho fixo de 800x600 pixels
        
        # Criando as labels para orientação
        self.label_num1 = tk.Label(root, text="Número 1:", font=("Arial", 12))
        self.label_num1.place(x=100, y=150)
        
        self.label_num2 = tk.Label(root, text="Número 2:", font=("Arial", 12))
        self.label_num2.place(x=100, y=200)
        
        self.label_resultado = tk.Label(root, text="Resultado:", font=("Arial", 12))
        self.label_resultado.place(x=100, y=300)  # Posiciona a label de resultado
        
        # Criando os campos de entrada (Entry) para digitação dos números
        self.entry_num1 = tk.Entry(root, font=("Arial", 12))
        self.entry_num1.place(x=200, y=150)  # Posiciona a entrada do número 1
        
        self.entry_num2 = tk.Entry(root, font=("Arial", 12))
        self.entry_num2.place(x=200, y=200)  # Posiciona a entrada do número 2
        
        # Criando o campo de resultado, que será apenas de leitura (não editável)
        self.entry_resultado = tk.Entry(root, font=("Arial", 12), state="disabled")
        self.entry_resultado.place(x=200, y=300)  # Posiciona o campo de resultado
        
        # Criando o botão Somar com largura fixa
        self.botao_somar = tk.Button(root, text="Somar", width=10, command=self.somar)
        self.botao_somar.place(x=200, y=350)  # Posiciona o botão de Somar na posição x=200, y=350
        
        # Criando o botão Limpar com largura fixa
        self.botao_limpar = tk.Button(root, text="Limpar", width=10, command=self.limpar)
        self.botao_limpar.place(x=350, y=350)  # Posiciona o botão de Limpar na posição x=350, y=350
        
        # Criando o botão Sair com largura fixa
        self.botao_sair = tk.Button(root, text="Sair", width=10, command=self.sair)
        self.botao_sair.place(x=500, y=350)  # Posiciona o botão de Sair na posição x=500, y=350

    def somar(self):
        try:
            # Obtendo os valores dos campos de entrada
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            
            # Operação de soma
            resultado = num1 + num2  # Soma dos valores digitados
            
            # Atualiza o campo de resultado com o resultado da soma
            self.entry_resultado.config(state="normal")  # Habilita temporariamente o campo de resultado para atualização
            self.entry_resultado.delete(0, tk.END)  # Limpa o campo de resultado
            self.entry_resultado.insert(0, str(resultado))  # Insere o resultado no campo
            self.entry_resultado.config(state="disabled")  # Desabilita novamente o campo de resultado para edição
        except ValueError:
            self.entry_resultado.config(state="normal")  # Habilita temporariamente para mostrar o erro
            self.entry_resultado.delete(0, tk.END)  # Limpa o campo de resultado
            self.entry_resultado.insert(0, "Erro (Entrada inválida)")  # Exibe a mensagem de erro
            self.entry_resultado.config(state="disabled")  # Desabilita novamente o campo de resultado para edição

    def limpar(self):
        # Limpar os campos de entrada e o campo de resultado
        self.entry_num1.delete(0, tk.END)
        self.entry_num2.delete(0, tk.END)
        self.entry_resultado.config(state="normal")
        self.entry_resultado.delete(0, tk.END)
        self.entry_resultado.config(state="disabled")

    def sair(self):
        # Fecha a aplicação
        self.root.quit()

# Criando a janela principal
root = tk.Tk()
formulario = MeuFormulario(root)

# Rodando a aplicação
root.mainloop()
