#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from scipy import stats
import numpy as np


# # Descriptive analytics

# In[7]:


df=pd.read_csv('Week_8_Q&A_dataset - Sheet1.csv')
print(df)


# In[8]:


df.head()


# In[9]:


df['Gender'].value_counts()


# In[10]:


df.describe()


# In[12]:


df.isna().sum()


# In[13]:


df.groupby(['Gender']).mean()


# In[14]:


df.groupby(['Test preparation']).mean()


# # Check whether female and male students scored the same marks.
# 

# Null hypothesis H0: male marks < female marks
# 
# Alternate Hypothesis H1: male marks > female marks

# In[15]:


boys_mark=df[df['Gender']=='male']
boys_mark['Total Marks']


# In[16]:


female_mark=df.loc[(df['Gender']=='female')]
female_mark['Total Marks']


# In[17]:


t_stat,p_value=stats.ttest_ind(boys_mark['Total Marks'],female_mark['Total Marks'],alternative='less')


# In[18]:


print('T Statistics value is: ',t_stat, 'P value is: ',p_value)


# T Statistics value is:  -0.6940885268848668 P value is:  0.24689111589803814
# Let us assume that alpha value is 0.05, our p value is 0.246 which is greater than alpha value. So, we reject null hypothesis.
# 
# Conclusion:- Female students scored higher than male

# # Whether test preparation helps the students?

# H0: the students who completed the test preparation <= students who didn't completed the test preparation
# 
# H1: the students who completed the test preparation > students who didn't completed the test preparation
# 
# 
# 

# In[19]:


completed_marks=df.loc[(df['Test preparation']=='completed')]


# In[20]:


completed_marks['Total Marks']


# In[22]:


none_marks=df.loc[(df['Test preparation']=='none')]


# In[23]:


none_marks['Total Marks']


# In[24]:


t_stat,P_value=stats.ttest_ind(completed_marks['Total Marks'],none_marks['Total Marks'],alternative='greater')
print('T-statistics value is: ',t_stat,'P-Value is: ',P_value)


# T-statistics value is:  3.6143637527769217 P-Value is:  0.0006335646228660053
# Let us assume that our alpha is 0.05, from the above we can see that our value for P-value is 0.0006. So, we reject the null hypothesis value.
# 
# Conclusion:-The students who completed test preparation scored greater than the students who didn't.
