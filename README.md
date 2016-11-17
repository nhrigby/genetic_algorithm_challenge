# genetic_algorithm_challenge
Data files, code, and results for Genetic Algorithm Challenge by @Sirajology on Youtube



The Challenge
=============
Use the TPOT library to make a discovery based on a question you pose. The question should be based on the Kaggle Climate Change Dataset (compiled from Berkeley Earth), but you get to choose the question. 



My Approach
============
The Climate Change Dataset on Kaggle contains several data files for land and ocean temperatures both globally and locally. I chose to address the following question:

**What will the monthly global average temperatures be for the next 5 years?**

I chose to use the file, GlobalTemperatures.csv, which contains global average land temperatures in celsius for months from 1750-2015. Here is my process:

1. I cleaned the data using the script clean_data.py to produce a .csv file with features that I wanted TPOT to use and no missing data. The main feature I was interested in was the date (dt, in the original data file). I split the date column in to year, month and day. Here, I also renamed the target variable (LandAverageTemperature) as 'class'. The output of clean_data.py is cleaned_globaldata.csv.

2. I created a "fake" .csv file containing the years and months for which I wanted to make temperature predictions. This .csv file is called global_test.csv. The original data only runs until the year 2015, so in order to predict temperatures for the next 5 years, my test file contains dates for 2016-2020. 

3. I wrote a script that read in the cleaned temperature data (cleaned_globaldata.csv), and applied the TPOT library to create a machine learning pipeline for predicting temperatures. This script also takes the test file of dates for which the temperature should be predicted (global_test.csv), and outputs a results file with these predictions. 
