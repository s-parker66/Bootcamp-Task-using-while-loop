'''get the user to input any number above 0 and continue to ask them to enter a number.
#if the user enters -1 then stop the program and find the average of the 
#numbers entered not including -1'''

#use math library for calculations later in the program
import math

#add variables for the while loop so they start at 0
#one for the sum of all user numbers entered and one for how many inputs the user enters
total_sum_of_numbers = 0
user_total_inputs = 0

#ask the user to input a number using a while loop

while True:
    user_input_str = input("\nPlease enter a number above 0 (enter -1 to stop): ")

    #insert try and except block to catch a value error
    try:
        
        #convert input to an integer
        user_input = int(user_input_str)
        
        #if user enters correct integer add inputs to counter variables
        if user_input > 0:
            total_sum_of_numbers += user_input
            user_total_inputs += 1

        #while loop will carry on until the user wishes to stop

        # add an if statement for when the user wants to stop and inputs -1
        #then find the average of the total of numbers entered by dividing by 
        #the number of inputs entered
        elif user_input == -1:
            average = (total_sum_of_numbers / user_total_inputs)

            #round the average total to 2 decimal places and then print the 
            #average of the numbers entered and then add a break to stop the program
            round_average = float(math.ceil(average*100)/100)
            print(f"\nThe average of the numbers entered is: {round_average}")
            break
        
        #make elif statement if user enters a number less than or equal to 0
        elif user_input <= 0:
            print("\nInvalid input. Number has to be above 0")
    
    #if the user enters anyhting but an integer, create a vlaue error message
    except ValueError:
        print("\nInvalid input: please enter an integer")
        continue   