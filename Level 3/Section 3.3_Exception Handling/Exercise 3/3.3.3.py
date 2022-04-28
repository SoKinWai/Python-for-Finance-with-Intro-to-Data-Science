#Student Name: Jianwei Su
#Date: 04/20/2022
#3.3.3

#Create a function that calculates the factorial
def factorial(number):

    #Raise an error message if the number is less than 0.
    if number<0:
        raise ValueError('Please try again and enter a positive integer.')

    #Raise an error message if the number type is not int.
    if type(number)!=int:
        raise TypeError('Please try again and make sure the type is int.')
    else:
        result=1
        while number>0:
            result=result*number
            number=number-1
        return result



def main():
    # Code goes here
    print('\n==========Exercise 3.3.3==========')
    print('Using explicit error handling and general error handling (catching all error types)')

    print('\n------Testing block 1-----')
    print('Testing about the ValueError.')
    try:
        #Ask the user to enter a number for factorial calculation
        #I entered -1, 1.3, 'Name' and 4 to test this block.
        number_a=int(input('Please enter a number for factorial calculation:'))

        #These will show the Unknown error message.
        #number_a = float(input('Please enter a number for factorial calculation:'))
        #print('The factorial of an input number:', factorial(number_d))

        # We only want to print result if there is no exception
        print('The factorial of an input number:',factorial(number_a))

    except ValueError as ex:
        print('ValueError exception:',ex,'\nPlease try again.')
        # This will handle other unknown errors
    except Exception as ex:
        print('Unknown error besides a ValueError:', ex, '\nPlease try again.')


    print('\n------Testing block 2-----')
    print('Testing about the TypeError.')
    try:
        # Ask the user to enter a number for factorial calculation
        #This will convert all numbers to float numbers.
        # I entered 1, 3.3, -1 and 'Name' to test this block.
        number_b = float(input('Please enter a number for factorial calculation:'))

        # We only want to print result if there is no exception
        # We will not have any outputs in this block because all numbers will convert to float number.
        print('The factorial of an input number:', factorial(number_b))

        # This will show the Unknown error message.
       # print('The factorial of an input number:', factorial(number_d))

    except TypeError as ex:
        print('TypeError exception:', ex, '\nPlease try again.')
    except ValueError as ex:
        print('ValueError exception:',ex,'\nPlease try again.')
        # This will handle other unknown errors
    except Exception as ex:
        print('Unknown error besides a TypeError or ValueError:', ex, '\nPlease try again.')

    print('\n------Testing block 3-----')
    print('Testing about the NameError.')
    try:
        # Try a undefined number.
        print('The factorial of an input number:', factorial(number_c))
    except NameError as ex:
        print('NameError exception:', ex, '\nPlease try again.')
    except TypeError as ex:
        print('TypeError exception:', ex, '\nPlease try again.')
    except ValueError as ex:
        print('ValueError exception:', ex, '\nPlease try again.')
        # This will handle other unknown errors
    except Exception as ex:
        print('Unknown error besides a TypeError or ValueError or NameError:', ex, '\nPlease try again.')

    print('\n------Testing block 4-----')
    print('Testing about the ZeroDivisionError.')
    try:
        # Ask the user to enter a number for factorial calculation
        # I entered -1, 1.3, 'Name' and 4 to test this block.
        number_d = int(input('Please enter a number for factorial calculation:'))/0

        # We only want to print result if there is no exception
        print('The factorial of an input number:', factorial(number_d))

    except ZeroDivisionError as ex:
        print('ZeroDivisionError exception:', ex, '\nPlease try again.')
    except NameError as ex:
        print('NameError exception:', ex, '\nPlease try again.')
    except TypeError as ex:
        print('TypeError exception:', ex, '\nPlease try again.')
    except ValueError as ex:
        print('ValueError exception:', ex, '\nPlease try again.')
        # This will handle other unknown errors
    except Exception as ex:
        print('Unknown error besides a TypeError or ValueError or NameError or ZeroDivisionError:', ex, '\nPlease try again.')


    print('\n------Testing block 5-----')
    print('Testing about the IOError.')
    try:
        #This testing block is not about the factorial function and it is just to test IOError.
        open('xxx')
    except IOError as ex:
        print('IOError exception:',ex)





    print('\n***Program Complete***')

if __name__ == '__main__':
    main()