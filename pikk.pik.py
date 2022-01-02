import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
warnings.filterwarnings("ignore")

data = pd.read_csv('final_data', index_col=0)
       
y=data['court_y']
X=data['judgment_text']

data_x = np.array(x)
data_y = np.array(y)
# print(X,y)
X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.3, random_state=0)
lin_reg = GradientBoostingClassifier()
lin_reg.fit(X_train, y_train)


est = make_pipeline(GradientBoostingClassifier())
est.fit(X_train, y_train)

pickle.dump(est,open('model.pkl','wb'))