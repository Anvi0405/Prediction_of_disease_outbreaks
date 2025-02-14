import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu  

st.set_page_config( page_title ='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon='🧑‍⚕️')

diabetes_model= pickle.load(open(r"C:\Users\Manoj Kumar\Desktop\Project Folder\Code\diabetes_model.sav", 'rb'))
heart_disease_model=pickle.load(open(r"C:\Users\Manoj Kumar\Desktop\Project Folder\Code\heart_model1.sav",'rb'))
parkinsons_model=pickle.load(open(r"C:\Users\Manoj Kumar\Desktop\Project Folder\Code\parkinson_model.sav",'rb'))
with st.sidebar:
    selected= option_menu('Prediction of Disease Outbreak System',
                          ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                          menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)



if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies= st.text_input('Number of Pregnancies')
    with col2:
        Glucose= st.text_input('Glucose Level')
    with col3:
        Bloodpressure= st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin= st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI  Value')
    with col1:
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age= st.text_input('Age of the Person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input= [float(x) for x in user_input]
        diab_prediction= diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis= 'The person is diabetic'
        else:
            diab_diagnosis= 'The person is not diabetic'
    st.success(diab_diagnosis)


if selected=='Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        Age = st.text_input('Age')
    with col2:
        Sex=st.text_input('Sex')
    with col3:
        CP=st.text_input('Chest Pain Types')
    with col1:
        Trestbps=st.text_input('Resting Blood Pressure')
    with col2:
        Chol=st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        Fbs=st.text_input('Fasting Blood Sugar >120mg/ml')
    with col1:
        Restecg=st.text_input('Resting Electrocardiographic Results')
    with col2:
        Thalach= st.text_input('Maximum Heart Rate Achieved')
    with col3:
        Exang=st.text_input('Exercise Induced Angina') 
    with col1:
        Oldpeak=st.text_input('ST Depression Induced by Exercise')      
    with col2:
        Slope=st.text_input('Slope of the Peak Exercise ST Segment')         
    with col3:
        CA=st.text_input('Major vessels colored by Flourosopy')
    
    with col1:
        Thal=st.text_input('Thal:0=normal;1=fixed defect,2 = reversable defect')
    heart_diagnosis=''
    if st.button('Heart Disease Test Result'):
       user_input=[Age,Sex,CP,Trestbps,Chol,Fbs,Restecg,Thalach,Exang,Oldpeak,Slope,CA,Thal]
       user_input=[float(x) for x in user_input]
       heart_prediction = heart_disease_model.predict([user_input])
       if heart_prediction[0]==1:
           heart_diagnosis='Person has heart disease.'
       else:
           heart_diagnosis='Person does not have heart disease.'    
    st.success(heart_diagnosis)

if selected == "Parkinsons Prediction":
    st.title("Parkinsons Disease using ML")    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        Fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        Fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        Flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')    
    with col1:
        RAP = st.text_input('MDVP:RAP')    
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DOP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')   
    with col5:       
        Shimmer_dB = st.text_input('MDVP:Shimmer_dB')  
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')      
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')  
    with col3:
        APQ = st.text_input('MDVP:APQ')  
    with col4:
        DDA = st.text_input('Shimmer:DDA')        
    with col5:
        NHR = st.text_input('NHR')   
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        Spread1 = st.text_input('Spread1')        
    with col5:
        Spread2 = st.text_input('Spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''
    if st.button("Parkinsons Test Result"):
        # Create a list of user inputs
        user_input = [
            Fo.strip(), Fhi.strip(), Flo.strip(), Jitter_percent.strip(), Jitter_Abs.strip(), 
            RAP.strip(), PPQ.strip(), DOP.strip(), Shimmer.strip(), Shimmer_dB.strip(), 
            APQ3.strip(), APQ5.strip(), APQ.strip(), DDA.strip(), NHR.strip(), 
            HNR.strip(), RPDE.strip(), DFA.strip(), Spread1.strip(), Spread2.strip(), 
            D2.strip(), PPE.strip()
        ]
        
        # Check if any input is empty
        if any(x == '' for x in user_input):
            st.error("Please fill in all fields.")
        else:
            try:
                # Convert the user input to float
                user_input = [float(x) for x in user_input]
                
                # Debugging: Print the user input
                st.write("User  Input:", user_input)
                
                # Make the prediction
                parkinsons_prediction = parkinsons_model.predict([user_input])
                
                # Debugging: Print the prediction
                st.write("Model Prediction:", parkinsons_prediction)
                
                if parkinsons_prediction[0] == 1:
                    parkinsons_diagnosis = "Person has parkinson's disease."
                else:
                    parkinsons_diagnosis = "Person does not have parkinson's disease."    
            except ValueError as e:
                st.error(f"An error occurred: {e}")
                
    st.success(parkinsons_diagnosis)