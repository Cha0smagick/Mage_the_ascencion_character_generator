import random
import streamlit as st
import pandas as pd

# Definición de las características del personaje
class Personaje:
    def __init__(self):
        self.nombre = self.generar_nombre()
        self.atributos = self.generar_atributos()
        self.habilidades = self.generar_habilidades()
        self.ventajas = self.generar_ventajas()
        self.tradicion = self.elegir_tradicion()
        self.background = self.generar_background()
        self.descripcion = self.generar_descripcion()
        self.vida = random.randint(5, 10)  # Vida inicial
        self.puntos_de_fuerza = random.randint(0, 5)
        self.puntos_de_energia = random.randint(0, 5)
        self.maldiciones = self.generar_maldiciones()
        self.clase_social = self.generar_clase_social()
        
    def generar_nombre(self):
        nombres = ["Artemis", "Eliora", "Julian", "Maeve", "Lysander", "Cassandra", "Dorian", "Thalia"]
        apellidos = ["Ravenwood", "Blackthorne", "Shadowend", "Stormwatch", "Frostbite", "Starfire"]
        return f"{random.choice(nombres)} {random.choice(apellidos)}"

    def generar_atributos(self):
        return {
            "Fuerza": random.randint(1, 5),
            "Destreza": random.randint(1, 5),
            "Constitución": random.randint(1, 5),
            "Inteligencia": random.randint(1, 5),
            "Percepción": random.randint(1, 5),
            "Carisma": random.randint(1, 5),
        }

    def generar_habilidades(self):
        habilidades_base = [
            "Artes Marciales", "Fuego", "Persuasión", "Investigación", "Sigilo", "Tecnología",
            "Ciencia", "Medicina", "Misticismo", "Conocimiento Oculto", "Ocultismo", "Música", 
            "Supervivencia", "Informática"
        ]
        habilidades_seleccionadas = random.sample(habilidades_base, 5)
        return {habilidad: random.randint(1, 5) for habilidad in habilidades_seleccionadas}

    def generar_ventajas(self):
        ventajas_base = ["Aliados", "Contatos", "Rituales", "Poderes", "Influencias"]
        return random.sample(ventajas_base, 2)

    def elegir_tradicion(self):
        tradiciones = [
            "Los Verbena", "Los Celestial", "Los Akashicos", 
            "Los Herméticos", "Los Místicos de la Huida", "Los Thig"
        ]
        return random.choice(tradiciones)

    def generar_background(self):
        entornos = [
            "una gran ciudad donde los secretos son moneda corriente",
            "una pequeña aldea aislada rodeada de mitos antiguos",
            "un barrio marginal donde la supervivencia es el pan de cada día",
            "una familia de académicos que le enseñaron a cuestionar la realidad",
            "un monasterio oculto que le enseñó a equilibrar su mente y espíritu"
        ]

        eventos = [
            "descubrió un libro antiguo que le reveló los secretos de la magia",
            "perdió a un ser querido en circunstancias misteriosas, lo que lo llevó a la magia",
            "fue testigo de un evento sobrenatural que le cambió la vida",
            "encontró un amuleto que despertó sus habilidades ocultas",
            "fue parte de un culto que buscaba poder a través de rituales oscuros"
        ]

        motivaciones = [
            "buscar venganza por una injusticia personal",
            "descubrir la verdad sobre su familia y su legado",
            "proteger a los débiles de las fuerzas oscuras que acechan",
            "comprender los secretos del universo y trascender la realidad",
            "ayudar a otros a encontrar su propio camino en la magia"
        ]

        traumas = [
            "fue testigo de la traición de alguien en quien confiaba",
            "sobrevivió a una experiencia cercana a la muerte que lo marcó para siempre",
            "fue víctima de un ritual oscuro que dejó una huella permanente en su alma",
            "creció en un ambiente hostil que lo forzó a luchar por su supervivencia",
            "perdió su hogar debido a un desastre sobrenatural"
        ]

        aspiraciones = [
            "convertirse en un maestro de la magia",
            "proteger a sus seres queridos a toda costa",
            "desenredar los misterios de su propia existencia",
            "afrontar sus miedos y superar sus debilidades",
            "descubrir un antiguo poder que cambiará el mundo"
        ]

        return (f"Creció en {random.choice(entornos)}, " 
                f"y {random.choice(eventos)}. "
                f"Motivado por {random.choice(motivaciones)}, "
                f"su trauma más profundo es que {random.choice(traumas)}, "
                f"y su mayor aspiración es {random.choice(aspiraciones)}.")

    def generar_descripcion(self):
        descripciones = [
            "Un buscador de la verdad, siempre con una pregunta en la mente.",
            "Un guerrero de las sombras, protegiendo el mundo de fuerzas oscuras.",
            "Un erudito que atesora conocimientos prohibidos y secretos antiguos.",
            "Un líder carismático, capaz de unir a las personas bajo una causa común.",
            "Un viajero del tiempo, buscando respuestas en el pasado y futuro."
        ]
        return random.choice(descripciones)

    def generar_maldiciones(self):
        maldiciones = [
            "Desconfianza permanente hacia los demás.",
            "Visiones aterradoras que interrumpen su paz.",
            "Una incapacidad para dejar el pasado atrás.",
            "Una conexión inquebrantable con el mundo espiritual.",
            "Un ciclo de mala suerte que parece perseguirle."
        ]
        return random.choice(maldiciones)

    def generar_clase_social(self):
        clases = [
            "Nobleza", "Clase Media", "Clase Baja", "Intelligentsia", "Marginado"
        ]
        return random.choice(clases)

# Generador de personaje
def generar_personaje():
    personaje = Personaje()
    return personaje

# Interfaz de usuario de Streamlit
def main():
    st.title("Generador de Personajes: Mago - La Ascensión")
    st.write("Haz clic en el botón para generar un personaje aleatorio.")

    if st.button("Generar Personaje"):
        personaje = generar_personaje()
        
        # Crear un DataFrame para mostrar los atributos en formato de cuadrícula
        data = {
            "Características": [
                "Nombre", "Tradición", "Clase Social", "Vida", "Descripción", "Puntos de Fuerza", 
                "Puntos de Energía", "Maldición"
            ],
            "Detalles": [
                personaje.nombre, personaje.tradicion, personaje.clase_social, personaje.vida, 
                personaje.descripcion, personaje.puntos_de_fuerza, personaje.puntos_de_energia,
                personaje.maldiciones
            ]
        }

        df = pd.DataFrame(data)
        
        st.subheader("Hoja de Personaje")
        st.write(df)

        # Mostrar Atributos
        st.write("### Atributos:")
        atributos_df = pd.DataFrame(personaje.atributos.items(), columns=["Atributo", "Valor"])
        st.write(atributos_df)

        # Mostrar Habilidades
        st.write("### Habilidades:")
        habilidades_df = pd.DataFrame(personaje.habilidades.items(), columns=["Habilidad", "Valor"])
        st.write(habilidades_df)

        # Mostrar Ventajas
        st.write("### Ventajas:")
        st.write(", ".join(personaje.ventajas))

        # Mostrar Background
        st.write("### Trasfondo:")
        st.write(personaje.background)

if __name__ == "__main__":
    main()
