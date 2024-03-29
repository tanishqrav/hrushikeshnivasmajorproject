
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import streamlit as st


@st.cache_data()
def load_data():
    """This function returns the preprocessed data"""

    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('kidney.csv')

    # Rename the column names in the DataFrame.
    
    # Perform feature and target split
    X = df[["Bp","Al","Su","Bu","Sc","Sod","Pot","Hemo","Wbcc","Rbcc"]]
    y = df['Class']

    return df, X, y

@st.cache_data()
def train_model(X, y):
    """This function trains the model and return the model and model score"""
    # Create the model
    model = DecisionTreeClassifier(
            ccp_alpha=0.0, class_weight=None, criterion='entropy',
            max_depth=4, max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_samples_leaf=1, 
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            random_state=42, splitter='best'
        )
    model1=RandomForestClassifier(n_estimators=100,random_state=42)
    model2=SVC(kernel='linear',random_state=42)
    # Fit the data on model
    model.fit(X, y)
    model1.fit(X,y)
    model2.fit(X,y)
    # Get the model score
    score = model.score(X, y)
    score1=model.score(X,y)
    score2=model.score(X,y)

    # Return the values
    return model, score,model1,score1,model2,score2

def predict(X, y, features):
    # Get model and model score
    model, score,model1,score1,model2,score2 = train_model(X, y)
    # Predict the value
    prediction = model.predict(np.array(features).reshape(1, -1))

    return prediction, score
