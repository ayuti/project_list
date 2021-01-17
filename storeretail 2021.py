#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


import warnings
warnings.filterwarnings("ignore")


# In[2]:


data=pd.read_csv(r'D:\2021\SampleSuperstore.csv')
data.head(5)


# In[3]:


data.shape


# In[4]:


data.columns


# In[5]:


data.dtypes


# In[6]:


data.isnull().sum()


# In[7]:


data["Ship Mode"].unique()


# In[8]:


#titanic.Family_size.value_counts()
data.Country.value_counts()


# In[9]:


data.City.value_counts()


# In[10]:


data["Ship Mode"].value_counts()


# In[11]:


data["Segment"].value_counts()


# In[12]:


data["Region"].value_counts()


# In[13]:


data["Category"].value_counts()


# In[14]:


data["Sub-Category"].value_counts()


# In[ ]:





# In[15]:


duplicate_df = data[data.duplicated(keep = False)]
duplicate_df


# In[16]:


check_df=duplicate_df[(duplicate_df["Segment"]=="Corporate") & (duplicate_df["Country"]== "United States")]
check_df


# In[17]:


data_2=data.copy()


# In[18]:


data_3=data_2.drop_duplicates(keep="first")
data_3


# In[19]:


dup_check =data_3[data_3.duplicated(keep= False)]
dup_check


# In[20]:


data_3.shape


# In[21]:


data_3.describe().round(2)


# In[22]:


#why profit is neg ,why discount 0


# In[23]:


sns.distplot(data["Profit"])


# In[24]:


sns.distplot(data["Discount"])


# In[25]:


fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize=(18,4))
sns.distplot(data_3["Profit"], ax=axes[0], kde = False)
sns.boxplot(data_3["Profit"], ax=axes[1], orient = "h", showmeans = True, color = "pink")
fig.suptitle('Univariate Analysis of profit', fontsize=16)
plt.show()


# In[26]:


neg_zone=data_3[data_3["Profit"]<=0]
neg_zone


# In[27]:


zero_zone=data_3[data_3["Profit"]== 0]
zero_zone


# In[28]:


neg_perc = len(neg_zone)*100/len(data_3)    # Percentage formula
print ("% of data having negative profit: {} %".format(round(neg_perc, 3)))   # print 


# In[29]:


zero_perc = len(zero_zone)*100/len(data_3)    # Percentage formula
print ("% of data having zero profit: {} %".format(round(neg_perc, 3)))   # print 


# In[30]:


data_4=data_3[data_3["Profit"]>0]  #greater than 0 profit


# In[31]:


data_4.shape


# In[32]:


data_5=data_4[data_4["Discount"]>0] # greater than zero discount


# In[33]:


data_5.shape


# In[34]:


fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize=(18,4))
sns.distplot(data_5["Profit"], ax=axes[0], kde = False)
sns.boxplot(data_5["Profit"], ax=axes[1], orient = "h", showmeans = True, color = "pink")
fig.suptitle('Univariate Analysis of profit', fontsize=16)
plt.show()


# In[35]:


data_profit_zero=data_5[data_5["Discount"]==0]
data_profit_zero


# In[36]:


data_5.Country.value_counts()


# In[38]:


#data_5.City.value_counts()
#data_5["Ship Mode"].value_counts()
#data_5["Segment"].value_counts()
#data_5["Region"].value_counts()
#data_5["Category"].value_counts()
#data_5["Sub-Category"].value_counts()


# In[40]:


data_5.columns


# In[44]:


#x_axis = data_5.columns.tolist() #Discount List
x_axis=
for x in x_axis:
    fig, axes = plt.subplots(1, 2, figsize=(18,4))
    sns.distplot(data_5[x], ax=axes[0], kde = False)
    sns.boxplot(data_5[x], ax=axes[1], orient = "h", showmeans = True, color = "pink")
    fig.suptitle('Univariate Analysis of ' + x, fontsize=16)
data_5[['Sales','Quantity','Discount','Profit']]


# In[48]:


def scatter_regplot(x, y, in_data): 
    '''
    Returns Scatter plot with regression trend line
    '''
    
    sns.regplot(x=x, y=y, data=in_data) 
    plt.xlabel(x, fontsize = 13)
    plt.ylabel(y, fontsize = 13)
    plt.title("Scatter Plot of " + x + " & " + y, fontsize = 15)
    plt.grid()
    plt.show()


# In[49]:


scatter_data=data_5[['Sales','Quantity','Discount']]
#scatter_data.columns.tolist()
x_axis = scatter_data.columns.tolist()
y_axis = "Profit"

for col in x_axis:
    scatter_regplot(x = col, y = y_axis, in_data = data)


# In[ ]:




