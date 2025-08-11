# CarDheko
By using this code, we can get able to predict the price of used car by using customized pre-learned model
# Objective:
To create an User friendly Streamlit Application which should incorporated with suitable machine learning algorithm model to predicts the price of used car.
# Version 1.0.0 Last Update: 11 August 2025
# Required Packages:
As of version 1.0.0, the program is written for python 3.7. It uses the following non-default packages:
```
•	Streamlit
•	pandas
•	sklearn
•	pickle
•	locale
•	math
•	time
•	scikit-learn
```
# Run the Project:
Then, activate the environment with “current directory address of file where it was available” followed by streamlit run CarDheko.py.
# Py Files:
```
1.	CapstoneProject3Preprocessing.ipynb -> Pre-processing code is available.
2.	CapstoneProject3ModelDevelopmentandEvaluation.ipynb  Model development and evaluation related codes are available in this file
3.	CarDheko.py -> User-Interface Streamlit code is available in this file.
```
# Program Usage:
```
•	Using the functions fillna(), pandas.to_numeric(), pandas.getdummies(data_frame,columns=[]), structured data will be pre-processed and cleaned data will be available.
•	Customized function ##“replace_outliers (data)”## is used to find the upper and lower bound using IQR technique to eliminate or replace the outliers with setting threshold. Here we need to pass the parameter single column in data_frame to find respective upper and lower bound.
•	Using the function train_test_split() to split the data into train and test data to verify whether model will learn the pattern in the data or not.
•	Using the function fit() to train the model based on imported algorithm (LinearRegression or DecissioTreeRegressor or RandomForestRegression or SupportVectorRegression)
•	Using the function Open() function to create a new file or open existing file in desired location.
•	With help of dump() to save the selected model as pickle file.
•	With help of load() to import the saved model and using it for prediction.
```
Outcome:
```
	As a result, well structured data was created.
	Structured data was pre-processed and cleaned data was created.
	Cleaned data was given to various model and respective evaluation were made.
	Based on evaluation, good model was selected and pickled.
	Using Streamlit, User-friendly application Car Dheko was developed.
	Finally, user can able to select desired car values and corresponding car price was predicted.
```

