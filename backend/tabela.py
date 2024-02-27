from tkinter import *
import subprocess
from datetime import date
import backend.calculo as calculo


def mostrartabela():
    data_atual = date.today()
    calculo.calculo()
    def voltar():
        janela.destroy()
        subprocess.run(["python", "main.py"])

    janela = Tk()
    janela.title("Tabela")
    
    # Criar texto de mensagem
    with open(f"cfg/{data_atual.month}-{data_atual.year}.txt", "r", encoding="utf-8") as dados:
        texto = dados.read()

    mensagem = StringVar()
    mensagem.set(texto)
    output_label = Label(janela, textvariable=mensagem, font=("Arial", 12))
    output_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Criar botão "Sim"
    botao_sim = Button(janela, text="Voltar", command=voltar, font=("Arial", 14))
    botao_sim.grid(row=1, column=0, padx=5, pady=5, sticky="e")

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