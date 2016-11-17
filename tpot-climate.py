# import modules
import pandas as pd
import numpy as np
from tpot import TPOTRegressor
from sklearn.model_selection import train_test_split

# open files
test = np.genfromtxt('global_test.csv',delimiter=',',skip_header=1)
train = np.genfromtxt('cleaned_globaldata.csv',delimiter=',',skip_header=1)

# make copy of training set without class (target variable)
train_new = np.delete(train,0,1)

# get list of class variables (second column in training file)
train_class = train[:,0]

# split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(train_new, train_class, train_size=0.75, test_size=0.25)

# intiate tpot instance
tpot = TPOTRegressor(verbosity=3, generations=10, population_size=50)

# call the fit function
tpot.fit(x_train, y_train)

#call the score function on the cv data
print('TPOT score: {}'.format(tpot.score(x_test,y_test)))

# predict temps for each month for next 5 years
submission = tpot.predict(test)

# create dataframe of results for each month/year
final = pd.DataFrame({'year':test[:,0],'month':test[:,1],'landavgtemp':submission})

# export pipeline
export_filename = 'climate_pipeline.py'
tpot.export(export_filename)

# export predicted values
final_filename = 'climate_results.csv'
final.to_csv(final_filename, index=False)

# exit program
exit()

