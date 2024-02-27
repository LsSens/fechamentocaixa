from tkinter import *
from datetime import date
import backend.calculo as calculo
import os
import subprocess

data_atual = date.today() 
calculo.calculo()

def Calculos(diadofaturamento, faturamentodia):

    with open(f"cfg/{data_atual.month}-{data_atual.year}.txt", 'r', encoding='utf-8') as dados:
        texto = dados.readlines()
        texto[diadofaturamento-1] = ''
        if diadofaturamento < 10:
            texto.insert(diadofaturamento, f'DIA 0{diadofaturamento}: R$ {faturamentodia:,.2f}' + '\n')
        else:
            texto.insert(diadofaturamento, f'DIA {diadofaturamento}: R$ {faturamentodia:,.2f}' + '\n')
    with open(f"cfg/{data_atual.month}-{data_atual.year}.txt", 'w', encoding="utf-8") as escrita:
        escrita.writelines(texto)
    calculo.calculo()

def addfaturamento():
    textodiafaturamento = str("Qual o dia deseja adicionar o faturamento?")
    textodiafaturamentoerror = str("Qual o dia deseja adicionar o faturamento?\n Digite um dia válido!")

    def Pergunta1(resposta):
        try:
            int(resposta)
            if int(resposta) < 32:
                global diadofaturamento
                diadofaturamento = int(resposta)
                entrada.delete(0, END)
                global textovalorfaturamento
                global textovalorfaturamentoerror
                textovalorfaturamento = str(f"Qual o faturamento do dia {diadofaturamento}?")
                textovalorfaturamentoerror = str(f"Qual o faturamento do dia {diadofaturamento}?\n Digite um valor válido")
                mensagem.set(textovalorfaturamento) # Setar proximo texto visivel
        except:
            entrada.delete(0, END)
            mensagem.set(textodiafaturamentoerror)
        janela.update()

    def Pergunta2(resposta):
        if float(resposta):
            global faturamentodia
            faturamentodia = float(resposta)
            Calculos(diadofaturamento, faturamentodia)
            entrada.delete(0, END)
            janela.destroy()
            calculo.calculo()
            subprocess.run(["python", "main.py"])
        else:
            entrada.delete(0, END)
            mensagem.set(textovalorfaturamentoerror)
        janela.update()


    def obter_resposta():
        resposta = entrada.get()  # Obter o texto inserido na caixa de texto
        if mensagem.get() == textodiafaturamento or mensagem.get() == textodiafaturamentoerror:
            Pergunta1(resposta)
            return
        if mensagem.get() == textovalorfaturamento or mensagem.get() == textovalorfaturamentoerror:
            Pergunta2(resposta)
            return

    janela = Tk()
    janela.title("Adicionar Faturamento!")

    # Criar texto de mensagem
    mensagem = StringVar()
    mensagem.set(textodiafaturamento)
    output_label = Label(janela, textvariable=mensagem, font=("Arial", 16))
    output_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Criar a caixa de texto
    entrada = Entry(janela, font=("Arial", 14))
    entrada.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Criar o botão
    botao = Button(janela, text="OK", command=obter_resposta, font=("Arial", 14))
    botao.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    janela.update_idletasks()  # Atualizar a renderização dos elementos
    
    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    # Calcular as coordenadas da janela para centralizá-la
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    
    janela.geometry(f"+{pos_x+2}+{pos_y+2}")
    janela.resizable(False, False)  # Definir as coordenadas da janela
    
    janela.mainloop()