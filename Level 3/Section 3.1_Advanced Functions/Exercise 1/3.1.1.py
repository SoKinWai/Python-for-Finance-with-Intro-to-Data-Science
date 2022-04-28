#Student Name: Jianwei Su
#Date: 04/18/2022
#3.1.1

def main():
    # Code goes here
    print('\n==========Exercise 3.1.1==========')
    print('Create a stored lambda function that calculates the hypotenuse of a right triangle:')

    #A stored lambda function that calculates the hypotenuse of a right triangle
    #It will take base and height as its parameter
    #I will add conditions to make sure base and height are greater than 0
    hypotenuse= lambda base, height:((base)**2+(height)**2)**0.5 if base>0 and height>0 else 'Error: Base and height have to be greater than zero'

    #Test the function with different arguments
    print('Test with arguments 3 and 4 for base and height:',hypotenuse(3,4))
    print('Test with arguments 4 and 3 for base and height:', hypotenuse(4, 3))
    print('Test with arguments 5 and 1 for base and height:', hypotenuse(5, 1))
    print('Test with arguments 3 and 3 for base and height:', hypotenuse(3, 3))
    print('Test with arguments 0.2 and 9 for base and height:', hypotenuse(0.2, 9))

    #Test the function with numbers are not positive
    print('Test with arguments -1 and 1 for base and height:',hypotenuse(-1,1))
    print('Test with arguments 0 and 1 for base and height:', hypotenuse(0, 1))

    print('\n***Program Complete***')






if __name__ == '__main__':
    main()