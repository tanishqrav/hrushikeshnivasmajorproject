import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn import tree
import streamlit as st
import pandas as pd

# Import necessary functions from web_functions
from web_functions import train_model
from web_functions import load_data

def app(df, X, y):
    """This function creates the visualization page"""
    
    # Remove the warnings
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Set the page title
    st.title("Visualise Heart Ailment Demographics")

    # Create a checkbox to show correlation heatmap
    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")

        fig = plt.figure(figsize=(4, 3))
        ax = sns.heatmap(df.iloc[:, 1:].corr(), annot=True)   
        bottom, top = ax.get_ylim()                             
        ax.set_ylim(bottom + 0.5, top - 0.5)                    
        st.pyplot(fig)

    if st.checkbox("Sodium Levels vs Blood Pressure"):
        sns.color_palette("rocket", as_cmap=True)
        ax = sns.scatterplot(x="Bp", y="Sod", data=df)
        st.pyplot()

    if st.checkbox("Show Confusion Matrix"):
        # Train model to get predictions
        model, score = train_model(X, y)
        predictions = model.predict(X)
        # Calculate confusion matrix
        cm = confusion_matrix(y, predictions)
        # Plot confusion matrix
        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', xticklabels=['0', '1'], yticklabels=['0', '1'])
        plt.xlabel('Predicted labels')
        plt.ylabel('True labels')
        plt.title('Confusion Matrix')
        st.pyplot()

    if st.checkbox("Show Sample Results"):
        safe = (df['Class'] == 0).sum()
        prone = (df['Class'] == 1).sum()
        data = [safe, prone]
        labels = ['Safe', 'Detected']
        colors = sns.color_palette('pastel')[0:7]
        plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
        st.pyplot()

    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(X, y)
        # Export decision tree in dot format and store in 'dot_data' variable.
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=3, out_file=None, filled=True, rounded=True,
            feature_names=X.columns, class_names=['0', '1']
        )
        # Plot the decision tree using the 'graphviz_chart' function of the 'streamlit' module.
        st.graphviz_chart(dot_data)

