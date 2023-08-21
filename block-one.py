import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def category(chart_data):
    fig, ax = plt.subplots()
    pie = chart_data
    ax.pie(pie.values, labels=pie.index)
    ax.axis('equal') 

    return st.pyplot(fig)

def line(chart_data):
    return st.line_chart(chart_data)

def line_degrade():
    return st.write("Линейная")

def line_dasda():
    return st.write("Вторая")

algorithms = {
    "линейная": line_degrade,
    "фывфывфы": line_dasda
}

def run():
    uploaded_file = st.file_uploader("Загрузить CSV", type="csv")
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        first_column = st.selectbox("Выберете первую колонку", dataframe.columns)
        is_catigory_1 = st.checkbox('Категориальная', key=1)
        chart_data = dataframe[first_column]

        if is_catigory_1:
            new_data = chart_data.groupby(chart_data).count()
            category(new_data)
        else: 
            line(chart_data)
            
        second_column = st.selectbox("Выберете вторую колонку", dataframe.columns)
        is_catigory_2 = st.checkbox('Категориальная', key= 2)
        chart_data_2 = dataframe[second_column]
        if is_catigory_2:
            new_data = chart_data_2.groupby(chart_data_2).count()
            category(new_data)
        else: 
            line(chart_data_2)
        third_option = st.selectbox("Выберете алгоритм", options=algorithms.keys())
        algorithms.get(third_option)()
    
    else:
        st.error('Файл не загружен', icon="🚨")

if __name__ == "__main__":
    run()