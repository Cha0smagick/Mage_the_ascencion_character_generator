import streamlit as st
import random
import base64
from freeGPT import Client  # Asegúrate de que esta es la importación correcta
from PIL import Image
from io import BytesIO

# Definir listas de datos para la generación aleatoria
first_names = [
    "Alex", "Jordan", "Taylor", "Morgan", "Jamie", "Casey",
    "Samantha", "Derek", "Robin", "Jessie", "Chris", "Kendall",
    "Quinn", "Riley", "Taylor", "Dakota", "Hayden", "Avery",
    "Skylar", "Emerson", "Parker", "Sage", "Tatum", "Reese",
    "Cameron", "Blake", "Finley", "Rowan", "Jaden", "Hayley",
    "Taylor", "Casey", "Phoenix", "Sydney", "Sloane", "Briar",
    "Emery", "Kylie", "Aiden", "Charlie", "Sawyer", "Zoe"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
    "Morrison", "Taylor", "Murphy", "Anderson", "Parker", "Harris",
    "Martinez", "Clark", "Robinson", "Young", "Scott", "Hill",
    "Green", "Adams", "Baker", "Nelson", "Carter", "Mitchell",
    "Perez", "Hall", "Rivera", "Torres", "Sanchez", "Ramirez",
    "Jenkins", "Wood", "Gray", "Hughes", "Price", "Washington",
    "Butler", "Dixon", "Castillo", "Curtis", "Perry", "James"
]

natures = [
    "Explorer", "Protector", "Rebel", "Visionary",
    "The Caregiver", "The Leader", "The Outcast", "The Jester",
    "The Sage", "The Innocent", "The Rebel", "The Hero",
    "The Martyr", "The Survivor", "The Revolutionary", "The Scholar",
    "The Thinker", "The Artisan", "The Strategist", "The Idealist",
    "The Mystic", "The Seeker", "The Guardian", "The Anarch",
    "The Puppetmaster", "The Manipulator", "The Dilettante", "The Conformist",
    "The Realist", "The Fatalist", "The Loyalist", "The Trickster",
    "The Warrior", "The Philosopher", "The Visionary", "The Sage",
    "The Mentor", "The Visionary", "The Pacifist", "The Overachiever",
    "The Wanderer", "The Shaman", "The Protector", "The Dreamer",
    "The Outsider", "The Altruist", "The Creator", "The Sentinel",
    "The Arbitrator", "The Heroic", "The Unseen", "The Quiet"
]

demeanors = [
    "Daring", "Reserved", "Charming", "Stern",
    "Introspective", "Imposing", "Mischievous", "Sympathetic",
    "Stoic", "Charismatic", "Cunning", "Amiable",
    "Discreet", "Sardonic", "Compassionate", "Skeptical",
    "Bold", "Humorous", "Inquisitive", "Cautious",
    "Noble", "Arrogant", "Witty", "Solitary",
    "Flamboyant", "Pensive", "Protective", "Subdued",
    "Confident", "Dramatic", "Pragmatic", "Thoughtful",
    "Idealistic", "Tactful", "Defiant", "Skeptical",
    "Empathetic", "Nonchalant", "Resilient", "Subtle",
    "Passionate", "Assertive", "Dreamy", "Pragmatic",
    "Eccentric", "Innovative", "Traditional", "Anarchic"
]

essences = [
    "Dynamic", "Static",
    "Entropic", "Liminal", "Feral", "Fixed",
    "Fluid", "Mysterious", "Arcane", "Visceral",
    "Transcendent", "Temporal", "Interdimensional", "Ethereal",
    "Formless", "Formative", "Catalytic", "Refined",
    "Raw", "Spiritual", "Profound", "Esoteric",
    "Chaotic", "Cyclical", "Evolving", "Adaptive",
    "Sentient", "Sentinel", "Aetheric", "Corporal",
    "Somatic", "Resonant", "Transitory", "Abyssal",
    "Informed", "Ineffable", "Vibrant", "Dimensional",
    "Celestial", "Infernal", "Mythic", "Prosaic",
    "Mystical", "Elemental", "Philosophical", "Causal"
]

