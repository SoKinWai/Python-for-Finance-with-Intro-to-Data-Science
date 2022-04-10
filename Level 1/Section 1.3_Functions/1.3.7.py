#Student name: Jianwei Su
#Date: 04/05/2022
#1.3.7

#function() function
#This function taks in name, age, and **kwargs as parameters of any type. The function then outputs all values that
#were input, along with their associated variable name (For name and age) or key(For the **kwargs).
def function(name, age=None, **kwargs):
    #Print the name, age and **kwargs from input on screen.
    print(name,age,kwargs.get('State'),kwargs.get('Weight'),kwargs.get('Height'),kwargs.get('HairColor'))
    # Print a line at the end to show the end of printing for the current function call
    print('---------------------------------------------------------------------------')


def main():
    # Code goes here
    print('\n==========Exercise 1.3.7===========')

    #Test the function by using different people and different information.
    function('Ankur',30,State='Illinois')

    function('Adam', 23, State='Iowa',Height=69)

    function('Tim',22,HairColor='Yellow')

    function('David',State='Illinois')

    print('\n***Program Complete***')




if __name__ == '__main__':
     main()