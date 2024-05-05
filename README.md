# Road Speed Analysis and Forecasting Tool

This Python program analyzes road speed data from various districts in Hong Kong using classification, visualization and machine learning techniques for modeling and prediction.

## Getting Started

Clone this repository and navigate to the root folder. This project requires Python 3 and the following packages:

- pandas
- matplotlib

You can install them using pip:

```
pip install -r requirements.txt
```

## Usage

1. Download `data.xlsx` from the data folder and place it in the root folder. 

2. Run the Python script:

```
python main.py
``` 

3. The output images will be saved to the root folder.

## Functions
The program performs the following steps:
1. Loads and preprocesses the speed and population data
2. Creates scatter plots of speed vs time for each district
3. Applies K-Means clustering to classify speeds
4. Generates a classification plot
5. Encodes categorical variables
6. Splits data for supervised learning
7. Trains a Random Forest regressor for forecasting
8. Evaluates model performance

## Output

The script produces two types of plots:

- Scatter plots of District wise speed distribution
- Bar plot of working population by district
- Scatter plot of speed classification
- MAE from Random Forest regression predictions

These allow visual comparison of speed and demographic trends across Hong Kong.


## Data

The input data is from Hong Kong government sources. 
1.	Traffic Speeds of Road Network Segments (Processed Data)
(https://data.gov.hk/en-data/dataset/hk-td-sm_4-traffic-data-strategic-major-roads)
3.	Locations of traffic detectors
(https://data.gov.hk/en-data/dataset/hk-td-sm_4-traffic-data-strategic-major-roads)
4.	2021 Population Census - Table E2021J: 2021 Population Census - District Profiles (Housing Market Areas and Building Groups) [Proportion of working population with a fixed place of work in Hong Kong who worked in the same District Council district as their residence (including those working at home)]
(https://data.gov.hk/en-data/dataset/hk-censtatd-census21c-d5212110)
5.	Territorial Population and Employment Data Matrix (2019-based Generalised Version)
(https://data.gov.hk/en-data/dataset/hk-pland-pland1-2019-based-tpedm)

