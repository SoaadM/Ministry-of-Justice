import streamlit as st
import pickle
import numpy as np


import pandas as pd

from nltk.corpus import stopwords
from textblob import TextBlob
import re

from bidi.algorithm import get_display
import arabic_reshaper
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.isri import ISRIStemmer

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge 
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score, recall_score, precision_recall_curve,f1_score, fbeta_score
from sklearn.metrics import classification_report
import pyarabic.araby as araby
import pyarabic.number as number



model=pickle.load(open('model.pkl','rb'))


arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|"!”…“–ـ'''

def remove_punctuations(text):
    translator = str.maketrans(' ', ' ', arabic_punctuations)
    return text.translate(translator)
data['judgment_text'] =data['judgment_text'].map(remove_punctuations)

def normalize_arabic(text):
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("گ", "ك", text)
    return text
data['judgment_text'] =data['judgment_text'].map(normalize_arabic)


data['judgment_text'] =data['judgment_text'].str.replace('\w*\d\w*', ' ')
data['judgment_text'] =data['judgment_text'].str.replace('\\', ' ')


data['judgment_text'] =data['judgment_text'].str.replace(r'\s', ' ')

data['judgment_text'] =data['judgment_text'].str.replace(r'\s*[A-Za-z]+\b', ' ')
data['judgment_text'] =data['judgment_text'].str.replace('-', ' ')
data['judgment_text'] =data['judgment_text'].str.replace('\u200c', ' ')

data.judgment_text = data.judgment_text.str.replace('\u0640', '')
data.judgment_text= data.judgment_text.str.replace('\u064E', '')# 
data.judgment_text= data.judgment_text.str.replace('\u0650', '')# 

 def get_Verdict(Verdict):
        
    if "حكمت"  in Verdict:
         return str.split(Verdict, "حكمت",1)[1]
    #if "حـكمـت"  in Verdict:
        # return str.split(Verdict, "حـكمـت",1)[1]
    if "قررت"  in Verdict:
         return str.split(Verdict, "قررت",1)[1]
    if "منطوق"  in Verdict:
         return str.split(Verdict, "منطوق",1)[1]
    if "منطوف"  in Verdict:
         return str.split(Verdict, "منطوف",1)[1]
    return None
data['Verdict'] =data['judgment_text'].map(get_Verdict)


st = ISRIStemmer()
def streem(f):
    return st.stem(f)
#data['Verdict'] = data['Verdict'].map(streem)
data['incident'] = data['incident'].map(streem)

stopwords = nltk.corpus.stopwords.words('arabic')
'و' in stopwords

word_st = 'الحمد','لله','تعالي','التوفيق','وصلي','الله','وسلم','علي','نبينا','محمد','اله','وصحبه','اجمعين','عضو','رئيس','الدائره','المحكمه','المحاكم','الحمد','والصلاه','والسلام','القضيه','رقم','لعام','سجل','القاضي','الموافق','المدعي','وكيل','الوكاله','المحاماه','المحاكم','بن','محكمة'

for i in range(len(word_st)):
    stopwords.append(word_st[i])
    
    
word_st2 = 'رسول','ﷲ','و','العقد','الحكم','الدعوي','للمحاكم','منطوقه','منطوق'



for i in range(len(word_st2)):
    stopwords.append(word_st2[i])
    
data['incident'] = data['incident'].apply(lambda t: " ".join(word for word in t.split() if word not in stopwords))


conditions1 = [
    (data['court'] == "التجارية"),
    (data['court'] == "العليا"),
    (data['court'] == "العامة"),
   ]
values1 = ['3','2','1']  
data['court_y'] = np.select(conditions1,values1)

y=data['court_y']
X=data['judgment_text']


from sklearn.feature_extraction.text import TfidfVectorizer
cv_tfidf = TfidfVectorizer()
X_train_tf = cv_tfidf.fit_transform(data['judgment_text'])
X_val_tf = cv_tfidf.transform(data['judgment_text'])





def predict_fareamount( judgment_text ):
    input=np.array([judgment_text]]).astype(np.float64)
    prediction=model.predict(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return str(pred) 





 st.title(" Ministry of Justice ")
    congestion_surcharge1 = st.st.write(" Enter judgment text :  ")
    
  
    if st.button("Predict"):      
        output=predict_fareamount(judgment_text)
        st.write('the  Predictis ', output)
if __name__=='__main__':
    main()