affiliations = [
    "Coven", "Coterie", "Circle", "Clan",
    "Order of Hermes", "Virtual Adepts", "Sons of Ether", "Dreamspeakers",
    "Verbena", "Akashic Brotherhood", "Cult of Ecstasy", "Hollow Ones",
    "Sahajiya", "Euthanatos", "Order of the Invisible College", "Tremere",
    "The Guardians of the Veil", "The Silver Ladder", "The Ordo Dracul", "The Akashics",
    "The Hollow Ones", "The Progenitors", "The Sons of Ether", "The Dreamspeakers",
    "The Verbena", "The Celestial Chorus", "The Order of Hermes", "The Order of the Silver Ladder",
    "The Virtual Adepts", "The Cult of Ecstasy", "The Euthanatos", "The Thyrsus",
    "The Akashic Brotherhood", "The Guardians of the Veil", "The Tremere", "The Silver Ladder",
    "The Order of the Invisible College", "The Sons of Ether", "The Progenitors", "The Hollow Ones",
    "The Seers of the Throne", "The Nephandi", "The Marauders", "The Ascended",
    "The Circle of the Crone", "The Mystics", "The Order of the Silver Ladder", "The Ebonites"
]

sects = [
    "The Camarilla", "Anarchs", "Independent", "Inconnu",
    "The Ascension", "The Technocracy", "The Traditions", "The Syndicate",
    "The Progenitors", "The Void Engineers", "The Syndicate", "The Collective",
    "The Disparate", "The Enlightened", "The Nephandi", "The Marauders",
    "The Celestial Chorus", "The Order of Hermes", "The Verbena", "The Dreamspeakers",
    "The Euthanatos", "The Akashic Brotherhood", "The Cult of Ecstasy", "The Order of the Silver Ladder",
    "The Guardians of the Veil", "The Hollow Ones", "The Sons of Ether", "The Order of the Invisible College",
    "The Technocrats", "The Innovators", "The Artisan", "The Unseen",
    "The Seekers", "The Traditionalists", "The Sentinels", "The Shadows",
    "The Practitioners", "The Occultists", "The Exiles", "The Kin",
    "The Forsaken", "The Watchers", "The Forgotten", "The Dreamers",
    "The Acolytes", "The Explorers", "The Prophets", "The Liberators"
]

concepts = [
    "The Reluctant Hero", "The Fallen Angel", "The Seeker", "The Scholar",
    "The Chosen One", "The Prodigal Son", "The Suffering Saint", "The Vengeful Spirit",
    "The Rebellious Outsider", "The Tragic Hero", "The Reluctant Leader", "The Unseen Savior",
    "The Dark Knight", "The Sorrowful Prophet", "The Unlikely Hero", "The Tormented Soul",
    "The Wayward Son", "The Forsaken Hero", "The Burdened Seeker", "The Visionary Leader",
    "The Timeless Wanderer", "The Ascetic Mystic", "The Wounded Healer", "The Mad Genius",
    "The Unconventional Thinker", "The Iconoclast", "The Keeper of Secrets", "The Altruistic Rebel",
    "The Hidden Guardian", "The Disillusioned Dreamer", "The Insurgent", "The Ethereal Wanderer",
    "The Reformed Shadow", "The Despondent Visionary", "The Fractured Reality", "The Lost Soul",
    "The Fateful Encounter", "The Unwritten Legend", "The Broken Prophecy", "The Echo of Destiny",
    "The Ascendant", "The Resilient Spirit", "The Guiding Light", "The Catalyst of Change",
    "The Ethereal Guide", "The Awakened Seer", "The Harbinger of Truth", "The Eternal Nomad"
]

