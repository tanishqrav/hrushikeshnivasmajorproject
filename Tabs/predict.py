"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict
from web_functions import load_data

def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
               Chronic Kidney Disease Prediction.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    Bp = st.slider("Blood Pressure", int(df["Bp"].min()), int(df["Bp"].max()))
    Al = st.slider("Albumin Level", int(df["Al"].min()), int(df["Al"].max()))
    Su = st.slider("Sugar Level", float(df["Su"].min()), float(df["Su"].max()))
    Bu = st.slider("Blood Urea Level", int(df["Bu"].min()), int(df["Bu"].max()))
    Sc = st.slider("Serum Creatinine Level", int(df["Sc"].min()), int(df["Sc"].max()))
    Sod = st.slider("Sodium Level", int(df["Sod"].min()), int(df["Sod"].max()))
    Pot = st.slider("Potassium Level", float(df["Pot"].min()), float(df["Pot"].max()))
    Hemo = st.slider("Hemoglobin Level", float(df["Hemo"].min()), float(df["Hemo"].max()))
    Wbcc = st.slider("White Blood Cell Count", int(df["Wbcc"].min()), int(df["Wbcc"].max()))
    Rbcc = st.slider("Red Blood Cell Count", int(df["Rbcc"].min()), int(df["Rbcc"].max()))

    
    # Create a list to store all the features
    features = [Bp,Al,Su,Bu,Sc,Sod,Pot,Hemo,Wbcc,Rbcc]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score,predicton1,score1,prediction2,score2 = predict(X, y, features)
        score = score 
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to get Chronic Kidney Disease!!")
            st.image("images/diseasedetected.png")
            st.title('Healthy Habits to follow')
            st.write('1.Exercise') 
            st.write('2.Eat Right')
            st.write('3.Drink Enough Water')
            st.write('4.Meditate')
            st.write('5.Go Visit a Doctor Regularly')
            st.write('6.Maintain a Healthy Body Weight')      
            st.write('7.Get A Good Night’s Sleep')
            st.write('8.Don’t Drink Alcohol')
            st.snow()
        else:
            st.success("The person is relatively safe from Chronic Kidney  Diseases")
            st.image("images/nodiseasedetected.png")
            st.balloons()

        # Print teh score of the model 
        st.text_area("Accuracy using Decision Tree Classifier: ",value=f'This model has an accuracy of {score*100}',height=100)
        st.text_area("Accuracy using Random Forest Classifier: ",value=f'This model has an accuracy of {score1*100}',height=100)
        st.text_area("Accuracy using Support Vector Machine Classifier: ",value=f'This model has an accuracy of {score2*100}',height=100)
        
