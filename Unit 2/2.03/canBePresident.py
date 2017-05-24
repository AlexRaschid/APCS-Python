print("This program will determine if you are elidgeable to be president of the united states. Just answer the following questions.")
age = int(input("How old are you? "))
resident = int(input("How long have you been a resident of the United States? "))
naturalBorn = bool(input("Are you a natural born citizen? (Answer with true or false) "))


if age >= 35 and resident >= 14 and naturalBorn:
    print("You ARE able to become the President of the United States, TRUE")
else:
    print("You are NOT able to become the President of the United States, FALSE")

    
    
