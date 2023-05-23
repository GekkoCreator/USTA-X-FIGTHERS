# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:03:28 2023

@author: jfern
"""
import streamlit as st
import pandas as pd
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sqlite3

 

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('sheets.json', scope)
client = gspread.authorize(credentials)

#spreadsheet = client.create('figthersbd')

spreadsheet = client.open('figthersbd')

#spreadsheet.share('jfernandoardila10@gmail.com', perm_type='user', role='writer')

class RowData:
    def __init__(self, user, title, comment):
        self.user = user
        self.title = title
        self.comment = comment
        
worksheet = spreadsheet.sheet1

# Define the headers
headers = ['user', 'title', 'comment']

# Insert the headers in the first row
#worksheet.append_row(headers)

user_values = worksheet.col_values(1)  # Column A
title_values = worksheet.col_values(2)  # Column B
comment_values = worksheet.col_values(3)  # Column C


rows = []
        

# Definimos las páginas de nuestra aplicación
pagina_inicio = "Inicio"
pagina_infoproyecto = "Nuestro proyecto"
pagina_personajes= "Personajes"
pagina_prueba="ForoFigthers"


# Creamos un selectbox en la barra lateral para seleccionar la página
pagina_seleccionada = st.sidebar.selectbox(
    "Selecciona una página",
    [pagina_inicio, pagina_infoproyecto, pagina_personajes, pagina_prueba]
)


st.experimental_set_query_params(pagina=pagina_seleccionada)

# Mostramos el contenido de la página seleccionada
if pagina_seleccionada == pagina_inicio:
        st.snow()
    
 
        st.markdown("<h1 style='text-align: center;'>USTA X-FIGTHERS</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Combate con honor, vence con gloria</h2>", unsafe_allow_html=True)
        st.write('')
        st.write('')
        st.write('')
        st.write('')
       
        st.write('')

        from PIL import Image

        image = 'sakura.gif'

        st.image(image, use_column_width=True)
        
        st.markdown("<p style='text-align: justify;'>¡Bienvenido al juego de combate de la facultad de telecomunicaciones! En este emocionante juego, los personajes principales son los profesores de la facultad de telecomunicaciones, y el objetivo es luchar y derrotar a tu oponente. Este es un juego de dos personas, por lo que necesitarás a un amigo para unirse a la batalla.</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: justify;'>Durante el juego, los jugadores pueden lanzar ataques y defenderse de los ataques de su oponente. La estrategia y la táctica son fundamentales para ganar el juego, así que asegúrate de pensar bien tus movimientos antes de actuar.</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: justify;'>El juego termina cuando uno de los jugadores ha perdido todas sus vidas. El jugador con vidas restantes será declarado el ganador y será coronado como el campeón del juego de combate de la facultad de telecomunicaciones.</p>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>¡Que empiece la batalla!</h1>", unsafe_allow_html=True)
        
        st.write('')
        st.write('')
        st.write('')
        st.write('')
       
        st.write('')
        
        

        
        col1, col2, col3 = st.columns(3)
        
        with col1: 
            santotoprl ='santoto.png'
            
            urlsantoto = 'https://www.ustabuca.edu.co/'
            
            st.image(santotoprl, use_column_width=True, output_format='png')
            if st.button("Santoto page"):
                st.write("¡Hiciste clic en la imagen!")
                st.markdown(f'<a href="{urlsantoto}" target="_blank">Haz clic aquí</a>', unsafe_allow_html=True)
            
        with col2:
            
            st.image("antena.png")
        
        with col3: 
            
            unitypt = 'unity.png'
            urlunity = 'https://unity.com/es'
            
            st.image(unitypt, use_column_width=True, output_format='png')
            
            if st.button("Unity page"):
                st.write("¡Hiciste clic en la imagen!")
                st.markdown(f'<a href="{urlunity}" target="_blank">Haz clic aquí</a>', unsafe_allow_html=True)
            

         
elif pagina_seleccionada == pagina_infoproyecto:
    
    st.markdown("<h1 style='text-align: center;'>NUESTRO PROYECTO</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Conoce mas acerca de usta x-figthers</h2>", unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')
    st.write('')

   
    st.write('')
    
    col1, col2 =st.columns(2)
    with col1:
        
     from PIL import Image

     image2 = 'cover.png'

     st.image(image2, use_column_width=True)
     
    with col2: 
        
     st.markdown("<p style='text-align: justify;'>Este proyecto se centra en crear un emocionante juego de combate de 2 personas utilizando la plataforma Unity. El objetivo principal de este juego es ofrecer a los estudiantes una experiencia única y divertida en la que puedan luchar contra sus amigos y disfrutar de una experiencia de juego única.</p>", unsafe_allow_html=True)
     st.markdown("<p style='text-align: justify;'>En este juego, los personajes principales son los profesores de la universidad, cada uno con habilidades y fortalezas únicas. Los jugadores podrán elegir a su personaje favorito y luchar contra su oponente para ganar la partida.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>El juego también presenta un ambiente inspirado en la universidad, con diversos escenarios y ubicaciones que recrean el ambiente estudiantil. Los jugadores podrán disfrutar de una experiencia de juego inmersiva mientras se divierten y luchan contra sus amigos.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>En resumen, este proyecto busca crear una experiencia de juego única y divertida para los estudiantes de la universidad, utilizando los personajes de los profesores como protagonistas y ofreciendo una experiencia de juego inmersiva en la que los jugadores puedan disfrutar de una emocionante batalla entre amigos. ¡Espero que disfruten jugando nuestro juego tanto como nosotros disfrutamos creándolo!</p>", unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')
    st.write('')
   
    
    st.markdown("<h2 style='text-align: center;'>¡¡Un poco de esperanza para ti!!</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>En este adelanto, podrán ver algunas de las características clave del juego, incluyendo los personajes y la mecánica de juego emocionante. Este adelanto es solo una pequeña muestra de lo que está por venir, y estamos ansiosos por compartir el juego completo con ustedes muy pronto.</p>", unsafe_allow_html=True)
    st.write('')
   
    st.video("inicio.mp4")
    st.video("combate.mp4")
    
    
    st.markdown("<h2 style='text-align: center;'>Mas información? CLARO!!!</h2>", unsafe_allow_html=True)
    
    archivo = "info.pdf"
    
    def descargar_archivo():
        with open(archivo, "rb") as f:
            contenido = f.read()
        return contenido
    
    st.write(
        "",
        st.download_button(
            label="Mas información aquí",
            data=descargar_archivo(),
            file_name=archivo,
            ),
        "",
        text_align="center"
        )
    





    
    
elif pagina_seleccionada == pagina_personajes:
    st.markdown("<h1 style='text-align: center;'>PERSONAJES USTA X-FIGTHERS</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>!!Conoce a los mas grandes y poderosos luchadores¡¡</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>Bienvenido/a a esta sección de nuestro videojuego en la que podrás conocer en detalle la historia de cada personaje que hemos creado. Nos enorgullece presentar a nuestros jugadores una experiencia única en la que no solo podrán disfrutar de la emocionante jugabilidad, sino también adentrarse en el trasfondo y motivaciones de cada uno de los personajes que encontrarán en el juego.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>Con esta sección, estamos seguros de que los jugadores podrán sumergirse aún más en el universo que hemos creado y disfrutar de una experiencia de juego aún más enriquecedora. ¡No te pierdas la oportunidad de conocer a fondo a cada personaje del juego!</p>", unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    
    tab1, tab2, tab3, tab4 = st.tabs(["X-FIGTHERS","Ricardo","Yuli","Elvis"])
    
    with tab1:
        col1, col2, col3 = st.columns(3)
        
        with col1: 
            st.image("ricardo.png")
        with col2: 
            st.image("dis.png")
        with col3:
            st.image("elvis.png")
      
            
    with tab2:
       
       col1, col2 =st.columns(2)
       
       with col1: 
           st.image("ricardo.png")
           
       with col2:    
           st.markdown("<p style='text-align: justify;'>Desde muy joven, Ricardo se había sentido atraído por el boxeo. La disciplina, el entrenamiento arduo y el desafío constante le fascinaban. Aunque la mayoría de la gente no lo sabía, Ricardo entrenaba en un gimnasio local después de sus clases y competía en combates de boxeo en su tiempo libre.</p>", unsafe_allow_html=True)
           st.markdown("<p style='text-align: justify;'>Su pasión por el boxeo y su dedicación al deporte no pasaron desapercibidas. Pronto, Ricardo comenzó a destacarse en las competiciones amateur. Su técnica, su resistencia y su determinación eran insuperables. Su fama creció rápidamente y se convirtió en uno de los peleadores más respetados en la comunidad del boxeo.</p>", unsafe_allow_html=True)

    with tab3:
       
       col1, col2 =st.columns(2)
       
       with col1: 
           st.image("dis.png")
           
       with col2:
           st.markdown("<p style='text-align: justify;'>Desde temprana edad, Yuli había mostrado una habilidad natural para las artes marciales. Su destreza y coordinación eran asombrosas, y su pasión por el combate la llevó a entrenar diligentemente en diversas disciplinas. A lo largo de los años, perfeccionó su técnica en estilos como el kung fu, el karate, la esgrima y muchas más.</p>", unsafe_allow_html=True)
           st.markdown("<p style='text-align: justify;'>Con el tiempo, Yuli se ganó el respeto y la admiración de toda la comunidad universitaria. Su habilidad en las artes marciales era solo un aspecto de su personalidad, pero era su dedicación y pasión por enseñar lo que la convertía en una profesora excepcional.</p>", unsafe_allow_html=True)

    
    with tab4:
        
        col1, col2 =st.columns(2)
        
        with col1:
            st.image("elvis.png")
        
        with col2:
            st.markdown("<p style='text-align: justify;'>Desde muy joven, Elvis fue cautivado por el mundo de la lucha libre. Se deleitaba con las acrobacias, los movimientos espectaculares y la emoción que rodeaba a este deporte. Mientras construía su imperio en las telecomunicaciones, Elvis también entrenaba en secreto, perfeccionando su técnica y desarrollando su físico para competir en el mundo de la lucha libre profesional.</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: justify;'>A pesar de sus compromisos empresariales, Elvis siempre encontraba tiempo para asistir a eventos de lucha libre y estudiar las tácticas de los mejores luchadores. Aprovechaba cada oportunidad para aprender y mejorar, y pronto se dio cuenta de que tenía un talento innato para el deporte. Con su gran fortuna, pudo contratar a los mejores entrenadores y acceder a las mejores instalaciones para perfeccionar su técnica.</p>", unsafe_allow_html=True)

            

    st.markdown("<h1 style='text-align: center;'>¡¡Mientras te adentras en este mundo!!</h1>", unsafe_allow_html=True)
    
    audio1 = open('monster.mp3','rb')
    audiobytes = audio1.read()
    
    st.audio(audiobytes, format='audio/mp3')
    
    audio2 = open('epic.mp3', 'rb')
    audiobytes2= audio2.read()
    
    st.audio(audiobytes2, format='audio/mp3')
    
    
        
elif pagina_seleccionada == pagina_prueba:
    
    st.markdown("<h3 style='text-align: Left; color: Gray;'>Deja una reseña</h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: Left; color: Gray;'>Comentario:</h5>", unsafe_allow_html=True)
    user = st.text_input('Usuario: ', '')
    title = st.text_input('titulo: ', '')
    comment = st.text_input('Comentario: ', '')
    if st.button('Enviar reseña'):
         st.write('Gracias por su reseña')
         data = [user, title, comment ]
         worksheet.append_row(data)
    st.markdown("<h3 style='text-align: Left; color: Gray;'>Reviews</h3>", unsafe_allow_html=True)
     # Print results.
    for title, comment, rating in zip(user_values, title_values, comment_values):
         row = RowData(title, comment, rating)
         rows.append(row)
    for row in rows:
         if(row.user != "user"):
             st.divider()
             st.subheader(f"{row.user}")
             st.subheader(f"{row.title}")
             st.write(f"{row.comment}")


       
       

          
       
        
    
    
    




   
    

    
   
    

    