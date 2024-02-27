from tkinter import *
from datetime import date
import subprocess
import backend.calculo as calculo
import os

data_atual = date.today()
calculo.calculo()

def CriandoArquivo(DiasMes, metamaxima, metaminima, diasdetrabalho):
    
    # Criando as lnhas padrões de todos mês
    with open(f"cfg/{data_atual.month}-{data_atual.year}.txt", 'w', encoding='utf-8') as arquivo:
        for m in range(1,32):
            if m >= DiasMes:
                arquivo.write(' ' + '\n')
            else:
                if m < 10:
                    arquivo.write(f'DIA 0{m}: R$ 0' + '\n')
                else:
                    arquivo.write(f'DIA {m}: R$ 0' + '\n')
        arquivo.write('\n' + f'Total: R$ 0' + '\n')
        arquivo.write(f'Meta maxima: R$ 0' + '\n')
        arquivo.write(f'Meta mínima: R$ 0' + '\n')
        arquivo.write(f'Faltante para meta total: R$ 0' + '\n')
        arquivo.write(f'Faltante para meta mínima: R$ 0' + '\n')
        arquivo.write(f'Para bater a meta mínima, você precisa fazer por dia: R$ 0' + '\n')
        arquivo.write(f'Para bater a meta total, você precisa fazer por dia: R$ 0')
    arquivo.close()

    # Adicionando os parametros passado pelo usuario
    with open(f"cfg/{data_atual.month}-{data_atual.year}.txt", 'r', encoding='utf-8') as dados:
        texto = dados.readlines()
        texto[33] = ''
        texto.insert(34 , f'Meta maxima: R$ {metamaxima:,.2f}' + '\n')
    with open(f"cfg/{data_atual.month}-{data_atual.year}.txt", 'w', encoding="utf-8") as escrita:
        escrita.writelines(texto)
    with open(f"cfg/{data_atual.month}-{data_atual.year}.txt", 'r', encoding='utf-8') as dados:
        texto = dados.readlines()
        texto[34] = ''
        texto.insert(35 , f'Meta mínima: R$ {metaminima:,.2f}' + '\n')
    with open(f"cfg/{data_atual.month}-{data_atual.year}.txt", 'w', encoding="utf-8") as escrita:
        escrita.writelines(texto)
    escrita.close()
    dados.close()

    with open("cfg/config.txt", 'w', encoding='utf-8') as dados:
        if diasdetrabalho < 10:
            if data_atual.month < 10:
                dados.write(f'Dias de trabalho mês 0{data_atual.month}: 0{diasdetrabalho}')
            else: 
                dados.write(f'Dias de trabalho mês {data_atual.month}: 0{diasdetrabalho}')
        else:
            if data_atual.month < 10:
                dados.write(f'Dias de trabalho mês 0{data_atual.month}: {diasdetrabalho}')
            else: 
                dados.write(f'Dias de trabalho mês {data_atual.month}: {diasdetrabalho}')


def janela_reposta():

    textodiasmes = str("Quantos dias tem o mês?")
    textodiasmeserror = str("Quantos dias tem o mês?\n Digite um dia válido!")
    textometamaxima = str("Qual a meta maxima desse mês? (ex: R$ 112345.32)")
    textometamaximaerror = str("Qual a meta maxima desse mês? (ex: R$ 112345.32)\n Digite um valor válido!")
    textometaminima = str("Qual a meta mínima desse mês? (ex: R$ 112345.32)")
    textometaminimaerror = str("Qual a meta mínima desse mês? (ex: R$ 112345.32)\n Digite um valor válido!")
    textodiastrabalho = str("Você vai trabalhar quantos dias esse mês?")
    textodiastrabalhoerror = str("Você vai trabalhar quantos dias esse mês?\nDigite um dia válido!")

    #Apagar conteudo da caixa de texto
    def apagarentrada():
        entrada.delete(0, END)
              
    # Gerar Perguntas
    def Pergunta1(resposta):
        if resposta.isdigit() == True and int(resposta) > 27 and int(resposta) < 32:
            global DiasMes
            DiasMes = int(resposta)+1
            apagarentrada()
            mensagem.set(textometamaxima) # Setar proximo texto visivel
        else:
            apagarentrada()
            mensagem.set(textodiasmeserror) 
        janela.update

    def Pergunta2(resposta):
        try: 
            float(resposta)
            global metamaxima
            metamaxima = float(resposta)
            apagarentrada()
            mensagem.set(textometaminima)  # Setar proximo texto visivel
        except:
            apagarentrada()
            mensagem.set(textometamaximaerror)

    def Pergunta3(resposta):
        try: 
            float(resposta)
            global metaminima
            metaminima = float(resposta)
            apagarentrada()
            mensagem.set(textodiastrabalho) # Setar proximo texto visivel
        except:
            apagarentrada()
            mensagem.set(textometaminimaerror)   

    def Pergunta4(resposta):
        try: 
            int(resposta)
            if int(resposta) < 32 and int(resposta) > 0:
                global diasdetrabalho
                diasdetrabalho = int(resposta)
                apagarentrada()
                print(diasdetrabalho)
                CriandoArquivo(DiasMes, metamaxima, metaminima, diasdetrabalho)
                janela.destroy()
                calculo.calculo()
                subprocess.run(["python", "main.py"])
            else:
                apagarentrada()
                mensagem.set(textodiastrabalhoerror) 
        except:
            apagarentrada()
            mensagem.set(textodiastrabalhoerror)   

    # Obter resposta
    def obter_resposta():
        calculo.calculo()
        resposta = entrada.get()  # Obter o texto inserido na caixa de texto
        if mensagem.get() == textodiasmes or mensagem.get() == textodiasmeserror:
            Pergunta1(resposta)
            return
        if mensagem.get() == textometamaxima or mensagem.get() == textometamaximaerror:
            Pergunta2(resposta)
            return
        if mensagem.get() == textometaminima or mensagem.get() == textometaminimaerror:
            Pergunta3(resposta)
            return
        if mensagem.get() == textodiastrabalho or mensagem.get() == textodiastrabalhoerror:
            Pergunta4(resposta)
            return
    
    janela = Tk()
    janela.title("RESPOSTAS")

    # Criar texto de mensagem
    mensagem = StringVar()
    mensagem.set("Quantos dias tem o mês?")
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
    
    janela.geometry(f"+{pos_x+2}+{pos_y+2}")  # Definir as coordenadas da janela
    janela.resizable(False, False)

    janela.mainloop()
