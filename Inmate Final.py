#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


#Adding Column Names

column_names = ['DCNumber', 'LastName', 'FirstName', 'MiddleName', 'NameSuffix', 'Race', 'Sex', 'BirthDate', 'PrisonReleaseDate', 'ReceiptDate', 'releasedateflag_descr', 'race_descr', 'custody_description','FACILITY_description', 'Age']


# In[3]:


#Importing Data

data1 = pd.read_csv('1.csv',sep=',', header=None, names=column_names)


# In[4]:


data1


# In[5]:


#Adding Column Names

column_names2=['DCNumber', 'Sequence', 'OffenseDate', 'DateAdjudicated', 'County', 'CaseNumber', 'prisonterm', 'adjudicationcharge_descr']


# In[6]:


#Importing Data

data2 = pd.read_csv('2.csv', low_memory=False,sep=',', header=None, names=column_names2)


# In[7]:


data2


# In[8]:


#Saving the file as csv

data1.to_csv('InMateRoot.csv', index=False)


# In[9]:


#Saving the file as csv

data2.to_csv('InmateOFFense.csv', index=False)


# In[10]:


import pandas as pd

#Load the data
inmate_active_root = pd.read_csv('InMateRoot.csv', sep=',', dtype={'DCNumber': str})
inmate_active_offenses = pd.read_csv('InmateOFFense.csv', sep=',', dtype={'DCNumber': str})

#Merge the DataFrames on 'DCNumber'
merged_df = pd.merge(inmate_active_root, inmate_active_offenses, on='DCNumber', how='inner')

#Filter for 'FLORIDA STATE PRISON' in 'FACILITY_description'
florida_state_prison = merged_df[merged_df['FACILITY_description'] == 'FLORIDA STATE PRISON']

#Count by offense
offense_counts = florida_state_prison.groupby('adjudicationcharge_descr')['DCNumber'].count().reset_index(name='Count')

#Sort the counts in descending order 
offense_counts_sorted = offense_counts.sort_values(by='Count', ascending=False)

print(offense_counts_sorted)


# In[11]:


#Number of Inmates by Facility

inmates_by_facility = merged_df['FACILITY_description'].value_counts().reset_index()
inmates_by_facility.columns = ['Facility', 'Number of Inmates']


# In[12]:


#Number of Offenses by Type

offenses_by_type = merged_df['adjudicationcharge_descr'].value_counts().reset_index()
offenses_by_type.columns = ['Offense Type', 'Count']


# In[13]:


#Distribution of Inmates by Age

from datetime import datetime

merged_df['BirthDate'] = pd.to_datetime(merged_df['BirthDate'])
merged_df['Age'] = merged_df['BirthDate'].apply(lambda x: datetime.now().year - x.year)
age_distribution = merged_df['Age'].value_counts().sort_index()


# In[14]:


#Distribution of Offenses Over Time

merged_df['ReceiptDate'] = pd.to_datetime(merged_df['ReceiptDate'])
offenses_over_time = merged_df.resample('YE', on='ReceiptDate').size()


# In[15]:


import matplotlib.pyplot as plt

#Plotting number of inmates by facility
inmates_by_facility.plot(kind='bar', x='Facility', y='Number of Inmates', figsize=(10, 6))
plt.title('Number of Inmates by Facility')
plt.ylabel('Number of Inmates')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[16]:


#From 'adjudicationcharge_descr'
offenses_by_type = merged_df['adjudicationcharge_descr'].value_counts().head(10)  # Top 10 offenses
offenses_by_type.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Offenses by Type')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[17]:


#Distribution of Ages

age_distribution = merged_df['Age'].dropna().value_counts().sort_index()  # Remove NaN values
age_distribution.plot(kind='bar', figsize=(10, 6), color='orange')
plt.title('Distribution of Inmates by Age')
plt.xlabel('Age')
plt.ylabel('Number of Inmates')
plt.tight_layout()
plt.show()


# In[18]:


#Group by year and count offenses

offenses_over_time = merged_df.groupby(merged_df['ReceiptDate'].dt.year)['DCNumber'].count()
offenses_over_time.plot(kind='line', marker='o', figsize=(10, 6), color='green')
plt.title('Offenses Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Offenses')
plt.show()


# In[19]:


filtered_df = merged_df[merged_df['ReceiptDate'].dt.year >= 2000]

# Group by year and count offenses in the filtered DataFrame
offenses_over_time = filtered_df.groupby(filtered_df['ReceiptDate'].dt.year)['DCNumber'].count()

# Plotting
offenses_over_time.plot(kind='line', marker='o', figsize=(10, 6), color='green')
plt.title('Offenses Over Time (From 2000 Onwards)')
plt.xlabel('Year')
plt.ylabel('Number of Offenses')
plt.grid(True)  # Optional: Adds a grid for better readability
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




