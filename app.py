import streamlit as st
from multiapp import MultiApp
from apps import drivers, teams #driver # import your app modules here

app = MultiApp()

st.title('Formula One Stats Explorer')

st.markdown("""
    This app performs simple webscraping of Formula One Data!
    * **Python libraries:** beautifulSoup, pandas, streamlit
    * **Data source:** [formula1.com](https://www.formula1.com/en/results.html).
""")

st.markdown("""
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) 
    framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). 
    Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

# Add all your application here
app.add_app("Drivers", drivers.app)
app.add_app("Teams", teams.app)
# The main app
app.run()