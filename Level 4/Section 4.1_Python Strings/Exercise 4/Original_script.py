#Student Name: Jianwei Su
#Date: 04/23/2022
#4.1.4
#Orginal version


def main():
    # Code goes here
    print('\n==========Exercise 4.1.4==========')

    print('------Testing block 1-----')
    print('Display the information.')

    #Prompts the user for name, age (integer), and country of residency.
    try:
        name_a=input('Please enter the name of the resident:')
        age_a=int(input('Please enter an integer of the age and it should be greater than 0:'))
        residency_a=input('Please enter the country of residency:')
        if age_a>0 and name_a!='' and residency_a!='':
            print(name_a+' is '+str(age_a)+' years old and lives in '+residency_a+'.')
        else:
            raise ValueError('Age has to be greater than 0. Name and residency can not be empty.')

    except ValueError as ex:
        print('ValueError exception:', ex, '\nPlease try again.')
        # This will handle other unknown errors
    except Exception as ex:
        print('Unknown error besides ValueError:', ex,'\nPlease try again.')



    print('\n------Testing block 2-----')
    print('Display the information and display the number with one decimal place.')
    # Prompts the user for name, age (with one decimal place), and country of residency.
    try:
        name_b = input('Please enter the name of the resident:')
        age_b = float(input('Please enter a number of the age and it should be greater than 0:'))
        residency_b = input('Please enter the country of residency:')
        if age_b > 0 and name_b!='' and residency_b!='':
            print(name_b+' is '+str(round(age_b,1))+' years old and lives in '+residency_b+'.')
        else:
            raise ValueError('Age has to be greater than 0. Name and residency can not be empty.')

    except ValueError as ex:
        print('ValueError exception:', ex, '\nPlease try again.')
        # This will handle other unknown errors
    except Exception as ex:
        print('Unknown error besides ValueError:', ex,'\nPlease try again.')




    print('\n------Testing block 3-----')
    print('Display the information and display the country name all caps')
    # Prompts the user for name, age (with one decimal place), and country of residency.
    try:
        name_c = input('Please enter the name of the resident:')
        age_c = float(input('Please enter a number of the age and it should be greater than 0:'))
        residency_c = input('Please enter the country of residency:')
        if age_c > 0 and name_c!='' and residency_c!='':
            print(name_c + ' is ' + str(round(age_c, 1)) + ' years old and lives in ' + residency_c.upper() + '.')
        else:
            raise ValueError('Age has to be greater than 0. Name and residency can not be empty.')

    except ValueError as ex:
        print('ValueError exception:', ex, '\nPlease try again.')
        # This will handle other unknown errors
    except Exception as ex:
        print('Unknown error besides ValueError:', ex, '\nPlease try again.')




    print('\n***Program Complete***')

if __name__ == '__main__':
    main()