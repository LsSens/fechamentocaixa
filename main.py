from tkinter import *
from tkinter import ttk
from datetime import date
import pywhatkit
import backend.simenao as simenao
import backend.addfaturamento as addfaturamento
import backend.tabela as tabela
import backend.calculo as calculo
import os

def criar_tabela():
    calculo.calculo()
    window.destroy()
    simenao.JanelaSimENao()
    # Seu código para criar uma nova tabela

def adicionar_faturamento():
    calculo.calculo()
    window.destroy()
    addfaturamento.addfaturamento()
    # Seu código para adicionar faturamento diário

def mostrartabela():
    calculo.calculo()
    window.destroy()
    tabela.mostrartabela()

def enviar_whatsapp():
    calculo.calculo()
    data_atual = date.today()
    localdatabela = os.path.abspath(os.path.join("cfg", f"{data_atual.month}-{data_atual.year}.txt")) # Diretorio da tabela
    with open(localdatabela, "r", encoding="utf-8") as dados:
            texto = dados.read()
            pywhatkit.sendwhatmsg_instantly("+5513988834648", texto)
    # Seu código para enviar informações pelo WhatsApp

window = Tk()
window.title("Opções")

# Estilo temático
style = ttk.Style()
style.theme_use("vista")  # Escolha o tema que desejar (por exemplo, "clam", "default", "alt", "vista", etc.)

# Componentes da interface
label = Label(window, text="Tabela meta PokoLoko", font=("Arial", 16))

label.pack(pady=20)

nova_tabela_button = Button(window, text="Criar nova tabela", command=criar_tabela, font=("Arial", 14))
nova_tabela_button.pack(pady=10)

adicionar_faturamento_button = Button(window, text="Adicionar faturamento", command=adicionar_faturamento, font=("Arial", 14))
adicionar_faturamento_button.pack(pady=10)

enviar_whatsapp_button = Button(window, text="Enviar pelo WhatsApp", command=enviar_whatsapp, font=("Arial", 14))
enviar_whatsapp_button.pack(pady=10)

mostrartabela = Button(window, text="Mostrar Tabela", command=mostrartabela, font=("Arial", 14))
mostrartabela.pack(pady=10)
window.update_idletasks()

largura_tela = window.winfo_screenwidth()
altura_tela = window.winfo_screenheight()
    
# Calcular as coordenadas da janela para centralizá-la
largura_janela = window.winfo_width()
altura_janela = window.winfo_height()
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
window.geometry(f"+{pos_x+2}+{pos_y+2}")
window.resizable(False, False)

window.mainloop()
