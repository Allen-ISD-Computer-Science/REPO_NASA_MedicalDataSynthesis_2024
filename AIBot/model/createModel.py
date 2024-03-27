import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    classification_report,
)
from joblib import dump, load

#Reads datasheet and outputs some info
df = pd.read_csv('GenDiseaseMultiSymp.csv')
df.head()

df.info()

#Converts String-Data-Column into serveral Boolean-Data-Columns for every unique string
pre_df = pd.get_dummies(df,columns=['Symptom_1', 'Symptom_2', 'Symptom_3', 'Symptom_4', 'Symptom_5', 'Symptom_6', 'Symptom_7','Symptom_8','Symptom_9','Symptom_10','Symptom_11','Symptom_12','Symptom_13','Symptom_14','Symptom_15','Symptom_16','Symptom_17'],drop_first=True)
pre_df.head()
print(pre_df)
#saved Boolean created dataset to CSV
pre_df.to_csv("booleanGenDiseaseMultiSymp.csv")

#Assigns X values to all symptoms (drops Disease column)
#Assigns Y values to possible diseases
X = pre_df.drop('Disease', axis=1)
y = pre_df['Disease']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=125
)

#Loads model framework and trains
model = GaussianNB()

model.fit(X_train, y_train)

#Predicts and scores itself
y_pred = model.predict(X_test)

accuray = accuracy_score(y_pred, y_test)
f1 = f1_score(y_pred, y_test, average="weighted")

print("Accuracy:", accuray)
print("F1 Score:", f1)

#Saves model for later use
dump(model, 'GenDiseaseMultiSymp.joblib') 