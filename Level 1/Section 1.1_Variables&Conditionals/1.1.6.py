#Student name: Jianwei Su
#Date: 04/05/2022
#1.1.6



def main():
    # Code goes here
    print('\n==========Exercise 1.1.6==========')
    print('***Takes two inputs from the user (using input):The base and height of a triangle.***')

    #try...except ValueError is an condition to check that the user’s input is an int or a float
    #If you do not enter a number, it will appear an error message about you did not enter a number for base or height
    try:
        #float(input(...)) is to convert the number's string to a float number
        Base=float(input('Please enter the base of a triangle(Number should be greater than 0):'))
        Height = float(input('Please enter the height of a triangle(Number should be greater than 0):'))
        print('\n***Check that the input values are valid for the sides of a triangle***')
        if Height > 0 and Base > 0:
            #This is the area function for a triangle.
            Area = Base * Height * 0.5

            #It will print the area for a triangle on screen.
            print('The area is ', Area)
        else:
            #It will print an error message if the user do not enter numbers are greater than 0.
            print('Error: Neither the input base nor height can be less than or equal to 0.')

    except ValueError:
        print("You didn't enter a number for base or height!")


    print('\n***Program Complete***')


if __name__ == '__main__':
    main()