import pandas as pd 
import joblib 
import streamlit as st
import sklearn
import xgboost
import imblearn
import category_encoders
model= joblib.load('final_pipeline_Model.h5')
inputs = joblib.load('final_input.h5')




def predict(customer_age,job_type, marital, education,default,balance, housing_loan, personal_loan,
             communication_type,month, num_contacts_in_campaign, num_contacts_prev_campaign,
             prev_campaign_outcome, call_dura_in_min, day_month_binned,
             new_client_contact_this_campaign ):
    
    
    test_df = pd.DataFrame(columns=inputs)
    test_df.at[0,'customer_age']=customer_age
    test_df.at[0,'job_type']=job_type
    test_df.at[0,'marital']=marital
    test_df.at[0,'education']=education
    test_df.at[0,'default']=default
    test_df.at[0,'balance']=balance
    test_df.at[0,'housing_loan']=housing_loan
    test_df.at[0,'personal_loan']=personal_loan
    test_df.at[0,'communication_type']=communication_type
    test_df.at[0,'month']=month
    test_df.at[0,'num_contacts_in_campaign']=num_contacts_in_campaign
    test_df.at[0,'num_contacts_prev_campaign']=num_contacts_prev_campaign
    test_df.at[0,'prev_campaign_outcome']=prev_campaign_outcome
    test_df.at[0,'call_dura_in_min']=call_dura_in_min
    test_df.at[0,'day_month_binned']=day_month_binned
    test_df.at[0,'new_client_contact_this_campaign']=new_client_contact_this_campaign
    result = model.predict(test_df)[0]
    return  result






def main():
    
   
    st.title('Client Deposit Status')
    st.image("""D:\1580024684661.jpeg""")

    customer_age=st.slider('customer_age', min_value=18.0 , max_value=97.0, value= 20.0 , step=1.0)
    job_type=st.selectbox('job_type',['blue-collar', 'management','technician','admin.','services','retired','self-employed','entrepreneur','unemployed'
                                   ,'housemaid','student','unknown'])
    marital=st.selectbox('marital', ['married','single','divorced'])
    education=st.selectbox('education',['secondary','tertiary','primary','unknown'])
    default=st.selectbox('default',['no','yes'])
    balance=st.number_input('balance', min_value=None, max_value=None, value=1000, step=None)
    housing_loan=st.selectbox('housing_loan',['no','yes'])
    personal_loan=st.selectbox('personal_loan',['no','yes'])
    communication_type=st.selectbox('communication_type',['cellular','unknown','telephone'])
    month=st.selectbox('month',['may', 'jul','aug','jun','nov','apr', 'feb','jan','oct','sep','mar','dec'])
    num_contacts_in_campaign=st.number_input('num_contacts_in_campaign', min_value=1.0 , max_value=63.0, value= 5.0 , step=1.0)
    num_contacts_prev_campaign=st.number_input('num_contacts_prev_campaign', min_value=1 , max_value=15, value= 5 , step=1)
    prev_campaign_outcome=st.selectbox('prev_campaign_outcome',['failure','other','success','unknown'])
    call_dura_in_min=st.slider('call_dura_in_min', min_value=0.0 , max_value=81.0, value= 20.0 , step=1.0)
    day_month_binned=st.selectbox('day_month_binned',['<11','10:20', ' >20'])
    new_client_contact_this_campaign= st.selectbox('new_client_contact_this_campaign',[1,0])
    if st.button('predict'):
        result=  predict(customer_age,job_type, marital, education,default,balance, housing_loan, personal_loan,
             communication_type,month, num_contacts_in_campaign, num_contacts_prev_campaign,
             prev_campaign_outcome, call_dura_in_min, day_month_binned,
             new_client_contact_this_campaign )
        st.write('your Client Deposit Status is {} '.format(result))
if __name__== '__main__':
    main()
    

    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
