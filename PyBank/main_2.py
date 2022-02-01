#!/usr/bin/env python
# coding: utf-8

# In[67]:


import os
import csv
from statistics import mean, median
import pandas as pd 


# In[68]:


#Reference to Budget csv file
Budget_Path = os.path.join("Resources", "budget_data.csv")
Budget_Path_df = pd.read_csv(Budget_Path, encoding="utf-8")
Budget_Path_df.head()
#how many rows to find how many months
#print(len(Budget_Path_df))


# In[69]:


Budget_Path_df.dtypes


# In[70]:


Budget_Path_df.index


# In[71]:


Months = len(Budget_Path_df)
print(Months)


# In[72]:


#Sum of rows Profit/Losses
Net_Total_Amount=Budget_Path_df["Profit/Losses"].sum()
#print(Net_Total_Amount)
print(Net_Total_Amount)


# In[73]:


#Find the Average amount of total period 
Average_Amount = round(Net_Total_Amount/Months)
#print(Average_Amount)
print(Average_Amount)


# In[74]:


for index, row in Budget_Path_df.head(n=85).iterrows():

    Budget_Path_df.loc[index+1, "Month Change"]=Budget_Path_df.loc[index+1,"Profit/Losses"]- Budget_Path_df.loc[index,"Profit/Losses"]
Budget_Path_df



# In[75]:


Budget=Budget_Path_df.fillna(0)
Budget


# In[ ]:





# In[76]:


Average_Change=Budget["Month Change"].sum()
Average_Change


# In[79]:


Y_change= Average_Change/(Months-1)
Year_change=round(Y_change,2)
Year_change


# In[46]:


Greatest_Increase = max(Budget["Month Change"])
print(Greatest_Increase)


# In[104]:


Gest_I_Month = Budget.loc[Budget["Month Change"] == Greatest_Increase, :]
Gest_I_Month


# In[105]:


Greatest_Decrease = min(Budget["Month Change"])
print(Greatest_Decrease)


# In[106]:


Gest_D_Month = Budget.loc[Budget["Month Change"] == Greatest_Decrease, :]
Gest_D_Month


# In[109]:


print("--------------------------------------------------------------------------------------")
print("      Financial Analysis")
print("--------------------------------------------------------------------------------------")
print("Total Months:     " +str(Months))
print("Total:            " +str(Net_Total_Amount))
print("Average Change:   " +str(Year_change))
print(f'Greatest Increase: {Gest_I_Month.loc[25,"Date"]} ${Gest_I_Month.loc[25,"Month Change"]}')
print(f'Greatest Decrease: {Gest_D_Month.loc[44,"Date"]} ${Gest_D_Month.loc[44,"Month Change"]}')
print("----------------------------------------------------------------------------------------")


# In[ ]:




