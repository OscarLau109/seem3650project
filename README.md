# Road Speed and Population Analysis Tool

This Python script analyzes road speed and population data from Hong Kong districts to visualize trends.

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
python analysis.py
``` 

3. The output images will be saved to the `output` folder.

## Output

The script produces two types of plots:

- Scatter plots of road speed vs time for each district
- Bar plot of working population by district

These allow visual comparison of speed and demographic trends across Hong Kong.

## Data

The input data is from Hong Kong government sources. 
1.	Traffic Speeds of Road Network Segments (Processed Data)
Link: https://data.gov.hk/en-data/dataset/hk-td-sm_4-traffic-data-strategic-major-roads
3.	Locations of traffic detectors
Link: https://data.gov.hk/en-data/dataset/hk-td-sm_4-traffic-data-strategic-major-roads
4.	2021 Population Census - Table E2021J: 2021 Population Census - District Profiles (Housing Market Areas and Building Groups) [Proportion of working population with a fixed place of work in Hong Kong who worked in the same District Council district as their residence (including those working at home)]
Link: https://data.gov.hk/en-data/dataset/hk-censtatd-census21c-d5212110 
5.	Territorial Population and Employment Data Matrix (2019-based Generalised Version)
Link: https://data.gov.hk/en-data/dataset/hk-pland-pland1-2019-based-tpedm

