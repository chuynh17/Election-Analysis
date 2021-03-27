#The Data we need to retrieve
import csv 
import os

#assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')

#create a filename variable to a direct or indirect path to a file
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#To do: read and analyze the data here

#Open the election resule and read the file.
with open(file_to_load) as election_data:

        #Read the file object with the reader function
        file_reader = csv.reader(election_data)

        #Print the header row
        headers = next(file_reader)
        print(headers)

#print the file object
print(election_data)

#Using he open() function the 'w' mode we will write the data to the file
with open(file_to_save, "w") as txt_file:
        
        #Write three counties to the file
        txt_file.write("Counties in the Election")
        txt_file.write("\n-------------------------")
        txt_file.write("\nArapahoe\nDenver\nJefferson")

#Close the File
txt_file.close()

#Write down the names of all the candidates
#Add a vote count for each candidate
#Get the total votes for each candidate
#Get the total votes cast for the Election