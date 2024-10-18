#!/usr/bin/env python
# coding: utf-8

# ### Importing Libraries

# In[1]:


import numpy as np 
import pandas as pd 


# ### Load Datasets

# #### Define the path to the dataset and load it into a pandas DataFrame

# In[2]:


path = "/Users/aakritigautam/Downloads/climate_change_impact_on_agriculture_2024.csv"


# In[3]:


climate_impact_df = pd.read_csv(path)
climate_impact_df


# ### Data Exploration and Cleaning

# #### Display column names:
# This provides an overview of the available data and helps understand the structure of the dataset.

# In[5]:


climate_impact_df.columns


# The dataset is well-structured with 15 columns capturing various aspects of climate change and agriculture.

# #### Display DataFrame information:
# The '.info()' method provides details about the dataset, such as the number of entries, column data types, and non-null values.

# In[6]:


climate_impact_df.info()


# #### Describe the data 
# This gives a quick look at key statistics (mean, standard deviation, min, max, quartiles) of numeric columns.

# In[7]:


climate_impact_df.describe()


# The dataset spans a period from 1990 to 2024, with diverse information on climate conditions, crop yield, and economic impact. Descriptive statistics hint at potential outliers (like negative temperatures) which may require further investigation.

# #### Find any missing values:
# Replace common placeholders for missing data (like '-', 'N/A', 'na') with NaN, then check for any null values.

# In[10]:


climate_impact_df.replace(['', ' ', '-', 'N/A', 'na', '?'], np.nan, inplace=True)
climate_impact_df.isnull().sum()


# No missing values were identified, which simplifies further analysis.

# In[ ]:
