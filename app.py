import streamlit as st

# ---------------------------
# Configuración de página
# ---------------------------
st.set_page_config(
    page_title="Neurología Digital e IA",
    page_icon="🧠",
    layout="wide"
)

# ---------------------------
# Estilos CSS
# ---------------------------
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

# ---------------------------
# SIDEBAR
# ---------------------------

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
st.sidebar.info("Dashboard de divulgación científica sobre IA y neurología.")

# ---------------------------
# TÍTULO
# ---------------------------

st.markdown(
'<div class="main-title">El Algoritmo del Olvido y el Paso del Tiempo: Cómo la IA y la Ética Redefinen la Neurología</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="motivational">Como sociedad, el reto es asegurar que, mientras las máquinas aprenden a diagnosticarnos, nosotros no olvidemos la importancia de cuidar el contexto humano que nos rodea.</div>',
unsafe_allow_html=True
)

# ---------------------------
# INTRODUCCIÓN
# ---------------------------

if section == "Introducción":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
La medicina moderna se encuentra en un punto de inflexión. Imagine un escenario donde un reloj inteligente o una cámara de alta resolución puedan detectar los primeros signos de una enfermedad neurodegenerativa años antes de que aparezcan los síntomas evidentes. Esta no es una escena de ciencia ficción, sino el resultado de la convergencia entre la Inteligencia Artificial (IA) y las neurotecnologías.

Sin embargo, a medida que nuestras máquinas se vuelven más inteligentes para leer nuestro cerebro, surgen preguntas fundamentales: ¿Cómo protegemos nuestra privacidad mental? ¿Cómo garantizamos que estos algoritmos sean justos?

Este artículo explora cómo el aprendizaje automático y la ética se han unido para transformar el diagnóstico del Alzheimer y el Parkinson, basándose en una sólida estructura de investigación científica.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# ÉTICA
# ---------------------------