# Función para generar un personaje
def generate_character():
    quirks = [
        "Has a peculiar laugh that echoes in the quiet.",
        "Collects unusual trinkets from every place visited.",
        "Always wears mismatched socks as a personal statement.",
        "Speaks in riddles to confuse and amuse others.",
        "Has an irrational fear of ducks.",
        "Is convinced they can communicate with ghosts."
    ]
    
    character = {
        "Name": f"{random.choice(first_names)} {random.choice(last_names)}",
        "Nature": random.choice(natures),
        "Demeanor": random.choice(demeanors),
        "Essence": random.choice(essences),
        "Affiliation": random.choice(affiliations),
        "Sect": random.choice(sects),
        "Concept": random.choice(concepts),
        "Description": generate_description(),
        "Background": generate_background(),
        "Attributes": {attr: random.randint(1, 5) for attr in [
            "Intelligence", "Wits", "Resolve", "Strength", "Dexterity", 
            "Stamina", "Presence", "Manipulation", "Composure"
        ]},
        "Talents": {talent: random.randint(1, 5) for talent in [
            "Alertness", "Athletics", "Brawl", "Empathy", "Expression", 
            "Intimidation", "Persuasion", "Streetwise", "Subterfuge"
        ]},
        "Skills": {skill: random.randint(1, 5) for skill in [
            "Animal Ken", "Crafts", "Drive", "Etiquette", "Firearms", 
            "Melee", "Performance", "Stealth", "Survival"
        ]},
        "Knowledges": {knowledge: random.randint(1, 5) for knowledge in [
            "Academics", "Computer", "Investigation", "Law", 
            "Linguistics", "Medicine", "Occult", "Politics", "Science"
        ]},
        "Spheres": {sphere: random.randint(1, 5) for sphere in [
            "Correspondence", "Entropy", "Forces", "Life", 
            "Matter", "Mind", "Prime", "Space", "Time"
        ]},
        "Advantages": {
            "Backgrounds": {
                "Resources": random.randint(1, 5),
                "Allies": random.randint(1, 5),
                "Contacts": random.randint(1, 5),
                "Fame": random.randint(1, 5),
                "Mentor": random.randint(1, 5),
            },
            "Willpower": random.randint(1, 5),
            "Merits": random.randint(1, 5),
            "Flaws": random.randint(1, 5),
        },
        "Health": {
            "Health Level": random.randint(1, 5),
            "Bashing": random.randint(0, 3),
            "Lethal": random.randint(0, 3),
            "Aggravated": random.randint(0, 3),
        },
        "Backgrounds": {
            "Retainer": random.randint(1, 5),
            "Safehouse": random.randint(1, 5),
            "Status": random.randint(1, 5),
        },
        "Other Traits": {
            "Quirks": random.choice(quirks),
        }
    }
    return character

