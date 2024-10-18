#!/usr/bin/env python
# coding: utf-8

# ## Importing Libraries

# In[24]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# ## Load Datasets

# #### Define the path to the dataset and load it into a pandas DataFrame

# In[25]:


path = "/Users/aakritigautam/Downloads/climate_change_impact_on_agriculture_2024.csv"


# In[26]:


climate_impact_df = pd.read_csv(path)
climate_impact_df


# ## Data Exploration and Cleaning

# #### Display column names:
# This provides an overview of the available data and helps understand the structure of the dataset.

# In[27]:


climate_impact_df.columns


# The dataset is well-structured with 15 columns capturing various aspects of climate change and agriculture.

# #### Display DataFrame information:
# The '.info()' method provides details about the dataset, such as the number of entries, column data types, and non-null values.

# In[28]:


climate_impact_df.info()


# #### Describe the data 
# This gives a quick look at key statistics (mean, standard deviation, min, max, quartiles) of numeric columns.

# In[29]:


climate_impact_df.describe()


# The dataset spans a period from 1990 to 2024, with diverse information on climate conditions, crop yield, and economic impact. Descriptive statistics hint at potential outliers (like negative temperatures) which may require further investigation.

# #### Find any missing values:
# Replace common placeholders for missing data (like '-', 'N/A', 'na') with NaN, then check for any null values.

# In[30]:


climate_impact_df.replace(['', ' ', '-', 'N/A', 'na', '?'], np.nan, inplace=True)
climate_impact_df.isnull().sum()


# No missing values were identified, which simplifies further analysis.

# ## Data Visualization

# ##### 1. How does climate change impact farming and food production?

# In[59]:


plt.figure(figsize= (14, 8))
plt.suptitle("Impact of Climate Change on Agriculture Over the Years", fontsize= 20, fontweight= "bold", y= 1.05)

# Average Temperature over the years
plt.subplot(2, 2, 1)
sns.lineplot(x= "Year", y= "Average_Temperature_C", data= climate_impact_df, marker= "o")
plt.title("Average Temperature Over Years", fontweight= "bold")
plt.xlabel("Year")
plt.ylabel("Avg Temperature (°C)")
plt.annotate("Shows the trend of yearly average temperatures.", 
             xy= (0.5, -0.25), xycoords= "axes fraction", ha= "center", fontsize= 9)

# Precipitation over the years
plt.subplot(2, 2, 2)
sns.lineplot(x= "Year", y= "Total_Precipitation_mm", data= climate_impact_df, marker= "o")
plt.title("Total Precipitation Over Years", fontweight= "bold")
plt.xlabel("Year")
plt.ylabel("Precipitation (mm)")
plt.annotate("Tracks yearly precipitation levels.", 
             xy= (0.5, -0.25), xycoords= "axes fraction", ha= "center", fontsize=9)

# CO2 Emissions over the years
plt.subplot(2, 2, 3)
sns.lineplot(x= "Year", y= "CO2_Emissions_MT", data= climate_impact_df, marker= "o")
plt.title("CO2 Emissions Over Years", fontweight= "bold")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions (MT)")
plt.annotate("Monitors CO2 emissions per year.", 
             xy= (0.5, -0.25), xycoords= "axes fraction", ha= "center", fontsize= 9)

# Crop Yield over the years
plt.subplot(2, 2, 4)
sns.lineplot(x= "Year", y= "Crop_Yield_MT_per_HA", data= climate_impact_df, marker= "o")
plt.title( "Crop Yield Over Years", fontweight= "bold")
plt.xlabel("Year")
plt.ylabel("Crop Yield (MT/HA)")
plt.annotate("Displays annual crop yield trends.", 
             xy=(0.5, -0.25), xycoords= "axes fraction", ha= "center", fontsize= 9)

# Adjust spacing between plots and from the top title
plt.tight_layout()
plt.subplots_adjust(top= 0.92, hspace= 0.5, wspace= 0.4)
plt.show()


# The above graph illustrates the impact of climate change on agriculture from 1990 to 2025, focusing on temperature, precipitation, CO2 emissions, and crop yield. The first graph shows an upward trend in average temperatures, fluctuating between 13°C and 17°C, indicating global warming over time. The second graph tracks total precipitation, which varies between 1450 mm and 1750 mm, showing no clear long-term trend but highlighting erratic rainfall patterns. The third graph depicts CO2 emissions, fluctuating between 13 and 17 million metric tons, with a slight increase, reflecting rising human-induced emissions. The fourth graph shows crop yield trends, ranging from 2.0 to 2.5 metric tons per hectare, with no consistent increase or decrease, suggesting the unpredictable effects of climate change on agricultural productivity. Together, the graphs demonstrate the complex and variable relationship between climate factors and agricultural outcomes.

# ##### 2. Which crops are producing the most or less over time during climate change?

# #### Plotting crop yields by Crop Type

# In[58]:


plt.figure(figsize=(10, 6))
sns.boxplot(x= "Crop_Type", y= "Crop_Yield_MT_per_HA", data= climate_impact_df)
plt.title("Crop Yields by Crop Type", fontsize= 16, fontweight= "bold", y= 1.05)
plt.xlabel("Crop Type")
plt.ylabel("Crop Yield (MT/HA)")
plt.show()


# The above box plot illustrates the distribution of crop yields, measured in metric tons per hectare (MT/HA), for various crop types, including Corn, Wheat, Coffee, Sugarcane, Fruits, Rice, Barley, Vegetables, Soybeans, and Cotton. The thick line within each box represents the median yield for each crop type, with most crops showing a median yield of around 2 MT/HA. The boxes themselves display the interquartile range (IQR), which captures the middle 50% of data points, indicating that the range of yields is fairly consistent across the different crops. The whiskers extending from each box show the overall spread of the yields, excluding any outliers, revealing that the yields for all crop types range from 1 to 5 MT/HA. Notably, no significant outliers are present in this visualization, highlighting the uniformity in the distribution of yields across all crops.

# ## Model Building and Evaluation

# ##### 3. How will food production impact the future?

# In[50]:


X = climate_impact_df[["Average_Temperature_C", "Total_Precipitation_mm", "CO2_Emissions_MT"]]
y = climate_impact_df["Crop_Yield_MT_per_HA"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# #### Building the linear regression model

# In[52]:


model = LinearRegression()
model.fit(X_train, y_train)


# In[53]:


y_pred = model.predict(X_test)


# #### Evaluating the model

# In[55]:


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')


# #### Predicting crop yields for future years

# In[56]:


future_data = pd.DataFrame({
    'Average_Temperature_C': [1.8, 2.5, 3.0],  # Future temperature projections
    'Total_Precipitation_mm': [500, 600, 700],  # Future precipitation projections
    'CO2_Emissions_MT': [40, 45, 50]  # Future CO2 emission projections
})

future_yields = model.predict(future_data)
print(f'Predicted Future Yields: {future_yields}')


# The predicted future yields, represented by the values [1.63831702, 1.61054581, 1.57814449], provide estimates of crop productivity, measured in metric tons per hectare (MT/HA), for upcoming harvest periods. These values suggest a slight downward trend in future yields. The first predicted yield is approximately 1.64 MT/HA, followed by a second yield estimate of 1.61 MT/HA, and finally, a third yield prediction of 1.58 MT/HA. This indicates a small but gradual decrease in crop productivity over the forecasted time frame. Understanding these predictions can help farmers and agricultural planners prepare for potential changes in output and make decisions to mitigate any potential decline.
