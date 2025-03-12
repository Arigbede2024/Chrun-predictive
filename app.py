import streamlit as st
from mode import *


def main():

    st.title("Expresso Telecommunication Churn Prediction")

    user_id = st.selectbox('Insert Your ID', (cat_col["user_id"]))
    region = st.selectbox("Insert Your Region",(cat_col["REGION"]))
    tenure = st.selectbox("Insert Your Subscription",(cat_col["TENURE"]))
    montant= st.number_input("Insert Your Montant",value=None)
    frequent_rech= st.number_input("Insert The Frequency of your recharge",value=None)
    revenue =st.number_input("insert the revenue", value=None)
    arpu_segment =st.number_input("insert the segment",value=None)
    frequency = st.number_input("insert the data Number",value=None)
    data_vol =st.number_input("insert the data volume of your recharge", value= None)
    on_net =st.number_input("insert the on_net value", value=None)
    orange = st.number_input('insert the orange', value=None)
    tigo = st.number_input("Insert The Tigo", value=None)
    zone1= st.number_input("Insert The zone 1", value=None)
    zone2 = st.number_input("Insert The zone 2", value=None)
    mrg =st.text_input("inser No")
    regularity = st.number_input("Insert The regularity", value=None)
    top_pack = st.selectbox("Insert your subscription pack", (cat_col['TOP_PACK']))
    freq_top_pack =st.number_input("insert the frequency pack number", value= None)

    CHURN = ""

    if st.button("predict"):
       
       
        CHURN = prediction([user_id, region,tenure,montant,frequent_rech, revenue,arpu_segment,frequency, data_vol,on_net,orange,tigo, zone1, zone2, mrg, regularity, top_pack,freq_top_pack])

    st.success(CHURN)
if __name__ =="__main__" :
        main()   