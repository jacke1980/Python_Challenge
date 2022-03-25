
import os
import csv
import statistics as st 

# define function to calculate average of the data #
def Average(data_csv):

    return round(st.mean(data_csv), 2) 

# define relative path for the input and output files #
input_file = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("Analysis", "pyBank_analysis.txt")

#  create empty lists for storing values and calculations from data #
Dates = []
Profit_Losses  = []
MontlyChanges=[]


#  read the CSV file and store values of each column #
with open(input_file, 'r') as budget_data:
    reader = csv.reader(budget_data, delimiter=",")
    
    # show header rows #
    Headers = next(reader)

    #  for loop to go through each row and append values from date column to the 'Dates' list and Profits/Losses column to the 'Profit_Losses' list #
    for row in reader:
        Dates.append(row[0])
        Profit_Losses.append(int(row[1]))

#  for loop to go through each value in Profit_Losses list and calculate total #
totalProfLoss = 0
for i in Profit_Losses:
    totalProfLoss = i + totalProfLoss

# use list comprehension to create a new list with difference values of each successive row (next row - current row) #
MontlyChanges = [Profit_Losses[i+1] - Profit_Losses[i] for i in range(0,len(Profit_Losses)-1)]

#  calculate average change by calling the function and store in variable #
AverageChange = Average(MontlyChanges)

#  insert a value of zero at index 0 of the ProfLossChanges list as there is no previous data to subtract for the first month ( also making the list equal in length to Dates and Profit_Losses lists for index finding later) #
MontlyChanges.insert(0,0)

#  initialize greatest increase/decrease variables to 0 #
GreatestIncrease = 0
GreatestDecrease = 0

#  for loop to calculate greatest increase and decrease in profits and losses #
for i in range(len(MontlyChanges)-1):
    if MontlyChanges[i] < GreatestDecrease:
        GreatestDecrease = MontlyChanges[i]

    if MontlyChanges[i] > GreatestIncrease:
        GreatestIncrease = MontlyChanges[i]   


#  find the index for the greatest increase and decrease in profits and losses #
GreatestIncrease_index = MontlyChanges.index(GreatestIncrease)
GreatestDecrease_index = MontlyChanges.index(GreatestDecrease)

# find the corresponding date of the greatest increase and decrease amounts using GI/GD indexes found above #
GreatestIncrease_date = Dates[GreatestIncrease_index]
GreatestDecrease_date = Dates[GreatestDecrease_index]
    
#  create output for text file#
analysisResult = (f"Financial Analysis\n"
                  f"----------------------------\n"
                  f"Total Months: {len(Dates)}\n"
                  f"Total: ${totalProfLoss}\n"
                  f"Average Change: ${AverageChange}\n"
                  f"Greatest Increase in Profits: {GreatestIncrease_date} (${GreatestIncrease})\n"
                  f"Greatest Decrease in Profits: {GreatestDecrease_date} (${GreatestDecrease})\n"
)

with open(output_file, 'w') as textfile:
    textfile.write(analysisResult)

# print analysis output to terminal #
print(analysisResult)










