#Student name: Jianwei Su
#Date: 04/05/2022
#1.1.5


def main():
    # Code goes here
    print('\n==========Exercise 1.1.5==========')
    print('***Extend the program from 4) to display the type of the variable that contains the value that the user entered***\n')

    # input() function to take input from the user.
    # Whatever you enter as input, the input function converts it into a string.
    Input_var = input('Please enter:')

    # type() method returns class type of the argument(object) passed as parameter.
    # It prints the input and the type of input on screen.
    print('Variable from input will show:', Input_var, '.\nThe type of the variable:', type(Input_var))


    print('\n***Program Complete***')

if __name__ == '__main__':
    main()