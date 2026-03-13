import streamlit as st

# ------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ------------------------------------------------

st.set_page_config(
    page_title="Neurología Digital e IA",
    page_icon="🧠",
    layout="wide"
)

# ------------------------------------------------
# ESTILO CSS MINIMALISTA
# ------------------------------------------------

st.markdown("""
<style>

.main-title{
font-size:42px;
font-weight:700;
}

.motivational{
text-align:right;
font-style:italic;
color:#555;
margin-bottom:30px;
}

.card{
background-color:#ffffff;
padding:40px;
border-radius:20px;
border:1px solid #e6e6e6;
box-shadow:0px 6px 18px rgba(0,0,0,0.05);
}

.section-title{
font-size:26px;
font-weight:600;
margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

st.sidebar.title("Panel de navegación")

section = st.sidebar.radio(
    "Secciones del artículo",
    [
        "Introducción",
        "Ética en IA",
        "Diagnóstico del Alzheimer",
        "Parkinson y aprendizaje automático",
        "Neurología Digital",
        "Conclusión",
        "Referencias"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Dashboard de divulgación científica sobre Inteligencia Artificial y Neurología.")

# ------------------------------------------------
# TÍTULO
# ------------------------------------------------

st.markdown(
'<div class="main-title">El Algoritmo del Olvido y el Paso del Tiempo: Cómo la IA y la Ética Redefinen la Neurología</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="motivational">Como sociedad, el reto es asegurar que, mientras las máquinas aprenden a diagnosticarnos, nosotros no olvidemos la importancia de cuidar el contexto humano que nos rodea.</div>',
unsafe_allow_html=True
)

# ------------------------------------------------
# INTRODUCCIÓN
# ------------------------------------------------

if section == "Introducción":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
La medicina moderna se encuentra en un punto de inflexión. Imagine un escenario donde un reloj inteligente o una cámara de alta resolución puedan detectar los primeros signos de una enfermedad neurodegenerativa años antes de que aparezcan los síntomas evidentes. Esta no es una escena de ciencia ficción, sino el resultado de la convergencia entre la Inteligencia Artificial (IA) y las neurotecnologías.

Sin embargo, a medida que nuestras máquinas se vuelven más inteligentes para leer nuestro cerebro, surgen preguntas fundamentales: ¿Cómo protegemos nuestra privacidad mental? ¿Cómo garantizamos que estos algoritmos sean justos?

Este artículo explora cómo el aprendizaje automático y la ética se han unido para transformar el diagnóstico del Alzheimer y el Parkinson.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------
# ÉTICA
# ------------------------------------------------

elif section == "Ética en IA":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### Más allá de los números: Una ética con los pies en la tierra")

    st.write("""
Tradicionalmente, la ética en la tecnología se ha manejado mediante grandes principios abstractos, como "haz el bien" o "sé justo". Sin embargo, la realidad clínica es mucho más compleja.

Resseguier y Rodrigues (2021) proponen pasar de una ética teórica a una **ética como atención al contexto**, donde las decisiones tecnológicas consideran la realidad social de los pacientes.
""")

    st.markdown("#### El problema de la caja negra")

    st.write("""
Muchos modelos de aprendizaje automático funcionan como una **caja negra**: generan resultados precisos, pero es difícil entender cómo llegaron a ellos.

Esto puede generar problemas de transparencia y reproducir desigualdades si no se analizan los contextos sociales.
""")

    st.markdown("#### Neuroética e IA")

    st.write("""
Cuando se trata del cerebro humano, la ética de la IA se conecta con la **neuroética**, disciplina que analiza las implicaciones morales de intervenir en procesos mentales.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------
# ALZHEIMER
# ------------------------------------------------

elif section == "Diagnóstico del Alzheimer":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### Detectando el Alzheimer antes de que se pierdan los recuerdos")

    st.write("""
Las **redes neuronales convolucionales (CNN)** permiten analizar resonancias magnéticas para detectar patrones asociados al Alzheimer.

Investigaciones recientes han alcanzado **precisiones cercanas al 98% en el diagnóstico temprano** mediante análisis automatizado de imágenes cerebrales.
""")

    st.markdown("#### La marcha como biomarcador")

    st.write("""
Además de las imágenes cerebrales, la forma en que caminamos también puede revelar cambios neurológicos.

La variabilidad del paso o la velocidad de la marcha pueden funcionar como **biomarcadores digitales tempranos**.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------
# PARKINSON
# ------------------------------------------------

elif section == "Parkinson y aprendizaje automático":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### El Parkinson bajo la lupa de los algoritmos")

    st.write("""
El Parkinson es una enfermedad compleja cuyo diagnóstico clínico puede variar entre especialistas.

El aprendizaje automático permite analizar parámetros de movimiento para detectar patrones asociados a la enfermedad.
""")

    st.markdown("#### Cinco parámetros clave")

    st.write("""
• Velocidad media del paso  
• Longitud del paso  
• Variabilidad del paso  
• Ancho del paso  
• Variabilidad del ancho
""")

    st.markdown("#### Sensores portátiles")

    st.write("""
Los **wearables** permiten monitoreo continuo del movimiento y ayudan a detectar cuándo la medicación está funcionando correctamente.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------
# NEUROLOGÍA DIGITAL
# ------------------------------------------------

elif section == "Neurología Digital":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
La integración de IA, neuroimagen y sensores portátiles está dando lugar a una nueva disciplina: **Neurología Digital**.

Este enfoque combina:

**Lo estructural:** imágenes cerebrales analizadas por IA  
**Lo funcional:** análisis del movimiento y comportamiento motor

Esta visión permite **detección temprana y tratamientos personalizados**.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------
# CONCLUSIÓN
# ------------------------------------------------

elif section == "Conclusión":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
La inteligencia artificial tiene el potencial de transformar el diagnóstico y tratamiento de enfermedades neurodegenerativas.

Sin embargo, el verdadero éxito de estas tecnologías dependerá de su integración en sistemas de salud que prioricen **transparencia, equidad y dignidad humana**.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------
# REFERENCIAS
# ------------------------------------------------

elif section == "Referencias":

    st.header("Referencias científicas")

    referencias = [

    {
    "titulo":"Selecting Clinically Relevant Gait Characteristics for Classification of Early Parkinson’s Disease",
    "cita":"Rehman et al. (2019) Scientific Reports",
    "resumen":"Estudio que usa machine learning para seleccionar características de la marcha para clasificar Parkinson temprano con alta precisión usando cinco variables."
    },

    {
    "titulo":"A supervised machine learning approach to detect the On/Off state in Parkinson's disease",
    "cita":"Aich et al. (2020) Diagnostics",
    "resumen":"Algoritmo supervisado que detecta automáticamente los estados On y Off de medicación en pacientes con Parkinson usando sensores de movimiento."
    },

    {
    "titulo":"Neuroethics and AI ethics: a proposal for collaboration",
    "cita":"Salles & Farisco (2024) BMC Neuroscience",
    "resumen":"Propone colaboración entre neuroética y ética de IA para abordar problemas de privacidad mental, sesgos y gobernanza."
    },

    {
    "titulo":"Predictive power of gait and gait-related cognitive measures",
    "cita":"Tuena et al. (2024)",
    "resumen":"Estudio que usa machine learning para predecir progresión de deterioro cognitivo leve a Alzheimer mediante análisis de marcha."
    },

    {
    "titulo":"Machine learning models for Parkinson's disease detection",
    "cita":"Ferreira et al. (2022)",
    "resumen":"Modelos de IA que detectan Parkinson y clasifican etapas de la enfermedad usando parámetros espacio-temporales de la marcha."
    },

    {
    "titulo":"Ethics as attention to context",
    "cita":"Resseguier & Rodrigues (2021)",
    "resumen":"Propone una ética de IA basada en atención al contexto en lugar de principios abstractos."
    },

    {
    "titulo":"Early diagnosis of Alzheimer's disease from MRI images",
    "cita":"Javid & Feghhi (2021)",
    "resumen":"Modelo de deep learning para diagnóstico temprano de Alzheimer mediante resonancias magnéticas."
    },

    {
    "titulo":"Artificial Intelligence and Neuroscience: Transformative Synergies",
    "cita":"Onciul et al. (2025)",
    "resumen":"Revisión que describe la convergencia entre IA y neurociencia para diagnóstico temprano y tratamientos personalizados."
    }

    ]

    for ref in referencias:

        st.subheader(ref["titulo"])
        st.write(ref["cita"])

        if st.button(f"Mostrar resumen — {ref['titulo']}"):
            st.info(ref["resumen"])

        st.markdown("---")
