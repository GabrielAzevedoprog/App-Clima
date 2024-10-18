import tkinter
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

# Imports do back
import requests
from datetime import datetime
import json
import pytz
import pycountry_convert as pc

# Cores
global imagem
co0 = "#444466" # Preto
co1 = "#feffff" #Branco
co2 = "#6f9fbd" # Azul

bg_dia = "#6cc4cc"
bg_noite = "#484f60"

bg_main = bg_dia

#Frame Main
janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=bg_main)
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=160)


# Style Janela
estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Funcão que retorna informações
def informacao():

    chave = '14224b85c8b25ff57a6f60003706e9ca'
    cidade = e_local.get()
    api_data = 'https://api.openweathermap.org/data/2.5/weather?q={},&appid={}'.format(cidade, chave)

    # Chamando API com requests
    r = requests.get(api_data)

    # Convertendo os dados para json
    data = r.json()
    print(data)
    dados = data['sys']['country']

    # -- CIDADE --
    cidade_data = data['name']
    print(cidade_data)
    # ---FUSO---
    zona_fuso = pytz.country_timezones[dados]

    # --PAIS--
    pais_data = pytz.country_names[dados]

    # --ZONA--
    zona_data = pytz.timezone(zona_fuso[0])

    zona_horas = datetime.now(zona_data)
    zona_horas = zona_horas.strftime("%d %M %Y | %H:%M:%S %p")

    # --TEMPO--
    tempo_data = data['main']['temp']
    pressao_data = data['main']['pressure']
    humidade_data = data['main']['humidity']
    velocidade_data = data['wind']['speed']
    descricao_data = data['weather'][0]['description']

    # Corrigindo Informações
    def pais_continente(i):
        pais_alpha = pc.country_name_to_country_alpha2(i)
        pais_continente_code = pc.country_alpha2_to_continent_code(pais_alpha)
        pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continente_code)
        return pais_continente_nome

    continente = pais_continente(pais_data)

    # Mudando Labels
    l_cidade['text'] = cidade_data + ' - ' + pais_data + ' / ' + continente
    l_data['text'] = zona_horas
    l_humidade['text'] = humidade_data
    l_pressao['text'] = 'Pressão Atmosferica: ' + str(pressao_data)
    l_velocidade['text'] = 'Velocidade dos Ventos: ' + str(velocidade_data)
    l_descricao['text'] = descricao_data

    # Mudando Fundo
    global img_data
    zona_periodo = datetime.now(zona_data)
    zona_periodo = zona_periodo.strftime("%H")

    zona_periodo = int(zona_periodo)

    if zona_periodo <= 5 or zona_periodo >=17:
        img_data = Image.open('midia/lua.png')
        bg_main = bg_noite
    elif zona_periodo >= 6 or zona_periodo <= 16:
        img_data = Image.open('midia/sol.png')
        bg_main = bg_dia

    img_data = ImageTk.PhotoImage(img_data)
    l_img =Label(frame_body, image=img_data, bg=bg_main)
    l_img.place(x=190, y=70)

    l_cidade['bg'] = bg_main
    l_data['bg'] = bg_main
    l_humidade['bg'] = bg_main
    l_hnome['bg'] = bg_main
    l_hsimbolo['bg'] = bg_main
    l_pressao['bg'] = bg_main
    l_velocidade['bg'] = bg_main
    l_descricao['bg'] =  bg_main

    janela.configure(bg=bg_main)
    frame_header.configure(bg=bg_main)
    frame_body.configure(bg=bg_main)
    

#Frame Header
frame_header = Frame(janela, width=320, height=50, bg=co1, pady=0, padx=0)
frame_header.grid(row=1, column=0)

e_local = Entry(frame_header, width=20, justify='left', font=('',10), highlightthickness=1, relief='solid')
e_local.place(x=45, y=14)

b_ver =Button(frame_header, command=informacao, text='Verificar Clima', bg=co1, fg=co2, font=('Ivy 8 bold'), highlightthickness=1, relief='raised', overrelief=RIDGE)
b_ver.place(x=210, y=12)


#Frame Body
frame_body = Frame(janela, width=320, height=300, bg=bg_main, pady=12, padx=0)
frame_body.grid(row=2, column=0, sticky=NW)

l_cidade =Label(frame_body, text='Cabinda - Angola | Africa', anchor='center', bg=bg_main, fg=co1, font=('Arial 12'))
l_cidade.place(x=10, y=4)

l_data =Label(frame_body, text='16 10 2024 | 10:35:00 AM', anchor='center', bg=bg_main, fg=co1, font=('Arial 10'))
l_data.place(x=10, y=54)

l_humidade =Label(frame_body, text='84', anchor='center', bg=bg_main, fg=co1, font=('Arial 40'))
l_humidade.place(x=10, y=100)

l_hsimbolo =Label(frame_body, text='%', anchor='center', bg=bg_main, fg=co1, font=('Arial 9 bold'))
l_hsimbolo.place(x=85, y=115)

l_hnome =Label(frame_body, text='Humidade', anchor='center', bg=bg_main, fg=co1, font=('Arial 7'))
l_hnome.place(x=80, y=135)

l_pressao =Label(frame_body, text='Pressão : 1000', anchor='center', bg=bg_main, fg=co1, font=('Arial 10'))
l_pressao.place(x=10, y=184)

l_velocidade =Label(frame_body, text='Velocidade do Vento : 1000', anchor='center', bg=bg_main, fg=co1, font=('Arial 10'))
l_velocidade.place(x=10, y=212)

img_data = Image.open('midia/sol.png')
img_data = ImageTk.PhotoImage(img_data)
l_img =Label(frame_body, image=img_data, bg=bg_main)
l_img.place(x=190, y=70)

l_descricao =Label(frame_body, text='Nublado', anchor='center', bg=bg_main, fg=co1, font=('Arial 10'))
l_descricao.place(x=215, y=170)






janela.mainloop()