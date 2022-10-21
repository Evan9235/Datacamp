from turtle import title
import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import altair as alt
import plotly.graph_objects as go

def media():
    with st.sidebar:
        st.write('Evan ROUILLARD')
        st.write('LinKedin:')
        st.write('https://www.linkedin.com/in/evan-rouillard-2269181ba/')
        st.write('Mail:')
        st.write('evanrouillard.efrei@gmail.com')

def import_csv():
    df = pd.read_csv('received-saved.csv')
    df2 = pd.read_csv('sent-saved.csv')
    return df, df2

def unnamed(df):
    df = df.drop('Unnamed: 0', axis= 1)
    return df

def new_col(df):
    df["Created"] = pd.to_datetime(df['Created'])
    df['Day'] = df['Created'].dt.day
    df['Day'] = pd.to_numeric(df['Day'], errors='coerce').fillna(0).astype(int)
    df['Year'] = df['Created'].dt.year
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce').fillna(0).astype(int)
    df['Hour'] = df['Created'].dt.hour
    df['Hour'] = pd.to_numeric(df['Hour'], errors='coerce').fillna(0).astype(int)
    df['Month'] = df['Created'].dt.month
    df['Month'] = pd.to_numeric(df['Month'], errors='coerce').fillna(0).astype(int)
    return df

def count_rows(rows):
    return len(rows)

def pourcentage(df):
    df.iloc[:,0].value_counts(normalize=True)*100

#graph ligne
def grapharea(df):
    by_date = df.groupby('Day').apply(count_rows)
    st.area_chart(by_date)


def graphline(df):
    by_date = df.groupby('Month',).apply(count_rows)
    st.line_chart(by_date)


#graph bar

def graphbar(df):
    by_year = df.groupby('Year').apply(count_rows)
    st.bar_chart(by_year)

def graphbar2(df):
    by_Media = df.groupby('Media Type').apply(count_rows)
    st.bar_chart(by_Media)

def bar(df):
    friends = df.groupby('From').apply(count_rows).sort_values(ascending = False)
    st.header('My 5 conversation with the most message receive')
    st.bar_chart(friends.head())
def bar2(df2):    
    friends = df2.groupby('To').apply(count_rows).sort_values(ascending = False)
    st.header('My 5 conversation with the most message send')
    st.bar_chart(friends.head())

#altair 
def altair1(df):
    c = alt.Chart(df).mark_bar().encode(
        x="Year",
        y=alt.Y('count()',title= 'Number of Message'),
        color="Media Type",
        )
    st.altair_chart(c)


def altair2(df):
    a = alt.Chart(df).mark_line().encode(
        x="Month",
        y=alt.Y('count()',title= 'Number of Message'),
        color="Year",
        )
    st.altair_chart(a)

def altair3(df):
    a = alt.Chart(df).mark_circle().encode(
        x="Hour",
        y="Day",
        color=alt.Y("count()",title='Number of message')
        )
    st.altair_chart(a)

def altair4(df):
    c = alt.Chart(df).mark_bar().encode(
        x='From',
        y=alt.Y('count()',title= 'Number of Message'),
        color="Media Type",
        )
    st.altair_chart(c)

def altair5(df):
    c = alt.Chart(df).mark_bar().encode(
        x="To",
        y=alt.Y('count()',title= 'Number of Message'),
        color="Media Type",
        )
    st.altair_chart(c)

def bouton():
    if st.button('See the graphs of the messages send'):
        pass


def seaborn1(df):
    fig = plt.figure(figsize=(20,10))
    sns.heatmap(x='Day', y='Hour', data=df)
    st.pyplot(fig)



def affichage(df,df2):

    if st.button('See the graphs of the messages received'):
        st.header('Number of messages received per day')
        grapharea(df)
        st.header('Number of messages received per month')
        graphline(df)
        st.header('Number of messages received per Year')
        graphbar(df)
        bar(df)
        bouton()
        
    else:
        st.header('Number of messages sent per day')
        grapharea(df2)
        st.header('Number of messages sent per month')
        graphline(df2)
        st.header('Number of messages sent per Year')
        graphbar(df2)
        bar2(df2)



def altair_graphe(df,df2):

    if st.button('See the graphs of the messages received'):
        st.header('Media type according to years(message received')
        altair1(df)
        st.header('Details of messages received by year')
        altair2(df) 
        st.header('The hours of the day when I receive the most messages')
        altair3(df)
        st.header('The hours of the day when I sent the most messages')
        altair4(df)
        bouton()
        
    else:
        st.header('Media type according to years(message send)')
        altair1(df2)
        st.header('Details of messages send by year')
        altair2(df2)
        st.header('The hours of the day when I sent the most messages')
        altair3(df2)
        st.header('The hours of the day when I sent the most messages')
        altair5(df2)

def main():

    media()
    df, df2=import_csv()
    df = unnamed(df)
    df2 =unnamed(df2)
    new_col(df)
    new_col(df2)
    st.title("Analyse of data snap")
    st.sidebar.title("Select type graph")
    st.sidebar.markdown("Select:")
    chart_visual = st.sidebar.selectbox('Select Charts/Plot type',('File csv','Streamlit graph', 'Other graph'))

    if chart_visual == 'File csv':
        st.write(df,df2)
    if chart_visual == 'Streamlit graph':
        affichage(df,df2)
    if chart_visual ==  'Other graph':
        altair_graphe(df,df2)

main()


