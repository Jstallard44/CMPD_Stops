import streamlit as st
import altair as alt

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = load_data('data/Officer_Traffic_Stops.csv')

boxplot = alt.Chart(stops).mark_boxplot().encode(x="Was_a_Search_Conducted:O", 
y="Driver_Age:Q")

st.altair_chart(boxplot)

