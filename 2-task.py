# Task 2: Write real time example if, elif, else

print("--------Welcome to Voting eligibility checker---------")

age = float (input("Enter your age: "))

if age > 18:
    print("-----You already eligible to vote----- \n -----Do not forget to vote in the upcoming election----- " )

elif age == 18:
    print("-----You are now eligible to vote----- \n -----Apply for voter ID----- \n -----Do not forget to vote in the upcoming election----- ")

else:
    years = 18 - age
    print(f" -----You are not eligible for voting in upcoming election (2024)----- \n You need to wait for {years} years to vote" )


      

