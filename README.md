# genetic_algorithm_challenge
Data files, code, and results for Genetic Algorithm Challenge by @Sirajology on Youtube



The Challenge
=============
Use the TPOT library to make a discovery based on a question you pose. The question should be based on the Kaggle Climate Change Dataset (compiled from Berkeley Earth), but you get to choose the question. 



My Approach
============
The Climate Change Dataset on Kaggle contains several files with data for land and ocean temperatures both globally and locally. My question was: What will the monthly global average temperatures be for the next 5 years?

I chose to use the file GlobalTemperatures.csv, which contains global average land temperatures in celsius for each month from 1750-2015.

First, I cleaned the data using the script clean_data.py to produce a .csv file with features that I wanted TPOT to use and no missing data. Here, I also renamed the target variable as 'class'. The output of clean_data.py is cleaned_globaldata.csv. 

Second, I created a "fake" .csv file containing the years and months for which I wanted to make temperature predictions. This .csv file is called global_test.csv. Because the original data only runs until the year 2015, I chose to predict temperatures for 2016-2020. 

Third, I created a script that read in the file containing the cleaned temperature data (cleaned_globaldata.csv), and ran tpot to create a machine learning pipeline for predicting temperatures. This script also takes the test file of dates for which the temperature should be predicted (global_test.csv), and outputs a results file with these predictions. 
