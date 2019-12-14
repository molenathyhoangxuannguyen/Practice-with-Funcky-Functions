######################################################################
# Author: Thy H. Nguyen
# Username: nguyent2
#
# Assignment: T06: Funky Functions Test Suite
# Purpose:  Write a simple function for Samantha to write the test suite.

######################################################################
def check_5_characters_functions(strings):
    """
    This function checks to see if the user's input has more than, or equal to 5 characters, or not.
    :param strings: This variable "strings" saves the user's input
    :return: True if the user's input has more than, or equal to 5 characters
    return False if the user's input has fewer than 5 characters
    """
    if len(strings) >= 5:
        #This line checks to see if the string has more than 5 characters or not.
        return True
        #If the user's input has more than 5 characters, the function will return True
    else:
        #If the user's input does not have more than 5 characters, the function will return False
        return False
def main():
    """
    This function ask for the user's input on the screen
    :return: This function will return True, if the user's input has more than, or equal to 5 characters
    The function will return False, if the user's has fewer than 5 characters
    """
    strings = input("Please enter something: " )
    print(check_5_characters_functions(strings)) #This line call the function above to check the user's input

if __name__ == "__main__":
    #Call the main() function
    main()
