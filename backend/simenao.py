from tkinter import *
import subprocess
from backend.novatabela import janela_reposta
import backend.calculo as calculo

def JanelaSimENao():
    def botao_sim_clicado():
        calculo.calculo()
        janela.destroy()
        janela_reposta()

    def botao_nao_clicado():
        calculo.calculo()
        janela.destroy()
        subprocess.run(["python", "main.py"])

    janela = Tk()
    janela.title("RESPOSTAS")
    
    # Criar texto de mensagem
    mensagem = StringVar()
    mensagem.set("Tem certeza que deseja criar uma nova tabela?\nAo começar uma nova tabela você apagará a existente do mesmo mês!")
    output_label = Label(janela, textvariable=mensagem, font=("Arial", 16))
    output_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Criar botão "Sim"
    botao_sim = Button(janela, text="SIM", command=botao_sim_clicado, font=("Arial", 14))
    botao_sim.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    # Criar botão "Não"
    botao_nao = Button(janela, text="NÃO", command=botao_nao_clicado, font=("Arial", 14))
    botao_nao.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    janela.update_idletasks()  # Atualizar a renderização dos elementos
    
    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    # Calcular as coordenadas da janela para centralizá-la
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    
    janela.geometry(f"+{pos_x+2}+{pos_y+2}")  # Definir as coordenadas da janela
    janela.resizable(False, False)

    janela.mainloop()