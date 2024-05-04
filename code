import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the data from the Excel file
df = pd.read_excel('data.xlsx', sheet_name='road speed')

# Create a list of all districts
districts = ['Central and Western', 'Wan Chai', 'Eastern', 'Southern', 'Yau Tsim Mong', 'Sham Shui Po', 'Kowloon City', 'Wong Tai Sin', 'Kwun Tong', 'Kwai Tsing', 'Tsuen Wan', 'Tuen Mun', 'Yuen Long', 'North', 'Tai Po', 'Sha Tin', 'Sai Kung', 'Islands']

# Loop through each district and create a scatter chart
for district in districts:
    # Filter the data to only include rows where 'District' == district
    df_filtered = df[df['District'] == district]

    # Convert the time column to datetime.datetime
    df_filtered['time'] = pd.to_datetime(df_filtered['time'], format='%H:%M:%S')

    # Create the scatter chart
    plt.scatter(df_filtered['time'].dt.hour, 
    df_filtered['speed'], c=df_filtered['segment_id'], marker=Marker(color='blue', symbol='o', size=10))

    # Set the x-axis label
    plt.xlabel('time')

    # Set the y-axis label
    plt.ylabel('Speed')

    # Set the title
    plt.title(f'Road Speed Distribution in {district}')

    # Show the plot
    plt.savefig(f'Road Speed Distribution in {district}.png')

# Load the data from the Excel file 
data = pd.read_excel('data.xlsx', sheet_name='Population')

# Create a bar chart using the 'District' as x-axis and 'Working population worked in the Different District Council district as their residence' as y-axis
plt.bar(data['District'], data['Working population worked in the Different District Council district as their residence'], yerr=data['Working population worked in the Different District Council district as their residence'] - data['Working population worked in the Different District Council district as their residence'].mean())

# Set the x-axis label
plt.xlabel('District')

# Set the y-axis label
plt.ylabel('Working Population')

# Set the title of the chart
plt.title('Working Population by District')

# Rotate the index labels for the x-axis
plt.xticks(rotation=30)

# Show the plot
plt.savefig('Working Population by District.png')
