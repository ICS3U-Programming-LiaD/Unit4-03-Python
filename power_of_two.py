#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Nov. 3rd, 2022
# This program 
# displays the user input to the power of 2 and all the 
# numbers before the user input to the power of 2
 
def main(): 


# Initializes the counter
        counter = 0
# getting an integer from the user
        user_number_as_string = input("Enter a whole integer: ")


        try:

                user_number_as_int = int(user_number_as_string)
                if user_number_as_int >= 0:
                        counter = counter + 1
        # The For Loop
                for counter in range(user_number_as_int + 1):
                        power_of_two = counter**2
                        print("{}^2 = {}".format(counter, power_of_two))
                else:
                        print("Invalid input, enter a positive number")
        except Exception:
                print("Invalid input, please input number")

        finally:
                print("Thanks for playing!")

if __name__ == "__main__":
                main()
