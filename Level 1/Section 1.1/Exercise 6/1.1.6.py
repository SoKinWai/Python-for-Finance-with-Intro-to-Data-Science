#1.1.6
#Create a program that takes two inputs from the user (using input):
#The base and height of a triangle.
#Output should be the area of the triangle.
#As input returns a string in all cases, you’ll need to convert it to a number using float.
#Be sure to have if statements which check that the input values are valid for the sides of a triangle
# (if not, print an error message to the user).


def main():
    #Code goes here
    base=float(input('Please enter the base:'))
    height=float(input('Please enter the height:'))

    if height>0 and base>0:
        area= base*height*0.5
        print('The area is ', area)
    else:
        print('This is an error.')


if __name__ == '__main__':
    main()