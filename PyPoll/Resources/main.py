# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Specify the file to read from
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
# Specify the file to write to
output_path = os.path.join('..', 'Resources', 'election_data_analysis_summary.txt')

# lists for placing the updated contents

pairs = {}
key_list = []
val_list = []
voter_id = []
county = []
candidate = []
unique_list = []
name_holder = []
percent_list = []
votes = []
count = []
#Reading using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:

        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        
        
    # calculating the total number of votes cast
    # Creating a list of uniqe candidates
    for name in candidate:
        if name not in unique_list:
            unique_list.append(name)
    #print(unique_list)          
    # Calculating the percentage of votes each candidate won
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for i in range(0,len(voter_id)):              
        if unique_list[0] == candidate[i]:
            count1 += 1        
        
        elif unique_list[1] == candidate[i]:
             count2 += 1
       
        elif unique_list[2] == candidate[i]:
             count3 += 1
        
        elif unique_list[3] == candidate[i]:
             count4 += 1

    count.append(count1) 
    count.append(count2)
    count.append(count3)
    count.append(count4)   
       
    # defining function for rounding and formating
    length = len(voter_id)
    
    def calc(count, length):
        win = (count/len(voter_id)) * 100
        win = round(win, 4)
        win = format(win, '.3f')
        return win

    # Calling function
    for i in range(0,len(unique_list)):
        win = calc(count[i], length)
        percent_list.append(win)
        val_list.append(count[i])
        #print(win)


    winner = max(val_list) 
   
    # Using dictionary comprehension
   
    pairs = {unique_list[i]:val_list[i] for i in range(0,len(unique_list))}
    #print(pairs)


    print('                                                                      \n')
    print('                      "Election Data Analysis Summary"                 \n')
    print('-----------------------------------------------------------------------\n')
    print(f"The total number of votes cast are: {len(voter_id)}\n" )
    print(f"The complete list of candidates who recieved votes are: {unique_list}\n" )
    print(f"The percentage of votes each candidate won are: {percent_list}\n" )
    print(f"The total number of votes each candidate won are: {val_list}\n" )  
    print(f"The winner of the election based on popular votes is: {unique_list[0]}\n" )
    print('------------------------------------------------------------------------\n')
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as textfile:
   
    # Write method to print the election_data_analysis_output 

    textfile.write('                                                                                   \n')
    textfile.write('                        "Election Data Analysis Summary"                           \n')
    textfile.write("-----------------------------------------------------------------------------------\n")
    textfile.write(f"The total number of votes cast are: {len(voter_id)}\n")           
    textfile.write(f"The complete list of candidates who recieved votes are: {unique_list}\n" )
    textfile.write(f"The percentage of votes each candidate won are: {percent_list}\n" )
    textfile.write(f"The total number of votes each candidate won are: {val_list}\n" )
    textfile.write('------------------------------------------------------------------------------------\n')
    textfile.write(f"The winner of the election based on popular votes is: {unique_list[0]}\n" )
    textfile.write('------------------------------------------------------------------------------------\n')