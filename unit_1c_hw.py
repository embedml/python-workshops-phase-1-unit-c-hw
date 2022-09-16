'''
In this file you will fill in each function.

Only edit where it says it is okay to edit. Altering the rest 
of the code may result in false failures. If you have trouble please
reach out to your instructor. :)
'''
import random # We will talk about imports later :)

########## Variables ##########

def assign_1():
    ''' Assign a variable x the integer 5 '''
    x = None
    # Put your code below#
    
    ######################
    return x # This is what will be set to the test for grading

def assign_2():
    '''Assign the variable x the string "Hello NC State"'''
    x = None
    # Put your code below#
    
    ######################
    return x

############ Lists ############

def list_1():
    '''Assign X as a list with the values 3, 4, and 5'''
    x = None
    # Put your code below #
    
    ######################
    return x

def list_2():
    '''Given the list x, use indexing to change the value 3 to the value 7'''
    x = [4, 3, 9]
    # Put your code below #
    
    ######################
    return x

def list_3():
    '''Given the list x, use indexing to change the value 9 to the value 7'''
    x = [4, 3, 9]
    # Put your code below #
    
    ######################
    return x

def list_4():
    '''Given the list x, and list y, assign the indices 2 through 11 of the list x the values of list y! Hint: Use the row operator for lists!
    Don't forget that Python does not include the last digit of the right most number.

    For example, if we have a list b = [0, 1, 2, 3], if we wanted the 0-2 index we must specify b[0:3] (Note, see how the right number is one more greater than the end index we want)
    '''
    x = [0, 0 , 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Put your code below #
    
    ######################
    return x

######### Dictionaries #########

def dict_1():
    '''Assign X as a dict with the keys 0, 1, 2, and values "A", "B", "C", respectively '''
    x = 0
    # Put your code below#
    
    ######################
    return x

def dict_2():
    '''Given dict animal_noises, assign x the value at the key "cat" '''
    animal_noises = {
        "dog" : "bark",
        "cow" : "moo",
        "cat" : "meow",
        "python" : "hsss"
    }
    x = ''
    # Put your code below#
    
    ######################
    return x

def dict_3():
    '''Given dict inventory, assign x the amount of tax for milk '''
    inventory = {
        "butter" : {
            "value" : 2.50,
            "tax" : .10,
        },
        "milk" : {
            "value" : 3.00,
            "tax" : 0.25
        },
        "cheese" : {
            "value" : 8.00,
            "tax" : .70
        }
    }
    x = ''
    # Put your code below#
    
    ######################
    return x 

def list_dict():
    '''
    Give the dictionary colors the keys "warm_colors" and "cool_colors". 
    Give the warm_colors key a value of a list with the values yellow, orange, red.
    Give the cool_colors key a value of a list with the values, green, blue, purple.

    Note: this is case sensitive! 
    '''
    colors = {}
    
    # Put your code below#
    
    ######################

    return colors 

######## if, elif, else ########

def if_practice(x):
    '''
    x is going to be a random number, use if, elif and else to return a value to the tester. 
    
    If, x is 5, it should return a string "X is 5!"
    Else if x is 6, it should return a string "X is 6!"
    Else if x is not 6 or 5, it should return the string "X is not 5 or 6!"
    '''
    # Note: You will have to indent the return statements onces you create your if, elif and else statements

    # Put/alter your code below#
    
    return "X is 5!"
    
    return "X is 6!"
    
    return "X is not 5 or 6!"
    ######################


########## for loops ###########

def for_loop():
    '''
    A list with 400 elements will be given.
    For each entry with a value of 1, replace it with a value of 2

    Hint: Iterate through all elements in the list, then check if the value is a 1, if it is a one use that index of the list
    to write the value as a 2. 

    Hint Hint: Use the variable index to keep track of the index you are on  

    BONUS POINTS (Optional): Use the enumerate function on the list to get index and value https://realpython.com/python-enumerate/

    '''
    x = [0, 1, 0, 3] * 400 # List with pattern [0, 1, 0, 3, 0, 1, 0, 3, ...  3]
    index = 0
    # Put/alter your code below#
    
    ######################
    return x


########## while loops #########

def while_loop():
    '''Create a while loop that will only break if the expression for the while loop evaluates to the number 5'''
    x = None
    '''
    The loop's condition should have the loop stop when the value of x is equal to 5.
    Then, inside the while loop use the code below to generate a new number for x on every single iteration of the loop
        x = random.randint(0, 10) # This should live in the while loop, so you may need to indent it once you have the while loop implemented
    (Note on random.randint(). This will generate an integer between the two values passed in each time it is run.)
    '''
    # Put/alter your code below#
    
    x = random.randint(0, 10) # This should live in the while loop, so you may need to indent it once you have the while loop implemented
    
    ######################
    return x


if __name__ == "__main__":
    '''Run your functions below to see what they are doing by calling print(<function name>())'''
    list_test_4()
    pass