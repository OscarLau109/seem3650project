import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.cluster import KMeans
import numpy as np

# Load the Excel file
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
                df_filtered['speed'], c=df_filtered['segment_id'])

    # Set the x-axis label
    plt.xlabel('time')

    # Set the y-axis label
    plt.ylabel('Speed')

    # Set the title
    plt.title(f'Road Speed Distribution in {district}')

    # Show the plot
    plt.savefig(f'Road Speed Distribution in {district}.png')
    plt.close()

# Load the data from the Excel file 
data = pd.read_excel('data.xlsx', sheet_name='Population')

# Create a bar chart using the 'District' as x-axis and 'Working population worked in the Different District Council district as their residence' as y-axis
plt.bar(data['District'], data['Working population worked in the Different District Council district as their residence'])

# Set the x-axis label
plt.xlabel('District')

# Set the y-axis label
plt.ylabel('Working Population')

# Set the title of the chart
plt.title('Working Population by District')

plt.xticks(rotation=30)

# Show the plot
plt.savefig('Working Population by District.png')
plt.close()



# Classification


speeds = df['speed'].values 
kmeans = KMeans(n_clusters=3, random_state=0).fit(speeds.reshape(-1,1))
labels = kmeans.labels_

df['speed_class'] = labels 

# Visualize classification
# Convert the time column to datetime.datetime
df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S')

plt.scatter(df['time'], df['speed'], c=labels)
plt.xticks(rotation=30)
plt.savefig('Speed_Classification.png')
plt.close()



# Supervised Learning 
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


# Encode district as dummy variables
district_dummies = pd.get_dummies(df['District']) 

# Concat dummy cols with original data  
df = pd.concat([df, district_dummies], axis=1)

# Drop original district col
df.drop('District', axis=1, inplace=True)

df['time'] = df['time'].astype(np.int64) / 10**9

# Now district is numeric
X = df[['time'] + list(district_dummies.columns)]
y = df['speed']

X_train, X_test, y_train, y_test = train_test_split(X, y) 

rf = RandomForestRegressor().fit(X_train, y_train)
predictions = rf.predict(X_test)

# Evaluate model
from sklearn.metrics import mean_absolute_error
print('Mean Absolute Error:', mean_absolute_error(y_test, predictions))
