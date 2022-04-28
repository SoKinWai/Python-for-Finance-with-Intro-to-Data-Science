#Student Name: Jianwei Su
#Date: 04/20/2022
#3.3.1


def main():
    # Code goes here
    print('\n==========Exercise 3.3.1==========')

    #Handle the divide-by-zero case via using exception handling
    try:
        # Takes a numerator and denominator input from the user

        numerator = float(input('Please enter a number for the numerator:'))
        denominator = float(input('Please enter a number for the denominator:'))

        # Output the quotient
        quotient=numerator/denominator

        #We only want to print result if there is no exception
        print('The output quotient:',quotient)

    #This will handle the divide-by-zero case
    except ZeroDivisionError as ex:
        print('ZeroDivisionError exception:',ex,'\nPlease try again.')




    #This is to check if the program still works after exception handling
    print('\nThe program still works after exception handling')

    print('\n***Program Complete***')



if __name__ == '__main__':
    main()