# Apply Natural language processing in Saudi Arabia judicial courts
---
 # Abstract
 The courts are an essential pillar of the State. Its presence plays a major role in preserving the security and stability of it and the private and public interests of the people. Therefore, The goal of this project is to build multiple NLP models, then perform a comparison between all built models to decide which one is the best.
 # Design
 This project is one of the T5 Data Science BootCamp requirements. 
 - Data provided by from : [Saudi Ministry of Justice](https://sjp.moj.gov.sa/Filter?isFilterButtonClicked=True).
  # Data
  The data for this project will be read into a CSV file, The dataset scraped from Scientific Judicial Portal. The obtained dataset consists of over 2300 cases records with 13 features. Some of them may effect on our targets such as: the judgment text, the date of the lawsuit, and the court type... etc.
  # Algorithms
1. Data scraping

2. Download and read data

3. Quick Look at the Data Structure

4. Prepare the Data for Machine Learning Algorithms

5. Prepare the Data for Machine Learning Algorithms

6. Models: 

**Supervised learning:**

• Logistic Regression

• Gradient Boosting Classifier

• Decision Tree

**Unsupervised learning:**

• K-Means

• Text similarity

# Tools 
 **Library :** 
- Python 
- Numpy
- classification
- Pandas
- Sklearn
- Seaborn
- imblearn
- gboost
- nltk
- stop_words
- wordcloud
- arabic_reshaper 
- matplotlib

# Deployment 
- Therefore, the project will predict the type of court through it, you can file a lawsuit by entering the data of the plaintiffs, defendants, and their attorneys or lawyers, while recording the subject matter of the lawsuit, its type, the requirements of the case and its grounds, the output will be  [the competent court for this case](https://share.streamlit.io/maithaq/deployment/main/maitha.py
)

- The project will [enable searching for subject matter](https://share.streamlit.io/maithaq/deployment-ministry_justice/main/text.py
)of the lawsuit, and provides visitors all the similarities lawsuits and obtaining it, this advantage will save the time for lawyers and law student and knowing how to win the cases
 
