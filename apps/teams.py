import bs4 as bs
import urllib.request
import pandas as pd
import streamlit as st
from utility_functions import filedownload


def app():
    
    st.sidebar.header('User Input Features')
    selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2021))))
    
    def constructor_standings_by_year(year):
        '''
            Get a list of the Constructor Standings by year.
        '''
        source = urllib.request.urlopen(f'https://www.formula1.com/en/results.html/{year}/team.html').read()
        soup = bs.BeautifulSoup(source,'html.parser')
        table = soup.find_all('table')[0] 
        df = pd.read_html(str(table), flavor='bs4', header=[0])[0]
        df.drop(["Unnamed: 0","Unnamed: 4"],axis=1, inplace=True)
        df.columns = ['Position', 'Team','Points']
        df.reset_index(drop=True, inplace=True)
        return(df)
    
    df_constructor_standings_by_year = constructor_standings_by_year(selected_year)
    
    st.header('Display Points by Driver for the selected year')
    st.write('Data Dimension: ' + str(df_constructor_standings_by_year.shape[0]) + ' rows and ' + str(df_constructor_standings_by_year.shape[1]) + ' columns.')
    st.dataframe(df_constructor_standings_by_year)
    
    st.markdown(filedownload(df_constructor_standings_by_year), unsafe_allow_html=True)
    
    
    
    
    