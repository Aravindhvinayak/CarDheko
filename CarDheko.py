import streamlit as st
import pandas as pd
import math
import pickle
import locale
import time

df = pd.read_excel(r"D:\Aravindh\Guvi\Guvi Project\Project 3\Data Set\wholedataframe cleaned model.xlsx")
df1 = df
df1 = df1.drop(['Variant name'],axis=1)

def own_reg_model(df1,user_input_data):
    with open(r"D:\Aravindh\Guvi\Guvi Project\Project 3\Project 3 Live evaluation\reg_model.pkl","rb") as file:
        load_model = pickle.load(file)

    if len(df1.columns) == len(user_input_data):
        df1.loc[len(df1)] = user_input_data
    else:
        temp = len(df1.columns) - len(user_input_data)
        temp = len(df1.columns) - temp
        for i in range(temp,len(df1.columns)):
            user_input_data.append(None)
        df1.loc[len(df1)] = user_input_data

    clm_list = df1.columns
    for i in clm_list:
        df1[i]=df1[i].fillna(df1[i].mode()[0])

    df1=pd.get_dummies(df1,columns=['Fuel type', 'Body type','Transmission type', 'Manufacturer','Car model',
                                'Insurance Type','Drive Type', 'City'],dtype='int')

    xtem = df1.drop(df1.index[0:len(df1)-1],axis=0)
    xtem = xtem.drop(['Price of the used car'],axis=1)
    own_prediction = load_model.predict(xtem)
    own_prediction = math.floor(own_prediction[0])
    return(own_prediction)


st.title('_WELCOME_:sparkles:')
st.header('Car Dekho - Used Car Price Prediction :red_car:',divider=True)
st.subheader('Select the following options to predict the price of required car :moneybag:',divider='orange')

user_input = []
with st.sidebar:
    st.image(r"D:\Aravindh\Guvi\Guvi Project\Project 3\Data Set\Car Image.JPEG",channels='RGB',use_container_width=True)
    st.success("This is a price prediction application that is used to predict the price of a used car based on user selection.",icon='💬')
    st.info("Project 3 : **Car Dheko**  \n Batch : **MA28**  \n Student Name : **Aravindh D**",icon="🧑‍💻")
with st.container():
    with st.expander(label='Car Data 📋',expanded=True):
        car_city = st.selectbox('City 🌇',df['City'].sort_values().unique(),label_visibility='visible')
        user_input.append(car_city)
        col1,col2,col3 = st.columns(3)
        with col1:
            car_manufacturer = st.selectbox('Car Manufacturer 🏭',df['Manufacturer'].sort_values().unique(),label_visibility='visible')
            user_input.append(car_manufacturer)
        model_df = df.loc[df['Manufacturer']==car_manufacturer]

        with col2:
            car_model = st.selectbox('Car model 🚘🚗🚕',model_df['Car model'].sort_values().unique(),label_visibility="visible")
            user_input.append(car_model)
        with col3:
            body_df = model_df.loc[model_df['Car model']==car_model]   
            body_type = st.radio('Car Body Type 🔮',body_df['Body type'].sort_values().unique(),label_visibility="visible")
            user_input.append(body_type)
        
        with col1:
            variant_df = body_df.loc[body_df['Body type']==body_type]
            variant_type = st.selectbox('Car Variant Type 🔍',variant_df['Variant name'].sort_values().unique(),
                                        label_visibility="visible")
            central_variant_df = variant_df.loc[variant_df['Variant name']==variant_type]
            central_variant = central_variant_df['Central variant ID'].unique()
            user_input.append(int(central_variant[0]))

        with col2:
            transmission_df = variant_df.loc[variant_df['Variant name']==variant_type]
            transmission_type = st.radio('Transmission Type 📟',transmission_df['Transmission type'].sort_values().unique(),label_visibility="visible")
            user_input.append(transmission_type)

        with col3:
            fuel_df = transmission_df.loc[transmission_df['Transmission type']==transmission_type]
            fuel_type = st.radio('Fuel Type ⛽',fuel_df['Fuel type'].sort_values().unique(),label_visibility="visible")
            user_input.append(fuel_type)

        kilometers = st.select_slider('Kilometers Driven 📈',range(0,200000),label_visibility="visible")
        user_input.append(kilometers)

        previous_owner = st.pills('No of Previous Owners 💂‍♂️',df['Previous owners'].unique(),label_visibility="visible")
        user_input.append(previous_owner)

        insurance_type = st.segmented_control('Insurance Type 📜',df['Insurance Type'].unique(),label_visibility='visible')
        user_input.append(insurance_type)

    #st.write(user_input)

    btn1 = st.button('Predict 🎰',help="Click on Predict button to get the predicted car price")

    if btn1:
        for i in range(len(user_input)):
            if not user_input[i]:
                if i==8:
                    st.error('Please select the No of previous owner and click on Predict button',icon="⚠️")
                    break
                elif i == 9:
                    st.error('Please select the Insurance Type and click on Predict button',icon="⚠️")
                    break
            elif i==len(user_input)-1:
                prediction = own_reg_model(df1,user_input)
                if prediction:
                    locale.setlocale(locale.LC_MONETARY,"en_IN")
                    amount_in_rupees = locale.currency(prediction,grouping=True)
                    with st.status("⏳Consolidating the data...", expanded=True) as status:
                        st.write("⏳Analyzing the data...")
                        time.sleep(2)
                        st.write("⏳Predicting price...")
                        time.sleep(1)
                        st.write("⏳Fetching the pridicted price...")
                        time.sleep(1)
                        status.update(
                            label="Predicted!", state="complete", expanded=False
                        )
                    st.success(f"The predicted price is {amount_in_rupees}",icon="💫")
                    break
                else:
                    st.error(" Error Occured! Please Try Again",icon="⚠️")


    