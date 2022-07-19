#!/usr/bin/env python
# coding: utf-8

# # Predict Wind Turbine Energy Output

# ### Data Importation

# In[1]:


import numpy as np
import matplotlib.pyplot as mango
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd 
import seaborn as sb

data = pd.read_csv('/Users/macbookpro/Desktop/Wind Turbine Dataset.csv')


# ### Data Exploration

# In[4]:


data.head()


# In[5]:


data.dtypes


# In[2]:


data['Date/Time'] = pd.to_datetime(data['Date/Time'])


# In[3]:


data.dtypes


# In[8]:


data.columns


# In[10]:


data.shape


# In[13]:


data.describe


# ### Data Cleaning

# In[15]:


data.isnull().sum()


# In[16]:


data.duplicated()


# In[17]:


data.duplicated('LV ActivePower (kW)')


# In[3]:


data['Date/Time'] = pd.to_datetime(data['Date/Time'])


# In[30]:


data.dtypes


# #### MISSING DATA POINTS
#      ** 2018-01-26 06:20:00  -  2018-01-30 14:40:00 **
#      ** 2018-09-28 21:20:00  -  2018-10-02 16:30:00 **
#      ** 2018-11-10 21:10:00  -  2018-11-14 12:00:00 ** 
#         

# ### Data Visualization

# In[61]:


sb.pairplot(data=data)


# #### LV Active Power vs Wind Direction

# In[11]:


sb.set_style('whitegrid')
sb.relplot(x = 'Wind Direction (°)', y = 'LV ActivePower (kW)', data=data, color='g')


# #### LV Active Power vs Wind Speed

# In[34]:


sb.set_style('whitegrid')
sb.relplot(x = 'Wind Speed (m/s)', y = 'LV ActivePower (kW)', data=data, color='orange')


# #### LV Active Power vs Theoretical Power 

# In[13]:


sb.set_style('whitegrid')
sb.relplot(x = 'Theoretical_Power_Curve (KWh)', y = 'LV ActivePower (kW)', data=data, color='red')


# #### Date/Time vs Wind Speed

# In[65]:


sb.set_style('whitegrid')
sb.relplot(x = 'Wind Speed (m/s)', y = 'Date/Time', data=data, color=bened)


# In[58]:


bened = sb.color_palette()[6]


# #### Date/Time vs Wind Direction

# In[9]:


sb.set_style('whitegrid')
greg=sb.color_palette()[5]
sb.relplot(x='Wind Direction (°)', y='Date/Time', data=data, color=greg)


# ### Modelling

# In[53]:


X = data[['Wind Speed (m/s)', 'Theoretical_Power_Curve (KWh)', 'Wind Direction (°)']]
Y = data['LV ActivePower (kW)']


# In[54]:


print(X)


# In[55]:


print(Y)


# In[23]:


from sklearn.model_selection import train_test_split


# In[59]:


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.23)


# In[60]:


len(X_train)


# In[32]:


len(X_test)


# In[61]:


X_train


# ## Build Linear Regression Model

# In[32]:


from sklearn.linear_model import LinearRegression


# In[34]:


model = LinearRegression()


# In[63]:


model.fit(X_train, Y_train)


# In[64]:


model.predict(X_test)


# In[65]:


Y_test


# ## Accuracy - Linear Regression Model

# In[66]:


model.score(X_test, Y_test)


# ### First Prediction - Linear Regression

# In[68]:


user_1 = model.predict([[25, 315.3738, 263.511425]])


# In[69]:


print(user_1)


# ### Second Prediction - Linear Regression

# In[71]:


user_2 = model.predict([[70, 603.343, 67.263934]])


# In[72]:


print(user_2)


# ## Build Random Forest Regressor Model

# In[7]:


X = data[['Wind Speed (m/s)', 'Theoretical_Power_Curve (KWh)', 'Wind Direction (°)']]
Y = data['LV ActivePower (kW)']


# In[8]:


from sklearn.model_selection import train_test_split


# In[18]:


X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.23)


# In[19]:


X_train


# In[20]:


from sklearn.ensemble import RandomForestRegressor


# In[21]:


model_reg = RandomForestRegressor()


# In[22]:


model_reg.fit(X_train, Y_train)


# In[23]:


model_reg.predict(X_test)


# In[24]:


Y_test


# ## Accuracy - Random Forest Regressor

# In[26]:


model_reg.score(X_test, Y_test)


# ### First Prediction - Random Forest 

# In[27]:


user_a = model_reg.predict([[45, 359.343, 271.263934]])


# In[28]:


user_a 

