import os
import csv

budget_data = []

csv_path = os.path.join("..","python-challenge","PyBank","Resources","budget_data.csv")
#open csv file
with open(csv_path) as csvfile:
    budget_data_read = csv.reader(csvfile, delimiter=",")

    next(budget_data_read)

#read budget data into table
    
    for row in budget_data_read:
        budget_data.append(row)

#Get the month_count
    month_count = len(budget_data)

#Find the total by looping through the rows of column 2
    total = 0
    for rows in budget_data:
        total += int(rows[1])
#initialize variables
    Totaldifference = 0
    #the number of differences in the data set is -1 bc it takes two numbers at a time to subtract
    num_differences = month_count-1
    greatest_increase = 0
    greatest_decrease = 0

    for rows2 in range(num_differences):
        #calculate the differences between a row and the previous row
        diff = int(budget_data[rows2+1][1]) - int(budget_data[rows2][1]) 
        #add them up
        Totaldifference += diff
        #If the diff found is greater than the current greatest increase replace the current & retrieve the corresponding date. 
        if diff > greatest_increase or greatest_increase == 0:  
            greatest_increase = diff
            greatest_increase_date = budget_data[rows2 + 1][0]
        #Same for greatest decrease Capture it and store it 
        if diff < greatest_decrease or greatest_decrease == 0:  
            greatest_decrease = diff
            greatest_decrease_date = budget_data[rows2 + 1][0]
    #calculate average change which equals the total differences/the total number of differences it found (number of times it subtracted) 
    average_change = Totaldifference/num_differences

output_data = (
      f"\nFinancial Analysis\n\n"
      f"--------------------------\n\n"
      f"Total number of months: {month_count}\n\n" 
      f"Total: {total}\n\n"
      f"Average Change: $ {round(average_change,2)}\n\n"
      f"Greatest Increase in Profits: {greatest_increase_date} ($+{greatest_increase})\n\n"
      f"Greatest Decrease in Profits: {greatest_decrease_date}  (${greatest_decrease})\n\n"
      )
print(output_data)
#export output data in a text file
output_path = os.path.join("..","python-challenge","PyBank","Resources", "output.txt")
with open(output_path, 'w') as file:
    file.write(output_data)


    