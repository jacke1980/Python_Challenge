#!/usr/bin/env python
# coding: utf-8

# In[33]:


import os
import csv
import pandas as pd


# In[34]:


#Reference to Poll csv file
Poll_Path = os.path.join("Resources", "election_data.csv")
Poll_Path_df = pd.read_csv(Poll_Path, encoding="utf-8")
Poll_Path_df.head()


# In[35]:


#Total Votes
Votes = len(Poll_Path_df)



# In[36]:


#Finding candidates
Candidates=list(Poll_Path_df["Candidate"].unique())



# In[37]:


#Finding votes by candidate
Vote_chart=Poll_Path_df["Candidate"].value_counts()



# In[38]:


Vote_chart_df=pd.DataFrame(Vote_chart)
Vote_chart_df["percent"]=round((Vote_chart_df["Candidate"]/Votes*100),2)
Vote_chart_df


# In[39]:


Vote_chart_df.dtypes



# In[40]:


Vote_chart_df["percent"]= "%"+ Vote_chart_df["percent"].astype(str) 


# In[41]:


Vote_chart_df=Vote_chart_df.rename(columns={"Candidate":"Votes", "percent":"Percent"})
chart_df=pd.DataFrame(Vote_chart_df)
chart_df


# In[42]:


#Finding the Winner
Winner="Khan"
Winner


# In[44]:


print("-------------------------------")
print(" ELECTIONS RESULTS")
print("-------------------------------")
print(" Total votes: "+ str(Votes))
print("-------------------------------")
print( f'{chart_df}')
print("-------------------------------")
print(" Winner:   "+   str(Winner))
print("-------------------------------")


# In[ ]:





# In[ ]:





# In[ ]:




