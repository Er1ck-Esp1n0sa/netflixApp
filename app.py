import pandas as pd
import streamlit as st
import base64

st.title('Netflix App')

DATA_URL=('dataset/movies.csv')

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('img/logo2.png')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows ,index_col=0, encoding='latin-1')
    return data

def load_data_byname(name):
    data = pd.read_csv(DATA_URL,index_col=0, encoding='latin-1')
    filtered_data_byname = data[data['name'].str.contains(name)]
    return filtered_data_byname

def load_data_bydirector(director):
    data = pd.read_csv(DATA_URL, index_col=0, encoding='latin-1')
    filtered_data_bysex = data[data[ 'director' ] == director]

    return filtered_data_bysex

st.text('Erick Juaerz Espinosa')
st.text('ZS20006728')

data_load_state = st.text('Data cargada')
data = load_data(500)
st.header("Todos los filmes")

st.sidebar.image("img/logo.png")
st.sidebar.markdown("##")

sidebar = st.sidebar
agree = sidebar.checkbox("Mostrar todos los filmes")
if agree:
  st.dataframe(data)

myname = sidebar.text_input('Titulo del filme :')
btnRange = sidebar.button('Buscar filmes')

if (myname):
    if (btnRange):
        filterbyname = load_data_byname(myname)
        count_row = filterbyname.shape[0]
        st.write(f"Buscar filmes : {count_row}")
        st.dataframe(filterbyname)

selected_director = sidebar.selectbox("Seleccionar director: ", data ['director'].unique())
btnFilterbyDirector = sidebar.button('Filtrar director')

if (btnFilterbyDirector):
    filterbyDirector = load_data_bydirector(selected_director)
    count_row = filterbyDirector.shape[0]
    st.write(f"Total items : {count_row}")
    count_row()
    st.dataframe(filterbyDirector)