elif section == "Ética en IA":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### Más allá de los números: Una ética 'con los pies en la tierra'")

    st.write("""
Tradicionalmente, la ética en la tecnología se ha manejado mediante grandes principios abstractos, como "haz el bien" o "sé justo". No obstante, la realidad de los hospitales y los pacientes es mucho más compleja.

Por ello, expertos como Resseguier y Rodrigues (2021) proponen un cambio de visión: pasar de una ética teórica a una "ética como atención al contexto".
""")

    st.markdown("#### El problema de la 'Caja Negra'")

    st.write("""
El motor de este avance es el Aprendizaje Automático (machine learning), un sistema que permite a las computadoras aprender patrones a partir de datos masivos.

El reto es que muchas veces estos sistemas funcionan como una **"caja negra"**: sabemos qué resultado arrojan, pero no exactamente cómo llegaron a él.

Si no prestamos atención al contexto social, corremos el riesgo de que los algoritmos hereden prejuicios o ignoren las desigualdades de la vida real.
""")

    st.markdown("#### Neuroética e IA: Una alianza necesaria")

    st.write("""
Cuando hablamos de enfermedades del cerebro, la ética de los datos se mezcla con la **neuroética**, que estudia las implicaciones de intervenir en la mente humana.

Dado que estas tecnologías tocan fibras sensibles como nuestra identidad y autonomía, diversos autores sostienen que la colaboración entre expertos en ética de IA y neurocientíficos es vital.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# ALZHEIMER
# ---------------------------

elif section == "Diagnóstico del Alzheimer":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### Detectando el Alzheimer antes de que se pierdan los recuerdos")

    st.write("""
La enfermedad de Alzheimer es la causa más común de demencia en el mundo. Detectarla a tiempo es como intentar encontrar una aguja en un pajar de datos clínicos.

Aquí es donde entran las **Redes Neuronales Convolucionales (CNN)**.
""")

    st.markdown("#### Los ojos digitales de la medicina")

    st.write("""
Las CNN son un tipo de diseño de IA inspirado en la visión humana, ideal para analizar imágenes médicas.

Cuando se aplican a las resonancias magnéticas, los resultados son sorprendentes. Investigaciones han logrado niveles de precisión cercanos al **98.67% en el diagnóstico temprano**.
""")

    st.markdown("#### La marcha como espejo del cerebro")

    st.write("""
El cerebro no solo se observa en imágenes; también se refleja en la manera en que nos movemos.

La forma de caminar —la marcha— puede convertirse en un **biomarcador digital temprano**, revelando alteraciones neurológicas antes de que los síntomas sean evidentes.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# PARKINSON
# ---------------------------

elif section == "Parkinson y aprendizaje automático":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### El Parkinson bajo la lupa de los algoritmos")

    st.write("""
El Parkinson es una enfermedad compleja y a menudo subjetiva; lo que un médico ve como un temblor leve, otro podría interpretarlo de forma distinta.

El aprendizaje automático permite una **medición objetiva** basada en datos.
""")

    st.markdown("#### Los cinco pilares del movimiento")

    st.write("""
Investigaciones han identificado cinco parámetros clave para una detección temprana:

• Velocidad media del paso  
• Longitud del paso  
• Variabilidad de la longitud  
• Ancho del paso  
• Variabilidad del ancho
""")

    st.markdown("#### Tecnología para llevar puesta (Wearables)")

    st.write("""
Los sensores portátiles permiten monitoreo continuo del movimiento.  
Esto facilita detectar cuándo la medicación está funcionando correctamente y cuándo deja de hacerlo.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# NEUROLOGÍA DIGITAL
# ---------------------------

elif section == "Neurología Digital":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
La integración de IA, neuroimagen y sensores portátiles está dando lugar a una nueva disciplina: **Neurología Digital**.

Este enfoque combina:

**Lo estructural:** imágenes cerebrales analizadas por IA.  
**Lo funcional:** análisis de la marcha y comportamiento motor.

Esta visión holística permite una **detección temprana más precisa** y tratamientos personalizados.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# CONCLUSIÓN
# ---------------------------

elif section == "Conclusión":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
La inteligencia artificial tiene el potencial de devolvernos tiempo y calidad de vida frente a enfermedades neurodegenerativas.

Sin embargo, el verdadero éxito de estas tecnologías no se medirá solo por su precisión, sino por su capacidad para integrarse en sistemas de salud que prioricen la **transparencia, la equidad y la dignidad humana**.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# REFERENCIAS
# ---------------------------

elif section == "Referencias":

    st.header("Artículos científicos")

  elif section == "Referencias":

    st.header("Referencias científicas")

    referencias = [

    elif section == "Referencias":

    st.header("Referencias científicas")

    referencias = [

    {
    "titulo":"Selecting Clinically Relevant Gait Characteristics for Classification of Early Parkinson’s Disease",
    "cita":"Rehman, R. Z. U., Del Din, S., Guan, Y., Yarnall, A. J., Shi, J. Q., & Rochester, L. (2019). Scientific Reports.",
    "resumen":"Estudio que usa machine learning para seleccionar las características de la marcha más relevantes para clasificar Parkinson temprano con alta precisión usando solo cinco variables."
    },

    {
    "titulo":"A supervised machine learning approach to detect the On/Off state in Parkinson's disease",
    "cita":"Aich, S., et al. (2020). Diagnostics.",
    "resumen":"Propone un algoritmo de machine learning supervisado que detecta automáticamente los estados On y Off en pacientes con Parkinson utilizando sensores de movimiento."
    },

    {
    "titulo":"Neuroethics and AI ethics: a proposal for collaboration",
    "cita":"Salles, A., & Farisco, M. (2024). BMC Neuroscience.",
    "resumen":"Argumenta que la convergencia entre IA y neurociencia requiere una colaboración estrecha entre ética de IA y neuroética para abordar cuestiones de privacidad, autonomía y sesgos."
    },

    {
    "titulo":"Predictive power of gait and gait-related cognitive measures",
    "cita":"Tuena, C., et al. (2024). Frontiers in Human Neuroscience.",
    "resumen":"Estudio que usa machine learning para evaluar cómo alteraciones en la marcha y pruebas cognitivas pueden predecir la progresión de deterioro cognitivo leve a Alzheimer."
    },

    {
    "titulo":"Machine learning models for Parkinson's disease detection",
    "cita":"Ferreira, M. I. A. S. N., et al. (2022). Gait & Posture.",
    "resumen":"Modelos de machine learning capaces de detectar Parkinson y clasificar estadios de la enfermedad utilizando parámetros espacio-temporales de la marcha."
    },

    {
    "titulo":"On the Contribution of Neuroethics to the Ethics and Regulation of Artificial Intelligence",
    "cita":"Farisco, M., Salles, A., & Evers, K. (2022). Neuroethics.",
    "resumen":"Propone que la neuroética contribuya con análisis conceptual profundo para mejorar las guías éticas actuales de IA."
    },

    {
    "titulo":"The AI inflection point in clinical neuropsychology",
    "cita":"Serafimovska A., Challinor K., Florio T. (2025). Journal of Clinical and Experimental Neuropsychology.",
    "resumen":"Describe un punto de inflexión en la neuropsicología clínica debido al avance de la IA en evaluación cognitiva y diagnóstico temprano."
    },

    {
    "titulo":"Ethics as attention to context",
    "cita":"Resseguier, A., & Rodrigues, R. (2021). Open Research Europe.",
    "resumen":"Critica las guías éticas abstractas de IA y propone un enfoque basado en atención al contexto para aplicaciones reales."
    },

    {
    "titulo":"Early diagnosis of Alzheimer's disease from MRI images",
    "cita":"Javid, S. A., & Feghhi, M. M. (2021). IEEE Access.",
    "resumen":"Modelo de deep learning basado en redes convolucionales para diagnóstico temprano de Alzheimer mediante resonancias magnéticas."
    },

    {
    "titulo":"Ethical considerations for integrating multimodal computer perception and neurotechnology",
    "cita":"Hurley, M., et al. (2024). Frontiers in Human Neuroscience.",
    "resumen":"Explora preocupaciones éticas sobre la integración de IA de percepción computacional con neurotecnologías."
    },

    {
    "titulo":"Neurociberética",
    "cita":"Ramos, R. (2024). Gaceta Médica de México.",
    "resumen":"Propone la neurociberética como nuevo enfoque para abordar riesgos éticos derivados de la convergencia entre neurociencia, IA y cibernética."
    },

    {
    "titulo":"Philosophical foundation of the right to mental integrity",
    "cita":"Lavazza, A., & Giorgi, R. (2023). Neuroethics.",
    "resumen":"Fundamenta filosóficamente el derecho a la integridad mental frente a tecnologías que pueden leer o modificar actividad cerebral."
    },

    {
    "titulo":"Addressing neuroethics issues in practice",
    "cita":"Berger, S. E., & Rossi, F. (2022). Neuron.",
    "resumen":"Analiza lecciones aprendidas por empresas tecnológicas al implementar ética en IA aplicada a neurotecnologías."
    },

    {
    "titulo":"Legal Governance of Brain Data Derived from Artificial Intelligence",
    "cita":"Ahluwalia, M. (2021). Voices in Bioethics.",
    "resumen":"Examina riesgos de privacidad asociados al big brain data generado por IA y propone gobernanza legal."
    },

    {
    "titulo":"Neuropsychological tests and machine learning",
    "cita":"Cazzolli, C., et al. (2025). Aging Clinical and Experimental Research.",
    "resumen":"Estudio que usa Random Forest para identificar pruebas neuropsicológicas predictoras de deterioro cognitivo y demencia."
    },

    {
    "titulo":"Artificial Intelligence and Neuroscience: Transformative Synergies",
    "cita":"Onciul, R., et al. (2025). Journal of Clinical Medicine.",
    "resumen":"Revisión que explora la convergencia entre IA y neurociencia para diagnóstico temprano y tratamiento personalizado."
    },

    {
    "titulo":"Ethical Implications of AI in Neuroscience",
    "cita":"Merlin, M., et al. (2024). International Research Journal on Advanced Engineering and Management.",
    "resumen":"Discute los desafíos éticos del uso de IA en investigación de enfermedades cerebrales."
    },

    {
    "titulo":"Minding Rights: Mapping Ethical and Legal Foundations of Neurorights",
    "cita":"Ligthart, S., et al. (2023). Cambridge Quarterly of Healthcare Ethics.",
    "resumen":"Mapea las bases éticas y legales de los neurorights para proteger privacidad mental, libertad cognitiva e integridad mental."
    },

    {
    "titulo":"Decoding the Brain, Respecting the Person",
    "cita":"Botes, M., et al. (2025). Neuroethics.",
    "resumen":"Explora modelos de consentimiento relacional para proteger libertad cognitiva y privacidad mental."
    },

    {
    "titulo":"A human rights-based approach for governing neurotechnologies",
    "cita":"McCulloch, W. S., & Pitts, W. (2022). Cambridge Handbook of Responsible AI.",
    "resumen":"Propone gobernar las neurotecnologías basadas en IA mediante un marco de derechos humanos."
    }

    ]

    for ref in referencias:

        st.subheader(ref["titulo"])

        st.write(ref["cita"])

        if st.button(f"Mostrar resumen: {ref['titulo']}"):
            st.info(ref["resumen"])

        st.markdown("---")

        st.markdown("---")
