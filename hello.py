# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:03:28 2023

@author: jfern
"""
import streamlit as st
import pandas as pd
import numpy as np
import sqlite3




# Definimos las páginas de nuestra aplicación
pagina_inicio = "Inicio"
pagina_infoproyecto = "Nuestro proyecto"
pagina_personajes= "Personajes"


# Creamos un selectbox en la barra lateral para seleccionar la página
pagina_seleccionada = st.sidebar.selectbox(
    "Selecciona una página",
    [pagina_inicio, pagina_infoproyecto, pagina_personajes]
)


st.experimental_set_query_params(pagina=pagina_seleccionada)

# Mostramos el contenido de la página seleccionada
if pagina_seleccionada == pagina_inicio:
    
 
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
            if st.button("Satoto page"):
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
           st.markdown("<p style='text-align: justify;'>El performance puede ser visto como una forma de arte que busca transformar la relación entre el artista y el público, y desafiar la noción tradicional del arte como objeto. Como tal, el performance ha sido utilizado por artistas para abordar temas sociales, políticos y culturales, y para desafiar las normas sociales y estéticas.</p>", unsafe_allow_html=True)
           
    with tab3:
       
       col1, col2 =st.columns(2)
       
       with col1: 
           st.image("dis.png")
           
       with col2:
           st.markdown("<p style='text-align: justify;'>El performance puede ser visto como una forma de arte que busca transformar la relación entre el artista y el público, y desafiar la noción tradicional del arte como objeto. Como tal, el performance ha sido utilizado por artistas para abordar temas sociales, políticos y culturales, y para desafiar las normas sociales y estéticas.</p>", unsafe_allow_html=True)
    
    with tab4:
        
        col1, col2 =st.columns(2)
        
        with col1:
            st.image("elvis.png")
        
        with col2:
            st.markdown("<p style='text-align: justify;'>El performance puede ser visto como una forma de arte que busca transformar la relación entre el artista y el público, y desafiar la noción tradicional del arte como objeto. Como tal, el performance ha sido utilizado por artistas para abordar temas sociales, políticos y culturales, y para desafiar las normas sociales y estéticas.</p>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>¡¡Mientras te adentras en este mundo!!</h1>", unsafe_allow_html=True)
    
    audio1 = open('monster.mp3','rb')
    audiobytes = audio1.read()
    
    st.audio(audiobytes, format='audio/mp3')
    
    audio2 = open('epic.mp3', 'rb')
    audiobytes2= audio2.read()
    
    st.audio(audiobytes2, format='audio/mp3')
    
    conn = sqlite3.connect('comentarios.db')
    c= conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS comentarios
              (id INTEGER PRIMARY KEY AUTOINCREMENT, comentario TEXT)''')
    
    conn.commit()
    
    def agregar_comentario(comentario):
        c.execute("INSERT INTO Ccomentarios (comentario) VALUES (?)", (comentario))
        conn.commit()
        
    def obtener_comentarios():
        c.execute("SELECT * FROM comentarios")
        comentarios = c.fetchall()
        return comentarios
    
    def main():
        st.title("¡DEJANOS TU COMENTARIO AQUI!")
        
        comentarios = obtener_comentarios()
        
        if comentarios:
            st.header("Conoce lo que dice nuestra comunidad:")
            
            for comentario in comentarios:
                st.write(comentario[1])
        else:
            st.write("No hay comentarios aún.")
            
        st.header("Agregar nuevo comentario")
        nuevo_comentario = st.text_input("Escribe tu comentario aquí")
        if st.button("Enviar"):
            if nuevo_comentario:
                agregar_comentario(nuevo_comentario)
                st.success("¡¡Gracias por tu aporte!!")
            else:
                st.warnig("Queremos conocer tu opinión.")
                
    if __name__ == '__main__':
        main()
    
     
    
    


       
       

          
       
        
    
    
    
    
    st.markdown("<p style='text-align: justify;'></p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'></p>", unsafe_allow_html=True)



   
    

    
   
    

    