# Función para generar una descripción del personaje
def generate_description():
    character_traits = [
    "They are exceptionally intelligent, often outsmarting their opponents.",
    "With a heart of a protector, they stand firm against injustice.",
    "Their rebellious nature leads them to challenge authority at every turn.",
    "A visionary at heart, they can see possibilities where others see obstacles.",
    "They can charm their way out of most situations with their charisma.",
    "Often reserved, they observe more than they speak, learning the secrets around them.",
    "Possessing a deep understanding of the Arcane, they often act as a mentor to others.",
    "They are fiercely independent, valuing personal freedom above all.",
    "Driven by curiosity, they are always eager to explore the unknown.",
    "They have a mysterious aura that draws others in, yet keeps them at a distance.",
    "Their analytical mind allows them to dissect problems and find creative solutions.",
    "Deeply empathetic, they connect with others' emotions and struggles.",
    "They have a knack for technology, often blending it with their magical abilities.",
    "As natural leaders, they inspire those around them to achieve greatness.",
    "A skeptic at heart, they question everything, even their own beliefs.",
    "They possess a strong moral compass, guiding their actions in complex situations.",
    "With a flair for the dramatic, they can turn any situation into a theatrical experience.",
    "They are relentless in their pursuit of knowledge, often at the cost of personal relationships.",
    "Their playful nature masks a deeper seriousness about their convictions.",
    "They have a gift for persuasion, often swaying others to their point of view.",
    "They approach life with a sense of wonder, finding joy in the mundane.",
    "Their past traumas have shaped them into resilient survivors.",
    "Incredibly resourceful, they can make the most out of limited resources.",
    "They carry an air of confidence that instills trust in others.",
    "Their creativity knows no bounds, often manifesting in unexpected ways.",
    "They have a keen sense of timing, knowing exactly when to act or hold back.",
    "Though they may appear aloof, they are deeply caring and protective of their loved ones.",
    "They are often plagued by self-doubt, questioning their decisions and abilities.",
    "They possess a rebellious spirit that fuels their desire for change.",
    "Their humor is sharp, often using wit to defuse tense situations.",
    "With a strong sense of justice, they often take on the role of the vigilante.",
    "They are guided by their intuition, often trusting their instincts over logic.",
    "A master of disguise, they can blend into any crowd or situation.",
    "They have a tendency to overthink, leading to analysis paralysis.",
    "Their loyalty to friends and allies is unwavering, often risking themselves for others.",
    "They are fiercely competitive, striving to be the best in their field.",
    "With an inquisitive mind, they never shy away from asking difficult questions.",
    "They often act as peacemakers, striving to resolve conflicts amicably.",
    "Their charm can be disarming, often helping them navigate social situations with ease.",
    "They are introverted yet passionate, preferring deep conversations over small talk.",
    "Possessing a strategic mind, they excel in planning and executing complex tasks.",
    "They have a unique perspective on life, often seeing the world through a different lens.",
    "Their idealism often clashes with harsh realities, leading to disillusionment.",
    "They are deeply spiritual, often exploring the metaphysical aspects of existence.",
    "They have an insatiable thirst for adventure, always seeking new experiences.",
    "Their emotional depth allows them to connect with others on a profound level.",
    "They often act impulsively, driven by passion rather than careful thought.",
    "With a fierce will, they are determined to change the world around them.",
    "They possess a natural talent for the arts, often expressing themselves creatively.",
    "Their love for learning keeps them perpetually seeking new skills and knowledge.",
    "They are natural diplomats, often able to mediate and resolve disputes.",
    "With a profound understanding of human nature, they can read others like a book.",
    "They often feel like outsiders, struggling to find their place in the world.",
    "Their commitment to their beliefs makes them a formidable adversary.",
    "They carry the weight of their responsibilities with grace and humility.",
    "Their visionary ideas often inspire those around them to dream bigger.",
    "They are intensely curious, often leading them into uncharted territory.",
    "They value honesty above all else, believing that truth is paramount."
]
    return random.choice(character_traits)

