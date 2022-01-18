import pandas as pd 
import plotly.express as px

df = pd.read_csv('covid_details.csv')

fig = px.scatter(df , x='date' , y='cases' , color='country' , title='Covid Details Per Country')
fig.show()