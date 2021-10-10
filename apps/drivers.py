import bs4 as bs
import urllib.request
import pandas as pd
import streamlit as st
from utility_functions import filedownload


def app():
    
    st.sidebar.header('User Input Features')
    selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2021))))
    
    def driver_points_by_year(year):
        '''
            Get a list of the drivers, position at the end of the year, nationality, career and points.
        '''
        source = urllib.request.urlopen(f'https://www.formula1.com/en/results.html/{year}/drivers.html').read()
        soup = bs.BeautifulSoup(source,'html.parser')
        table = soup.find_all('table')[0] 
        df = pd.read_html(str(table), flavor='bs4', header=[0])[0]
        df.drop(["Unnamed: 0","Unnamed: 6"],axis=1, inplace=True)
        df.columns = ['Position', 'Driver', 'Nationality', 'Car', 'Points']
        df.reset_index(drop=True, inplace=True)
        return(df)
    
    df_driver_points_by_year = driver_points_by_year(selected_year)
    
    st.header('Display Points by Driver for the selected year')
    st.write('Data Dimension: ' + str(df_driver_points_by_year.shape[0]) + ' rows and ' + str(df_driver_points_by_year.shape[1]) + ' columns.')
    st.dataframe(df_driver_points_by_year)
    
    st.markdown(filedownload(df_driver_points_by_year), unsafe_allow_html=True)
    
    def fastest_lap_by_year(year):
        '''
            Get a list of the fastest laps for each Grand Prix.
        '''
        source = urllib.request.urlopen(f'https://www.formula1.com/en/results.html/{year}/fastest-laps.html').read()
        soup = bs.BeautifulSoup(source,'html.parser')
        table = soup.find_all('table')[0] 
        df = pd.read_html(str(table), flavor='bs4', header=[0])[0]
        df.drop(["Unnamed: 0","Unnamed: 5"],axis=1, inplace=True)
        df.columns = ['Grand Prix', 'Driver', 'Car', 'Time']
        df.reset_index(drop=True, inplace=True)
        return(df)
    
    df_fastest_lap_by_year = fastest_lap_by_year(selected_year)
    
    st.header('Display Fastest Laps for the selected year')
    st.write('Data Dimension: ' + str(df_fastest_lap_by_year.shape[0]) + ' rows and ' + str(df_fastest_lap_by_year.shape[1]) + ' columns.')
    st.dataframe(df_fastest_lap_by_year)
    
    st.markdown(filedownload(df_fastest_lap_by_year), unsafe_allow_html=True)

    


    
    
    
    
    
    