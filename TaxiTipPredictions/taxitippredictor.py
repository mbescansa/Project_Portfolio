import streamlit as st
from PIL import Image
import base64


st.title('NYC Taxi Tip Predictor')

st.image('/app/Predicting-Taxi-Tips-in-NYC/blob/main/resources/taxi.jpg')

st.write('Welcome to our taxi tip predictor! Please enter information about your trip.')

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

# To make run all you ask in one cell, not only the last required
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
# Format
pd.options.display.float_format = '{:,.2f}'.format

final_data = pd.read_csv('/app/Predicting-Taxi-Tips-in-NYC/blob/main/resources/app_data.csv')
final_data.drop(['fare_amount'],axis=1, inplace=True)

y = final_data['tip_amount']
X= final_data.drop(['tip_amount'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=100)
numerical_train = X_train.select_dtypes(include = np.number)

# TRAIN DATASET
numerical_train = X_train.select_dtypes(include = np.number)
# scaling standard scaler: make data normal distributed with mean=0 and std=1
transformer = StandardScaler().fit(numerical_train)
num_standardized = transformer.transform(numerical_train)
train_num_stand = pd.DataFrame(num_standardized, columns=numerical_train.columns)
# categorical
categorical_train = X_train.select_dtypes(include = np.object)
# encode categorical
encoder = OneHotEncoder().fit(categorical_train)
train_onehot = encoder.transform(categorical_train).toarray()
enc = [columname for sublist in encoder.categories_ for columname in sublist]
train_onehot = pd.DataFrame(train_onehot,columns=enc)
# final train dataset
numerical_train.reset_index(drop=True, inplace=True)
train_onehot.reset_index(drop=True, inplace=True)
X_train_preproc = pd.concat([train_num_stand,train_onehot], axis= 1)

# TEST DATASET
numerical_test = X_test.select_dtypes(include = np.number)
# scaling standard scaler: make data normal distributed with mean=0 and std=1
test_num_standardized = transformer.transform(numerical_test)
test_num_stand = pd.DataFrame(test_num_standardized, columns=numerical_test.columns)
# categorical
categorical_test = X_test.select_dtypes(include = np.object)
# encode categorical
test_onehot = encoder.transform(categorical_test).toarray()
enc = [columname for sublist in encoder.categories_ for columname in sublist]
test_onehot = pd.DataFrame(test_onehot,columns=enc)
# final test dataset
X_test_preproc = pd.concat([test_num_stand,test_onehot], axis= 1)
# X_test_preproc.head()

LR = linear_model.LinearRegression()
LR.fit(X_train_preproc,y_train)
y_pred= LR.predict(X_test_preproc)
r2 = r2_score(y_test,y_pred)
# print(y_pred[0])
# print(r2)


passenger = st.number_input("How many are you?",step=1)
distance = st.number_input("Where are you going? ",step=1)
duration = st.number_input("How long do you want to take? ",step=1)

numerical_client = pd.DataFrame({"passenger_count":passenger,
            "trip_distance" : distance,
            "trip_duration": duration,
            "trip_average_speed":35}, index=[0])

weekday = st.radio("When are you going to travel? ",('Monday', 'Tuesday', 'Wednesday','Thursday','Friday'))
day_part = st.radio("What time? ",('Morning','Midday','Afternoon','Evening','Night'))
categorical_client = pd.DataFrame({"day_part" : day_part,
            "weekday" : weekday,
            "passenger_load":"Small group"}, index=[0])
# numerical: scaling standard scaler
test_num_standardized = transformer.transform(numerical_client)
test_num_stand = pd.DataFrame(test_num_standardized, columns=numerical_client.columns)
# categorical encoding
test_onehot = encoder.transform(categorical_client).toarray()
enc = [columname for sublist in encoder.categories_ for columname in sublist]
test_onehot = pd.DataFrame(test_onehot,columns=enc)
# final test dataset
X_test_preproc = pd.concat([test_num_stand,test_onehot], axis= 1)
# X_test_preproc.head()

st.subheader('Passengers have tipped an average amount $'+ str(LR.predict(X_test_preproc)[0].round(2))+' for this trip. Don\'t forget to tip if you are happy with the service!')