# Función para generar un background de personaje basado en sus atributos
def generate_background():
    backgrounds = [
    "A former soldier with a mysterious past.",
    "An academic who delved too deep into forbidden knowledge.",
    "A street-smart hustler with a knack for survival.",
    "A gifted artist haunted by visions.",
    "A diplomat with secrets that could alter the balance of power.",
    "An explorer seeking ancient artifacts.",
    "A former member of a secret society, now seeking redemption.",
    "An orphan raised by a powerful mage, struggling with their legacy.",
    "A gifted hacker who uncovers arcane truths hidden in the digital realm.",
    "A former cult member, now escaping the shadow of their past.",
    "An undercover agent working to expose dark magical practices.",
    "A wanderer who has traveled through various realms and dimensions.",
    "A historian specializing in lost civilizations and their magical practices.",
    "A member of a powerful family, caught in a web of political intrigue.",
    "A gifted healer with a tragic backstory, seeking to help others.",
    "A former academic expelled for controversial theories on reality.",
    "A refugee from a war-torn land seeking a new life.",
    "An enigmatic bard whose songs contain hidden truths and prophecies.",
    "A rogue time traveler with knowledge of future events.",
    "A talented chef whose dishes are imbued with magical properties.",
    "A former detective, now investigating supernatural occurrences.",
    "An environmental activist with a deep connection to nature spirits.",
    "A psychic medium, communicating with spirits to uncover secrets.",
    "A former spy who has seen too much and is now on the run.",
    "An inventor seeking to blend science and magic for new innovations.",
    "A skilled negotiator with ties to multiple factions in the magical community.",
    "A former priestess, now wielding their faith as a weapon against corruption.",
    "An exiled noble with a claim to a lost throne.",
    "A mystical cartographer mapping the hidden ley lines of the world.",
    "A conspiracy theorist who has uncovered a deeper reality.",
    "A former journalist exposing the dark side of magic.",
    "An adept martial artist with a unique connection to their inner power.",
    "A former librarian, now a guardian of ancient and forbidden texts.",
    "A gifted musician whose melodies can manipulate emotions and reality.",
    "A skilled thief with a penchant for magical artifacts.",
    "A mentor figure, guiding young mages on their path to enlightenment.",
    "A former criminal mastermind, now seeking atonement for past deeds.",
    "An anthropologist studying ancient magical practices in remote cultures.",
    "A former bodyguard for a powerful mage, now trying to carve their own path.",
    "A gifted athlete, using their physical prowess to transcend limits.",
    "A medium for a powerful spirit, navigating the complexities of the spirit world.",
    "A cult leader with a vision for a new world order based on magical principles.",
    "An archaeologist uncovering lost magical civilizations.",
    "A naturalist who communes with the spirits of the land and animals.",
    "A mentor to a group of fledgling mages, imparting wisdom and guidance.",
    "A former politician whose ambitions led them to dabble in dark magic.",
    "A gifted storyteller whose tales are woven with hidden truths.",
    "A reformed hacker who now uses their skills to protect the innocent.",
    "A former member of a powerful mage clan, seeking to break free from family ties.",
    "A magical prodigy raised in isolation, now exploring the wider world.",
    "An elemental shaman connected to the forces of nature.",
    "A fallen angel seeking redemption in a world full of darkness.",
    "A tragic hero, marked by loss yet driven by hope.",
    "A gifted designer whose creations blend art and magic seamlessly.",
    "A former employee of a megacorporation with ties to the occult.",
    "An empathetic listener, helping others heal their emotional wounds.",
    "A gifted strategist, often plotting several moves ahead in the game of power.",
    "A wanderer between worlds, collecting stories from each realm.",
    "An exiled mage from a distant land, seeking a new purpose.",
    "A magical botanist discovering plants with unique magical properties.",
    "A former member of a governing council, now advocating for change."
]
    return random.choice(backgrounds)

# Función para generar una imagen a partir del prompt
def generate_image(prompt):
    # Aquí debes llamar a la función adecuada de freeGPT para generar la imagen
    return Client.create_generation("prodia", prompt)  # Ajusta esto si es necesario

# Inicializar la aplicación
st.title("Character Creator for MAGE")

if "character_sheet" not in st.session_state:
    st.session_state.character_sheet = None

if st.button("Generate Character"):
    st.session_state.character_sheet = generate_character()

