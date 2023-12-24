import pandas as pd
import joblib

grad_pipeline = joblib.load('./models/finished_model.joblib')
encoder= joblib.load('./models/encoder.joblib')
column = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
       'MonthlyCharges', 'TotalCharges'] 
df = pd.DataFrame(columns=column)
df[0]=['Female','Yes','Yes','No',1,'Yes','No','Fiber optic','No','No','No','No','No','No','month to month','Yes','Electronic check',69.55,69.55]
prediction = grad_pipeline .predict(df)
threshold = 0.11
y_pred_proba =grad_pipeline.predict_proba(df)[:,1]
binary_prediction =(y_pred_proba > threshold)
print(binary_prediction)

