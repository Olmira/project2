import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title('Ceci est ma page du projet')

st.write("la voilà")

df_test = pd.read_csv('filtered_data.csv', sep=',')
#df_test

def recommendation(nom_film):
    try:
        index_film = df_test[df_test['primaryTitle']==nom_film].index[0]
        groupe = df_test.loc[index_film, 'groupe']
        df_recommendation = df_test[df_test['groupe']== groupe].drop(index_film)
        df_recommendation = df_recommendation.sort_values(by='numVotes', ascending=False).head(3)
        return df_recommendation[['primaryTitle', 'first']]
    except:
        return "Entrez le titre valide du film pour voir les recommendations"


if "input" not in st.session_state:
    st.session_state.input = ""
def input_callback():
    st.session_state.input = st.session_state.my_input
user_input = st.text_input("Entrer le primaryTitle du film: ", key="my_input",on_change=input_callback,args=None)

#st.text("your input is : " + st.session_state.my_input)
#st.text("your input is: " + st.session_state.input)
st.text(recommendation(st.session_state.my_input))