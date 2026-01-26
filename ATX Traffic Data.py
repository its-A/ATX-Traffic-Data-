#data was obtained from city of austin data portal
#https://data.austintexas.gov/Transportation-and-Mobility/Real-Time-Traffic-Incident-Reports/dx9v-zd7x/data_preview

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

atx_traffic = pd.read_csv('/Users/eugeniaportillo/Desktop/Python Projects/Analyze ATX Traffic Data/ATX_Traffic_Incident_Reports_20250805.csv', low_memory=False)

#returning total count of rows & columns
atx_traffic.shape #returning the numbers of rows & columns

atx_traffic.info

#previewing data > returning the first 5 rows
atx_traffic.head()

atx_traffic.dtypes #understanding data types

#extracting different classifications for issues reported
unique_categories = atx_traffic['Issue Reported'].unique()
print(unique_categories)

# Calculate counts of each issue reported
issue_counts = atx_traffic['Issue Reported'].value_counts()
print(issue_counts)

#visualize percentage of issues reported
plt.figure()
x=atx_traffic['Issue Reported'].value_counts()[0:9] #limiting the first 17 values (they have a a higher than 100 occurence count)
other_sum = sum(atx_traffic['Issue Reported'].value_counts()[10:]) #summing remaining values
x.at['Other']=other_sum #adding new key value 
labels=x.index
plt.pie(x,labels=labels, autopct='%.02f%%')
plt.title('Percentage of Issues Reported', fontsize=18)
plt.show()

# Bar chart to visualize issue counts
plt.figure(figsize=(8, 4))
plt.bar(issue_counts.index, issue_counts)
plt.title('Issue Reported Counts')
plt.xlabel('Issues')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Count')
plt.show()

#extracting & filtering from the datetime column
# Convert 'Date' column to datetime objects
atx_traffic['Published Date'] = pd.to_datetime(atx_traffic['Published Date'])

# Extract the year into a new 'Year' column
atx_traffic['Published Date'] = atx_traffic['Published Date'].dt.year

# Print data for a specific year (e.g., 2021)
atx_traffic_2025 = atx_traffic[atx_traffic['Published Date'] == 2025]
print("\nData for the year 2025 (extracted from datetime):")
print(atx_traffic_2025)

# Calculate counts of issue reported based on year
yearly_issue_counts = atx_traffic['Published Date'].value_counts()
print (yearly_issue_counts)

# Bar chart to visualize issue counts
plt.figure(figsize=(10, 5))
plt.bar(yearly_issue_counts.index, yearly_issue_counts)
plt.title('Issue Reported Per Year')
plt.xlabel('Years')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Count')
plt.show()

import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster

#plotting in a map the location of accidents
m_1 = folium.Map(location=[30.2672, -97.7431], tiles='openstreetmap', zoom_start=10)

m_1 = folium.Map(location=[30.2672, -97.7431], tiles='openstreetmap', zoom_start=10)

# Plotting Function
def plotDot(point):
    folium.CircleMarker(location=[point['Latitude'],point['Longitude']], radius=2, weight=5).add_to(m_1)

data_clean = atx_traffic.dropna()
for idx, row in data_clean.iterrows():
    folium.CircleMarker([row['Latitude'], row['Longitude']]).add_to(m_1)

m_1