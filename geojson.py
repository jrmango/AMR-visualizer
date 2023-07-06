import pandas as pd
import plotly.express as px
import statsmodels as sm

# Load the data that will be used to create the choropleth map
df = pd.read_csv('2019.csv')

# Create interactive map figure of EU member nations (and UK), aiming to visualize GDP and total percentage of E.coli resistances at once
fig = px.choropleth(df,
                    locations='ISOcode',
                    color='2019gdp',
                    color_continuous_scale=("viridis"),
                    hover_name='Nation',
                    title='Percentages of E. Coli resistant isolates by country versus National GDP, 2019')

# Add the scatter points to the map
fig.add_scattergeo(lat=df['Lat'],
                   lon=df['Lon'],
                   marker=dict(size=df['resperc']*3,
                               color='red',
                               line_color='black',
                               line_width=0.5))

# Output GDP map
fig.write_html("vsGDP.html")

fig2 = px.scatter(df, x='2019gdp', y='resperc', size='bov', trendline="ols",
                 title='GDP versus Percentage of Resistant E. Coli isolates, 2019')



# Output GDP scatter with trend line
fig2.write_html("GDPscatter.html")

fig3 = px.scatter(df, x='bov', y='resperc', size='2019gdp', trendline="ols",
                 title='Number of Bovine herds versus Percentage of Resistant E. Coli isolates 2019')

# Output bovine scatter with trend line
fig3.write_html("Cowscatter.html")

# Create interactive map figure of EU member nations (and UK), aiming to visualize bovine herds and total percentage of E.coli resistances at once
fig4 = px.choropleth(df,
                    locations='ISOcode',
                    color='bov',
                    color_continuous_scale=("deep"),
                    hover_name='Nation',
                    title='Percentages of E. Coli resistant isolates by country versus National Bovine Herds, 2019')

# Add points to the map, scaled by percentage of resistant isolates and located on national capitals
fig4.add_scattergeo(lat=df['Lat'],
                   lon=df['Lon'],
                   marker=dict(size=df['resperc']*3,
                               color='red',
                               line_color='black',
                               line_width=0.5))

# Output GDP map
fig4.write_html("vsCat.html")

fig5 = px.pie(df, names="Nation", values="bov")

fig5.write_html("cow_pie.html")