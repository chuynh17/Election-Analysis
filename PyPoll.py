#The Data we need to retrieve (Dependencies)
import csv 
import os

#assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')
#create a filename variable to a direct or indirect path to a file
file_to_save = os.path.join("Analysis", "election_analysis.txt")


#Initialize a total vote counter
total_votes = 0
#Get Candidates Names
candidate_options = []
#Get Candidates Votes
candidate_votes = {}
#Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election result and read the file.
with open(file_to_load) as election_data:


        #Read the file object with the reader function
        file_reader = csv.reader(election_data)
        #Print the header row
        headers = next(file_reader)
        #Print each row in the CSV file
        for row in file_reader:


                #add to the total vote count.
                total_votes +=1
                #print the candidate name from each row.
                candidate_name = row[2]
                #If the candidate does not match any existing candidate...
                if candidate_name not in candidate_options:


                        #Add the candidate name to the candidate list.
                        candidate_options.append(candidate_name)
                        #Begin tracking that cnadidate's vote count.
                        candidate_votes[candidate_name] = 0


                #add a vote to that candidates count
                candidate_votes[candidate_name] +=1


        #print the candidate vote dictionary.
        print(candidate_votes)
        #print the candidatelist
        print(candidate_options)
        #Print the total votes.
        print(total_votes)

        #Determine the percentage votes for each candidate by looping through the counts
        
        #Iterate thought the candidate list.
        for candidate_name in candidate_votes:
                #retrieve vote count of a candidate
                votes = candidate_votes[candidate_name]
                #calculate the percentage of votes
                vote_percentage = float(votes)/ float(total_votes)*100


                #Determine winning vote count and candidate
                #Determine if the votes is greater than the winning count.
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                        #If true then set winning_count = votes and winning_percent = vote_percentage
                        winning_count = votes 
                        winning_percentage = vote_percentage
                        #set the winning_candidate equal to the candidate's name
                        winning_candidate = candidate_name

                
                #print the candidate name and percentage votes
                print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")
                #Print out each candidate's name, vote count, and percentage of votes
                print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


                winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
                print(winning_candidate_summary)


#print the file object
print(election_data)


#Using the open() function the 'w' mode we will write the data to the file
with open(file_to_save, "w") as txt_file:
        
        #Write three counties to the file
        txt_file.write("Counties in the Election")
        txt_file.write("\n-------------------------")
        txt_file.write("\nArapahoe\nDenver\nJefferson")

#Close the File
txt_file.close()

