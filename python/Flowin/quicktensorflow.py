#From "Tensorflow Tutorial for Python in 10 minutes"
#Currently using pandas and scikit-learn
#[0. IMPORT DATA]
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('c:\DCode\pyle\Flowin\Churn.csv')
print("we made it")
x = pd.get_dummies(df.drop(['Churn','Customer ID'],axis=1))
y = df['Churn'].apply(lambda x:1 if x=='Yes' else 0)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.2)

x_train.head() 
y_train.head()


#[1. IMPORT DEPENDENCIES]

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score

#[2: BUILD AND COMPILE MODEL]
model = Sequential()
model.add(Dense(units=32,activation='relu',input_dim=len(x_train.columns)))
model.add(Dense(units=64,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))
