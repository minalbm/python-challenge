# Please note that before running this code, make sure you are having the correct path for your own device.
# If you wanted to run the code in visual studio, if you choose to open only the PyBank folder, then the path to write your txt file would be: "Analysis","analysis.txt"
# If you choose to open the entire python challenge folder the path would change to: "PyBank","Analysis","analysis.txt"
# The path depends on where you store these files or you want to store your txt file.

import os
import csv


# Path to collect data from the resources folder
budget_data_csv = r"PyBank\Resources\budget_data.csv"


# Lists to store data:
# The list of all months included in the dataset
Total_Months = []

# The list of all "Profit/Losses" in the dataset
Total = []

# The list of all the "Profit/Losses" changes over the entire period
Changes = []


# Read in the CSV file
with open(budget_data_csv, "r") as csvfile:

    # Splits the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # Storing the header row
    header_row = next(csvreader)
    
    # Loop through the data
    for row in csvreader:

        # Adding all the dates to the Total_months list
        Total_Months.append(row[0])

        # Counting the total number of months included in the dataset
        Total_Months_Count = len(Total_Months)

        # Adding all the "Profit/Losses" to the Total list
        Total.append(row[1])
        
        # Since the "Profit/Losses" added to the list are of type string, in order to use the sum function to find the net total amount of "Profit/Losses" over the entire period, we have to change them to integer. 
        # Total_Int stores all the converted values of the Total list. Total_Int list is basically the same as the Total list but now the type has been changed to integer.
    Total_Int = []
    for num in Total:
        Total_Int.append(int(num))

        # To find the net total amount of "Profit/Losses" over the entire period, the sum function has been used which adds up all the values in the Total_Int list.
        Total_Count = sum(Total_Int)       

    # The Avg_Changes in "Profit/Losses" over the entire period can be calculated by subtracting the last value of "Profit/Losses" from the first value of "Profit/Losses" and divide it by the (Total length - 1).
    # The code will then round the result to have only 2 decimal places.  
    Avg_Change = round(float((int(Total[len(Total) - 1]) - int(Total[0])) / (len(Total) - 1)), 2)

    # In order to find the greatest increase & greatest decrease in profits over the entire period, at first a list called Changes have been created to store all the profit changes over the entire period.
    # The for loop, loops over the entire period and find the differences between two values and add them to the Changes list, so then a reference list is created to find the maximum and minimum values from there.
    for number in range(len(Total_Int) - 1):
        Data_Changes = ((Total_Int[number + 1]) - (Total_Int[number]))
        Changes.append(Data_Changes)
   
    # The greatest increase in profits over the entire period is basically the maximum value of the Changes list.
    Grt_Inc_Prof = max(Changes)
    
    # In order to find the date that the greatest increase happen, we just need to find the index or the location of where the maximum changes happen.
    Grt_Inc_Prof_Date = Total_Months[Changes.index(max(Changes)) + 1]

    # The greatest decrease in profits over the entire period is basically the minimum value of the Changes list.
    Grt_Dec_Prof = min(Changes)
    
    # In order to find the date that the greatest decrease happen, we just need to find the index or the location of where the minimum changes happen.
    Grt_Dec_Prof_Date = Total_Months[Changes.index(min(Changes)) + 1]


# Printing all the requested values in the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Total_Months_Count}")
print(f"Total: ${Total_Count}")
print(f"Average Change: ${Avg_Change}")
print(f"Greatest Increase in Profits: {Grt_Inc_Prof_Date} (${Grt_Inc_Prof})")
print(f"Greatest Decrease in Profits: {Grt_Dec_Prof_Date} (${Grt_Dec_Prof})")


# This creates the analysis.txt file and will add it under the Analysis folder.
Analysis = os.path.join("PyBank","Analysis","analysis.txt")

# Open the analysis file
with open(Analysis, "w") as txtfile:
    
    # Writes all the requested values and results in the created text file. 
    # "\n" is used to go to the next line
    txtfile.write("Financial Analysis" + "\n")
    txtfile.write("\n")
    txtfile.write("----------------------------" + "\n")
    txtfile.write("\n")
    txtfile.write(f"Total Months: {Total_Months_Count}" + "\n")
    txtfile.write("\n")
    txtfile.write(f"Total: ${Total_Count}" + "\n")
    txtfile.write("\n")
    txtfile.write(f"Average Change: ${Avg_Change}" + "\n")
    txtfile.write("\n")
    txtfile.write(f"Greatest Increase in Profits: {Grt_Inc_Prof_Date} (${Grt_Inc_Prof})" + "\n")
    txtfile.write("\n")
    txtfile.write(f"Greatest Decrease in Profits: {Grt_Dec_Prof_Date} (${Grt_Dec_Prof})" + "\n")




