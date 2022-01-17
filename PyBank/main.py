import os
import csv
from statistics import mean, median
import pandas as pd 

#Reference to Budget csv file
Budget_Path = os.path.join("Resources", "budget_data.csv")
Budget_Path_df = pd.read_csv(Budget_Path, encoding="utf-8")
Budget_Path_df.head()
#how many rows to find how many months
#print(len(Budget_Path_df))
Months = len(Budget_Path_df)

#Sum of rows Profit/Losses
Net_Total_Amount=sum(Budget_Path_df["Profit/Losses"])
#print(Net_Total_Amount)

#Find the Average amount of total period 
Average_Amount = round(Net_Total_Amount/Months)
#print(Average_Amount)

Budget_Path_df["Yearly_change"]=Budget_Path_df["Profit/Losses"] - Average_Amount
Budget_Path_df.head()
print(Budget_Path_df)

#The Average change is calculated by the mean of rows Yearly_change
Total_Year_change=median(Budget_Path_df["Yearly_change"])
Total_Yearly_change=round(Total_Year_change,4)
#print(Total_Yearly_change)

#Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest_Increase=max(Budget_Path_df["Yearly_change"])
#print(Greatest_Increase)

#Greatest Decrease in Profits: Sep-2013 ($-2196167)
Greatest_Decrease = min(Budget_Path_df["Yearly_change"])
Greatest_Monthly_Decrease= Budget_Path_df
#print(Greatest_Decrease)
print("--------------------------------")
print("Financial Analysis")
print("--------------------------------")
print("Total Months:     " +str(Months))
print("Total:            " +str(Net_Total_Amount))
print("Average Change:   " +str(Total_Yearly_change))
print("Greatest Increase: " +str(Greatest_Increase))
print("Greatest Decrease: " +str(Greatest_Decrease))
