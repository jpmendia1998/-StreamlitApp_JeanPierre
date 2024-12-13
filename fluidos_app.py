import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Insert an icon
icon = Image.open("resource/gota.png")

# State the design of the app
st.set_page_config(page_title="DrillFluids Pro", page_icon=icon)

# Insert css codes to improve the design of the app
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;
      margin: 15px auto;
}
footer {
  display: none;
}
</style>""",
    unsafe_allow_html=True,
)

# Insert title for app
st.title("DrillFluids Pro")

st.write("---")

# Add information of the app
st.markdown(
    """
    DrillFluid Pro es una herramienta web diseñada para optimizar el análisis, diseño y monitoreo de fluidos de perforación en operaciones de perforación de pozos.
     Su propósito es proporcionar cálculos rápidos, simulaciones precisas y reportes detallados que permitan a los ingenieros tomar decisiones informadas en tiempo real,
      mejorando la eficiencia operativa y reduciendo riesgos en campo."""


)

# Add additional information
expander = st.expander("Information")
expander.write(
    "This is an open-source web app fully programmed in Python"
)

# Insert subheader
st.subheader("**Qué son los fluidos de perforación?**")
# Insert Image
image = Image.open("resource/1.png")
st.image(image, width=100, use_container_width=True)

# Insert subheader
st.subheader("**Tpos de fluidos de perforación**")
# Insert Image
image = Image.open("resource/2.jpg")
st.image(image, width=100, use_container_width=True)

# Insert subheader
st.subheader("**Funciones del lodo de perforación**")

# Insert video
video = open("resource/fluidos.mp4", "rb")
st.video(video)


# Sidebar section
logo = Image.open("resource/logo.jpg")
st.sidebar.image(logo)

# Add title to the sidebar section
st.sidebar.title("Home")

# Upload files
file = st.sidebar.file_uploader("Carga tu archivo csv")

# Add sections of the app
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Propiedades y Clasificación","simulacion", "Impacto Ambiental"],
        icons=["bar-chart","display-fill", "tree"],
    )