# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Specify the file to read from
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# Specify the file to write to
output_path = os.path.join('..', 'Resources', 'budget_data_analysis_summary.txt')

# lists for placing the updated contents
pairs = {}
key_list = []
val_list = []
total_month = []
profit_loss = []

#Reading using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:

        key_list.append(row[0])

        # calculating the total number of months
        month = row[0].split('-')           
        total_month.append(month[0])
        #print(month[0]) 
    
        # calculating the net total amount of "profit/losses" over the entire period.
               
        profit_loss.append(int(row[1]))
Sum = sum(profit_loss)  
#print(Sum)    

# calculating the changes in profit/losses over the entire period
    
i = 0
change = []
lenght = len(profit_loss) - 1
for i in range(lenght):
    difference = profit_loss[i + 1] - profit_loss[i]
    change.append(difference)
    i = i + 1
    #print(change)
avg_change = (sum(change) / lenght) 
#print(round(avg_change, 2))


# calculating the greatest increase and greatest decrease in profit

greatest_increase = max(change)
#print(greatest_increase)

greatest_decrease = min(change)
#print(greatest_decrease)

#adding 'dates' as 'key' and 'profit/loses' as 'value' in adictionary                  
        
       
pairs = {key_list[i]:change[i] for i in range(0,len(change))}
#print(pairs)

# finding the date for greatest increase in change in profit
for i in range(0,len(change)):
    if greatest_increase == change[i]: 
        date1 = key_list[i + 1]
        #print(greatest_increase, key_list[i + 1])

# finding the date for greatest decrease in change in profit
for i in range(0,len(change)):
    if greatest_decrease == change[i]: 
        date2 = key_list[i + 1]
        #print(greatest_increase, key_list[i + 1])

print('                        "Budget Data Analysis Summary"                               \n')
print("-----------------------------------------------------------------------------------\n")
print(f"The total number of months included in the database are: {len(total_month)}\n")           
print(f"The net total amount of profit/losses over the entire period: ${(Sum)}\n")
print(f"The average change in profit/losses over the entire period: ${round(avg_change, 2)}\n")
print(f"The greatest increase in profit/losses over the entire period: ${round(greatest_increase, 2)} {str(date1)}\n")
print(f"The greatest decrease in profit/losses over the entire period: ${round(greatest_decrease, 2)} {str(date2)}\n")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as textfile:
   
# Write method to print the Budget_data_analysis_output

    
    textfile.write('                        "Budget Data Analysis Summary"                               \n')
    textfile.write("-----------------------------------------------------------------------------------\n")
    textfile.write(f"The total number of months included in the database are: {len(total_month)}\n")           
    textfile.write(f"The net total amount of profit/losses over the entire period: ${(Sum)}\n")
    textfile.write(f"The average change in profit/losses over the entire period: ${round(avg_change, 2)}\n")
    textfile.write(f"The greatest increase in profit/losses over the entire period: ${round(greatest_increase, 2)} {str(date1)}\n")
    textfile.write(f"The greatest decrease in profit/losses over the entire period: ${round(greatest_decrease, 2)} {str(date2)}\n")






    
       


        
