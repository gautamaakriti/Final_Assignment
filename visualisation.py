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