# import modules
import numpy as np
import pandas as pd
from sklearn.cluster import FeatureAgglomeration
from sklearn.ensemble import GradientBoostingRegressor, VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from sklearn.preprocessing import FunctionTransformer

# read in training data
# NOTE: Make sure that the class is labeled 'class' in the data file
tpot_data = np.recfromcsv('cleaned_globaldata.csv', delimiter=',', dtype=np.float64)

# feature selection
features = np.delete(tpot_data.view(np.float64).reshape(tpot_data.size, -1), tpot_data.dtype.names.index('class'), axis=1)

# split into training and testing set
training_features, testing_features, training_classes, testing_classes = train_test_split(features, tpot_data['class'], random_state=42)

# create pipeline
exported_pipeline = make_pipeline(
     FeatureAgglomeration(affinity="cosine", linkage="average"),
     GradientBoostingRegressor(learning_rate=0.03, max_features=0.03, n_estimators=500))

# train pipeline on training features
exported_pipeline.fit(training_features, training_classes)

# run pipeline on all features to get pipeline's prediction for all months for visualization
results = exported_pipeline.predict(features)

# put results in dataframe
final = pd.DataFrame({'year':tpot_data['year'],'month':tpot_data['month'],'day':tpot_data['day'],'actual_temp':tpot_data['class'],'predicted_temp':results})
final.to_csv('original_data_predictions.csv', index=False)

# exit program
exit()
