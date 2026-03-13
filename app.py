import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------
# Configuración de la página
# -----------------------------
st.set_page_config(
    page_title="Neurología Digital e IA",
    page_icon="🧠",
    layout="wide"
)

# -----------------------------
# Estilos CSS minimalistas
# -----------------------------
st.markdown("""
<style>

.main-title{
    font-size:42px;
    font-weight:700;
}

.motivational{
    text-align:right;
    font-style:italic;
    color:#4a4a4a;
    margin-bottom:30px;
}

.card{
    background-color:#ffffff;
    padding:35px;
    border-radius:20px;
    border:1px solid #e6e6e6;
    box-shadow:0px 4px 15px rgba(0,0,0,0.05);
}

.section-title{
    font-size:24px;
    font-weight:600;
    margin-top:25px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Panel de navegación")

section = st.sidebar.selectbox(
    "Selecciona sección",
    ["Artículo", "Visualizaciones", "Referencias"]
)

variable = st.sidebar.selectbox(
    "Variable de análisis",
    ["Marcha", "Diagnóstico IA", "Biomarcadores"]
)

st.sidebar.markdown("---")
st.sidebar.write("Dashboard educativo sobre IA y neurología.")

# -----------------------------
# Título principal
# -----------------------------
st.markdown(
    '<div class="main-title">El Algoritmo del Olvido y el Paso del Tiempo</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="motivational">Como sociedad, el reto es asegurar que, mientras las máquinas aprenden a diagnosticarnos, nosotros no olvidemos la importancia de cuidar el contexto humano que nos rodea.</div>',
    unsafe_allow_html=True
)

# -----------------------------
# ARTÍCULO
# -----------------------------
if section == "Artículo":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("""
La medicina moderna se encuentra en un punto de inflexión. Imagine un escenario donde un reloj inteligente o una cámara de alta resolución puedan detectar los primeros signos de una enfermedad neurodegenerativa años antes de que aparezcan los síntomas evidentes.  

Esta no es una escena de ciencia ficción, sino el resultado de la convergencia entre la Inteligencia Artificial (IA) y las neurotecnologías.  

Sin embargo, a medida que nuestras máquinas se vuelven más inteligentes para leer nuestro cerebro, surgen preguntas fundamentales:  

- ¿Cómo protegemos nuestra privacidad mental?  
- ¿Cómo garantizamos que estos algoritmos sean justos?  

Este artículo explora cómo el aprendizaje automático y la ética se han unido para transformar el diagnóstico del Alzheimer y el Parkinson.
""")

    st.markdown('<div class="section-title">1. Más allá de los números: ética en contexto</div>', unsafe_allow_html=True)

    st.markdown("""
Tradicionalmente, la ética tecnológica se ha basado en principios abstractos como la justicia o la transparencia. Sin embargo, en el contexto clínico real estos principios necesitan aterrizarse en situaciones concretas.

Resseguier y Rodrigues proponen una **“ética como atención al contexto”**, donde las decisiones tecnológicas consideran las realidades sociales y clínicas.

Uno de los mayores desafíos es el problema de la **“caja negra”**: muchos modelos de aprendizaje automático producen resultados precisos, pero su proceso interno es difícil de interpretar.
""")

    st.markdown('<div class="section-title">2. Detectando el Alzheimer antes de perder los recuerdos</div>', unsafe_allow_html=True)

    st.markdown("""
Las **redes neuronales convolucionales (CNN)** permiten analizar imágenes médicas como resonancias magnéticas.

Investigaciones recientes han alcanzado **precisiones cercanas al 98% en el diagnóstico temprano del Alzheimer** mediante análisis automatizado de imágenes cerebrales.

Además, el cerebro también puede estudiarse indirectamente a través de la **marcha humana**. Cambios en la velocidad, longitud del paso o variabilidad del movimiento pueden actuar como biomarcadores digitales tempranos.
""")

    st.markdown('<div class="section-title">3. El Parkinson bajo la lupa de los algoritmos</div>', unsafe_allow_html=True)

    st.markdown("""
El Parkinson es una enfermedad compleja cuyo diagnóstico clínico puede variar entre especialistas.

Los algoritmos de aprendizaje automático pueden analizar **parámetros de la marcha** para identificar patrones asociados con la enfermedad.

Cinco variables clave identificadas por investigaciones recientes incluyen:

- Velocidad media del paso  
- Longitud del paso  
- Variabilidad del paso  
- Ancho del paso  
- Variabilidad del ancho

Además, los **wearables** permiten monitoreo continuo mediante sensores de movimiento, lo que ayuda a detectar cuándo la medicación está funcionando correctamente.
""")

    st.markdown('<div class="section-title">4. Hacia una neurología digital</div>', unsafe_allow_html=True)

    st.markdown("""
La integración de IA, neuroimagen y sensores portátiles está dando lugar a una nueva disciplina: la **neurología digital**.

Este enfoque combina:

**Lo estructural:** análisis de imágenes cerebrales mediante IA.  
**Lo funcional:** análisis de la marcha y el comportamiento motor.

El objetivo es lograr **detección temprana, monitoreo continuo y tratamientos personalizados**, siempre respetando la privacidad y la dignidad humana.
""")

    st.markdown('<div class="section-title">Conclusión</div>', unsafe_allow_html=True)

    st.markdown("""
La inteligencia artificial tiene el potencial de transformar la neurología clínica.

Pero el verdadero éxito no se medirá solo por la precisión de los algoritmos, sino por su capacidad de integrarse en sistemas de salud que prioricen:

- Transparencia  
- Equidad  
- Dignidad humana  

La tecnología debe complementar el juicio clínico, no reemplazar el contexto humano que define la medicina.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# VISUALIZACIONES
# -----------------------------
elif section == "Visualizaciones":

    st.header("Visualización de datos simulados")

    data = pd.DataFrame({
        "Velocidad_paso": np.random.normal(1.2,0.2,100),
        "Longitud_paso": np.random.normal(0.7,0.1,100),
        "Variabilidad": np.random.normal(0.2,0.05,100)
    })

    st.subheader("Distribución de variables de marcha")
    st.bar_chart(data)

    st.subheader("Relación entre variables")
    st.scatter_chart(data)

# -----------------------------
# REFERENCIAS
# -----------------------------
elif section == "Referencias":

    st.header("Artículos científicos utilizados")

    article_titles = [
        "Selecting clinically relevant gait characteristics for Parkinson’s disease",
        "Detecting On/Off state in Parkinson using wearable signals",
        "Neuroethics and AI ethics: a proposal for collaboration",
        "Predictive power of gait in mild cognitive impairment",
        "Machine learning models for Parkinson detection",
        "Early diagnosis of Alzheimer's from MRI with deep learning",
        "Ethics as attention to context in AI",
        "The AI inflection point in clinical neuropsychology"
    ]

    selected = st.selectbox(
        "Selecciona un artículo",
        article_titles
    )

    st.write("Artículo seleccionado:")
    st.info(selected)
