# 
# =================================================================
# This is the "pyBank" Financial Analysis
# Python 3.6.3 script to calculate the following:
# Total number of months included in datasets
# Total amount of revenue gained over entire period
# Average Change in revenue between months over the entire period
# Greatest increase in revenue over the entire period
# Greatest decrease in revenue over the entire period
# =================================================================
#
# Modules
import os
import csv

# Set path for file

infile1 = os.path.join('Resources', 'budget_data_1.csv')
infile2 = os.path.join('Resources', 'budget_data_2.csv')
outputf = os.path.join('Resources', 'pyBank_analysis.txt')

my_data = [] # initialize the input files list
saveinfile1 = {} # saving the budget_data1.csv in a dictionary
saveinfile2 = {} # saving the budget_data2.csv in a dictioany
monthyyrev = {} # initialize the dictionary for saving Month-year-revenue from input dataset file
unique_year = {} # for every year there are 12 months (monthsort dictionary)
same_months = {} # initialize the dictionary for saving unique months
monthsort = {} # initialize the months dictionary for sorting 
ttavgchg_bet_months = {} # initiaze the dictionary for total average change between months 


monthsort = {"Jan": 1,"Feb": 2,"Mar": 3,"Apr": 4,"May": 5, "Jun": 6,"Jul": 7, "Aug": 8, "Sep": 9,"Oct": 10,"Nov": 11,"Dec": 12}
 

my_data = [ infile1, infile2 ]  # list with input dataset files
my_len = len(my_data) # getting the length of the list to lookp through the input data sets
 

# Loop through all the input dataset files
while (my_len) != 0:  

    # Open the CSV file one at a time Hint : indexing of list starts from 0
    with open(my_data[(my_len -1)] , newline='') as csvfile:
  
        csvreader = csv.reader(csvfile, delimiter=',') # reads the cvs files with delimiter ',' 
        next(csvreader) ## This skips the first row of the csv file (this has headers )

        # loop through the input lines in a row - one row at a time
        for row in csvreader:
            
            # splitting the date into month and year(yy)
            words = row[0].split('-')
            mon = words[0]
            yearstr = words[1]
            
            # if year string is 4 digits
            if (len(yearstr)) == 4:
                yearstr = (yearstr[2:]) # taking only last 2 digits
                row[0] = (mon + '-' + yearstr) # concatenating the month and year back into original format

            # creating a dictionary to store date as key , and revenue as value
            if (my_len == 2):
                saveinfile1[row[0]] = row[1] 
            elif (my_len == 1):
                saveinfile2[row[0]] = row[1] 
                #print("This is from infile1")
                #print(saveinfile1)
    
    my_len = my_len - 1  #Loop through all the input dataset files


# Open a file for writing and create - if it does not exist
fw = open(outputf, 'a+')

# write the header to the outputfile
fw.write("\n")
fw.write("\n")
fw.write("Financial Analysis\n")
fw.write("---------------------------\n")


# looping through the datasets to find unique months and year
for key1 in saveinfile1.keys():
    for key2 in saveinfile2.keys():
        if key1 == key2:  # if month and year is same 
            sametotrev = (int(saveinfile1[key1]) + int(saveinfile2[key2])) # add the revenue values together
            same_months[key2] = str(sametotrev)
            #same_months = {"Date": key1, "revenue": sametotrev} # saving into a dictionary with uniquie months and year
            break # breaking the loop after finding the same month and year
    else:
        if key1 in saveinfile1.keys(): # if not same month and year
            difftotrev = (saveinfile1[key1]) # save the revenue 
            same_months[key1] = str(difftotrev)
            #same_months = {"Date": key1, "revenue": difftotrev} # add into the dictionary with unique month and year
#print(same_months)
# looping through the same_months dictionary for analysis



#===============================================================
# Financial analysis while looping through the saved dictionary
#===============================================================
total_months = 0 # counter of total unique months
ttavgchg_months = 0 # counter of revenue change
total_revenue = 0 # counter of total revenue
currentrev = 0
previousrev = 0
flag = False


for k, v in same_months.items():
    #print("This is k: ", k)
    #print("This is v: ", v)
    total_months += 1   # Calculating total number of unique months over the period
    total_revenue += int(v) # Calculating total revenue over the entire period
    
    # Calculating the revenue between months over entire period
    if flag == False:
        previousrev = int(v)
        currentrev = int(v)
        #print("This is from False")
        #print(previousrev)
        #print(currentrev)
        betmonrev = (currentrev) - (previousrev) # currentmonth revenue minus previousmonth revenue
        #print(betmonrev)
        flag = True
    else:
        #print("This is from True")
        #print(previousrev)
        #print(currentrev)
        previousrev = currentrev
        currentrev = int(v)

        betmonrev = (currentrev) - (previousrev)
        #print(betmonrev)
        ttavgchg_bet_months[k] = str(betmonrev)

#print("This is from ttavgchg_bet_months")
#print(ttavgchg_bet_months)   


#Total Average change between months 
min = 0
max = 0
min_mon = ""
max_mon = ""

for m, v in ttavgchg_bet_months.items():
    ttavgchg_months += int(v)
    avg = ttavgchg_months/total_months
    
    # Greatest Increase and Greatest Decrease in Revenue
    # Check for min
    if int(v) < min:
        min = int(v)
        min_mon = m
    elif int(v) > max:
        max = int(v)
        max_mon = m


#print("This is min")
#print(min)
#print("This is max")
#print(max)


fw.write("Total Months:   %d\n" %(total_months))
fw.write("Total Revenue:  $%d\n" %(total_revenue))
fw.write("Average Revenue Change:   $%d\n" %(avg))
fw.write("Greatest Increase in Revenue: %s  ($%d ) \n" %(max_mon, max))
fw.write("Greatest Decrease in Revenue: %s  ($%d ) \n"  %(min_mon, min))
fw.write("\n")
fw.write("\n")


fw.close()