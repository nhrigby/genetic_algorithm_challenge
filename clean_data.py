# import modules
import pandas as pd
import numpy as np

# load main dataset
globaldata = pd.read_csv('GlobalTemperatures.csv')

# convert date to pandas date time
globaldata.dt = pd.to_datetime(globaldata.dt)

# create new columns for date information
globaldata['year'] = globaldata['dt'].dt.year
globaldata['month'] = globaldata['dt'].dt.month
globaldata['day'] = globaldata['dt'].dt.day

# drop original datetime column
globaldata = globaldata.drop('dt',1)

# take rows with no missing LandAverageTemperature, target variable
globaldata = globaldata[np.isfinite(globaldata['LandAverageTemperature'])]

# fill in missing data
globaldata = globaldata.fillna(-9999)

# drop unnecessary columns
globaldata = globaldata.drop('LandMaxTemperature',1)
globaldata = globaldata.drop('LandMaxTemperatureUncertainty',1)
globaldata = globaldata.drop('LandMinTemperature',1)
globaldata = globaldata.drop('LandMinTemperatureUncertainty',1)
globaldata = globaldata.drop('LandAverageTemperatureUncertainty',1)
globaldata = globaldata.drop('LandAndOceanAverageTemperature',1)
globaldata = globaldata.drop('LandAndOceanAverageTemperatureUncertainty',1)

# rename target variable as class
globaldata.rename(columns={'LandAverageTemperature': 'class'}, inplace=True)

# write processed data to file
globaldata.to_csv('cleaned_globaldata.csv',index=False)

# exit program
exit()