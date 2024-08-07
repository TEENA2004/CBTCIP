#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('C://Users//teena//Downloads//Unemployment in India.xlsx')

data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')
data.set_index('Date', inplace=True)


covid_start = '2020-03-01'


pre_covid = data[data.index < covid_start]['Estimated Unemployment Rate (%)'].mean()
during_covid = data[data.index >= covid_start]['Estimated Unemployment Rate (%)'].mean()

print(f"Pre-Covid: {pre_covid:.2f}%, During Covid: {during_covid:.2f}%")


data['Estimated Unemployment Rate (%)'].plot(figsize=(10, 5), title='Unemployment Rate Over Time')
plt.axvline(pd.to_datetime(covid_start), color='r', linestyle='--', label='Covid-19 Start')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