if st.session_state.character_sheet:
    character_sheet = st.session_state.character_sheet
    
    st.subheader("Character Sheet")
    st.write(character_sheet)

    # Crear un prompt para la generación de la imagen
    image_prompt = f"Create an image of {character_sheet['Name']}, a {character_sheet['Nature']} {character_sheet['Demeanor']} with the essence of {character_sheet['Essence']}. They are part of the {character_sheet['Affiliation']} and belong to the sect of {character_sheet['Sect']}. Concept: {character_sheet['Concept']}. {character_sheet['Description']}."

    # Generar la imagen usando el prompt
    if st.button("Generate Image"):
        try:
            image_response = generate_image(image_prompt)
            if image_response:  # Verifica que la respuesta tenga una imagen
                image = Image.open(BytesIO(image_response))  # Cargar la imagen desde la respuesta
                st.image(image, caption=f"Image of {character_sheet['Name']}", use_column_width=True)
            else:
                st.error("Error generating image.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

    def download_html(character_sheet):
        html = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}
                th, td {{
                    border: 1px solid #000;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                h1, h2, h3 {{
                    color: #333;
                }}
            </style>
        </head>
        <body>
            <h1>MAGE Character Sheet</h1>
            <h2>Basic Information</h2>
            <p>Name: {character_sheet["Name"]}</p>
            <p>Nature: {character_sheet["Nature"]}</p>
            <p>Demeanor: {character_sheet["Demeanor"]}</p>
            <p>Essence: {character_sheet["Essence"]}</p>
            <p>Affiliation: {character_sheet["Affiliation"]}</p>
            <p>Sect: {character_sheet["Sect"]}</p>
            <p>Concept: {character_sheet["Concept"]}</p>
            <p>Background: {character_sheet["Background"]}</p>
            <p>Description: {character_sheet["Description"]}</p>
            <h2>Attributes</h2>
            <table>
                <tr><th>Attribute</th><th>Value</th></tr>
                {''.join([f"<tr><td>{attr}</td><td>{value}</td></tr>" for attr, value in character_sheet["Attributes"].items()])}
            </table>
            <h2>Talents</h2>
            <table>
                <tr><th>Talent</th><th>Value</th></tr>
                {''.join([f"<tr><td>{talent}</td><td>{value}</td></tr>" for talent, value in character_sheet["Talents"].items()])}
            </table>
            <h2>Skills</h2>
            <table>
                <tr><th>Skill</th><th>Value</th></tr>
                {''.join([f"<tr><td>{skill}</td><td>{value}</td></tr>" for skill, value in character_sheet["Skills"].items()])}
            </table>
            <h2>Knowledges</h2>
            <table>
                <tr><th>Knowledge</th><th>Value</th></tr>
                {''.join([f"<tr><td>{knowledge}</td><td>{value}</td></tr>" for knowledge, value in character_sheet["Knowledges"].items()])}
            </table>
            <h2>Spheres</h2>
            <table>
                <tr><th>Sphere</th><th>Value</th></tr>
                {''.join([f"<tr><td>{sphere}</td><td>{value}</td></tr>" for sphere, value in character_sheet["Spheres"].items()])}
            </table>
            <h2>Advantages</h2>
            <table>
                <tr><th>Type</th><th>Value</th></tr>
                {''.join([f"<tr><td>{advantage}</td><td>{value}</td></tr>" for advantage, value in character_sheet["Advantages"].items()])}
            </table>
            <h2>Health</h2>
            <table>
                <tr><th>Health Level</th><th>Value</th></tr>
                {''.join([f"<tr><td>{health}</td><td>{value}</td></tr>" for health, value in character_sheet["Health"].items()])}
            </table>
            <h2>Backgrounds</h2>
            <table>
                <tr><th>Background</th><th>Value</th></tr>
                {''.join([f"<tr><td>{background}</td><td>{value}</td></tr>" for background, value in character_sheet["Backgrounds"].items()])}
            </table>
            <h2>Other Traits</h2>
            <p>Quirks: {character_sheet["Other Traits"]["Quirks"]}</p>
        </body>
        </html>
        """
        return html

    # Botón para descargar el HTML
    html = download_html(character_sheet)
    b64 = base64.b64encode(html.encode()).decode()
    href = f'<a href="data:text/html;base64,{b64}" download="character_sheet.html">Download Character Sheet</a>'
    st.markdown(href, unsafe_allow_html=True)
