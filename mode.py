import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pickle

model =pickle.load(open('model.pkl', 'rb'))
cat_col =pickle.load(open('data.pkl', 'rb'))

def prediction(data):
    le =LabelEncoder()
    df =pd.DataFrame(data)

    for i in data:
        if type(i)== str:
            df.iloc[data.index(i)]=le.fit_transform(df.iloc[data.index(i)])
    df= df.drop([0])        
    pred =model.predict(df.values.reshape(1,-1))  
    if pred[0] ==1:
        return'The customer left the Telecommunication Service'     
    else:
        return"The Customer Enjoys the Telecommunication Service"
    


print(prediction(['00001654a9d9f96303d9969d0a4a851714a4bb57', 'DAKAR','K > 24 month',3600.0,2.0,1020.0,340.0,2.0,257.0,90.0,46.0,7.0,1.0,2.0,'NO',17,'On-net 1000F=10MilF;10d', 1.0
 ]))

