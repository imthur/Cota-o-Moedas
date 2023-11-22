import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic.get('USDBRL', {}).get('bid', 'N/A')
    cotacao_euro = requisicao_dic.get('EURBRL', {}).get('bid', 'N/A')
    cotacao_btc = requisicao_dic.get('BTCBRL', {}).get('bid', 'N/A')

    texto = f'''
    Dólar: R$ {cotacao_dolar}
    Euro: R$ {cotacao_euro}
    BTC: R$ {cotacao_btc}'''

    textoCotacoes["text"] = texto

def centralizar(jan):
    jan.grid_configure(pady=(janela.winfo_height() - jan.winfo_height()) // 2,
                          padx=(janela.winfo_width() - jan.winfo_width()) // 2)

janela = Tk()
janela.title("Cotação Atual de Moedas")

janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_rowconfigure(2, weight=1)
janela.grid_columnconfigure(0, weight=1)

estilo_titulo = ("Helvetica", 14, "bold")
estilo_texto = ("Helvetica", 12)

texto_inicial = Label(janela, text='Clique no botão para ver as cotações atualizadas', font=estilo_texto)
texto_inicial.grid(column=0, row=0)
centralizar(texto_inicial)

botao = Button(janela, text="Atualizar Cotações", command=pegar_cotacoes, font=estilo_texto)
botao.grid(column=0, row=1)
centralizar(botao)

global textoCotacoes
textoCotacoes = Label(janela, text=f'''
Dólar: R$ 0
Euro: R$ 0
BTC: R$ 0
Cotações ainda não atualizadas.''', font=estilo_texto)
textoCotacoes.grid(column=0, row=2)
centralizar(textoCotacoes)

largura_janela = 700
altura_janela = 700

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

x = (largura_tela - largura_janela) // 2
y = (altura_tela - altura_janela) // 2

janela.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')

janela.mainloop()