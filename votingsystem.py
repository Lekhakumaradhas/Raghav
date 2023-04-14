nominee1 = input("Enter the name of first naminee: ")
nominee2 = input("Enter the name of second nominee: ")

nm1_votes = 0
nm2_votes = 0

voter_id = [1,2,3,4,5]
valid_voter_id = [1,2,3,4,5]
no_of_voter = len(voter_id)
while True:
    if voter_id == []: # check voter list completed
        print("voting session is over")
        if nm1_votes > nm2_votes:
            percent = (nm1_votes/no_of_voter)*100 # calculate the percent
            print(nominee1,"has won the election ",percent,"% of votes")
            break # to get rid of infinite loop
        elif nm2_votes > nm1_votes:
            percent = (nm2_votes/no_of_voter)*100
            print(nominee2,"has won the election ",percent,"% of votes")
            break
        else:
            print("Both have equal number of votes or goverment will12 decided")
            break

            
    voter = int(input("Enter your voter_id: "))
    if voter in voter_id:
        print("you are a voter ")
        voter_id.remove(voter)
        print("To give vote to ", nominee1, "Press 1")
        print("To give vote to ", nominee2, "Press 2")
        vote = int(input("Enter your precious vote: "))
        if vote == 1:
            nm1_votes +=1
            print(nominee1, "Thank you to give your vote to them")
        elif vote == 2:
            nm2_votes +=2
            print(nominee2, "Thank you to give you vote to them")
        elif vote > 2:
            print("check your pressed key")
        else :
            print("you are not a voter OR you have already a voter")
    elif voter in valid_voter_id:
            print("You have already voted")
    else:
            print("You are not a valid voter")