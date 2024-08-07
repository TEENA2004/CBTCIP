#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
df = pd.read_excel('C://Users//teena//Downloads//Iris Flower.xlsx')
print(df)
X = df.drop('Species', axis=1) 
y = df['Species']               

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



svm = SVC(kernel='linear', random_state=42)
svm.fit(X_train, y_train)

y_pred = svm.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
        
print(f'Accuracy: {accuracy:.2f}')


# In[ ]:





# In[ ]:




