import pandas as pd
import plotly.express as px
import plotly.io as pio
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

# Create images directory
if not os.path.exists('images'):
    os.makedirs('images')

print("Loading datasets...")
# Using the datasets we downloaded
# covid.csv -> countries-aggregated.csv
# covid_grouped.csv -> time-series-19-covid-combined.csv
# coviddeath.csv -> owid-covid-data.csv

df_countries = pd.read_csv('data/covid.csv')
df_timeseries = pd.read_csv('data/covid_grouped.csv')
df_owid = pd.read_csv('data/coviddeath.csv')

print("Processing Data...")

# 1. Bar Chart: Top 15 Countries by Confirmed Cases (Latest Date)
latest_date = df_countries['Date'].max()
df_latest = df_countries[df_countries['Date'] == latest_date].sort_values(by='Confirmed', ascending=False).head(15)

fig1 = px.bar(df_latest, x='Country', y='Confirmed', 
             color='Confirmed', title=f'Top 15 Countries by Confirmed Cases ({latest_date})',
             labels={'Confirmed': 'Confirmed Cases'},
             hover_data=['Country'])
fig1.write_image("images/top_15_confirmed.png")
print("Saved: images/top_15_confirmed.png")

# 2. Bubble Chart: Confirmed vs Deaths
fig2 = px.scatter(df_latest, x='Confirmed', y='Deaths', 
                 size='Confirmed', color='Country',
                 hover_name='Country', title='Confirmed vs Deaths (Top 15 Countries)',
                 size_max=60)
fig2.write_image("images/confirmed_vs_deaths_bubble.png")
print("Saved: images/confirmed_vs_deaths_bubble.png")

# 3. Time Series: US Confirmed Cases Over Time
df_us = df_timeseries[df_timeseries['Country/Region'] == 'US']
fig3 = px.line(df_us, x='Date', y='Confirmed', 
              title='COVID-19 Confirmed Cases in US Over Time',
              labels={'Confirmed': 'Total Confirmed Cases'})
fig3.write_image("images/us_confirmed_timeseries.png")
print("Saved: images/us_confirmed_timeseries.png")

# 4. Choropleth Map: Global Confirmed Cases (Latest)
fig4 = px.choropleth(df_countries[df_countries['Date'] == latest_date], 
                    locations="Country", locationmode='country names',
                    color="Confirmed", hover_name="Country", 
                    title=f'Global COVID-19 Confirmed Cases ({latest_date})',
                    color_continuous_scale=px.colors.sequential.Plasma)
fig4.write_image("images/global_confirmed_map.png")
print("Saved: images/global_confirmed_map.png")

# 5. Word Cloud: OWID Locations (just as a demonstration of wordcloud)
print("Generating Word Cloud...")
location_text = " ".join(df_owid['location'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(location_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Locations in OWID Dataset')
plt.savefig('images/location_wordcloud.png')
print("Saved: images/location_wordcloud.png")

print("\nAnalysis Complete. All visualizations saved in the 'images' folder.")
