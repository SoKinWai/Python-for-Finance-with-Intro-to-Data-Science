#Student name: Jianwei Su
#Date: 04/05/2022
#1.3.8

#Method 1
#function_1 function
#This function taks in name, country, and **kwargs as parameters of any type. The function then outputs all values that
#were input, along with their associated variable name (For name and country) or key(For the **kwargs).
def function_1(name, country, **kwargs):
    #Print the input name
    print('name =', name)
    #Print the input country
    print('country =', country)
    #Print the input **kwargs keys and associated values using a for loop to go through each key:value pair
    for key, value in kwargs.items():
     print(key, '=', value)
    #Print a line at the end to show the end of printing for the current function call
    print('---------------------------------------------------------------------------')

#Method 2
#function_2 function
#This function taks in name, country, and **kwargs as parameters of any type. The function then outputs all values that
#were input, along with their associated variable name (For name and country) or key(For the **kwargs).
def function_2(name, country, **kwargs):
    #Print the input name
    print('name =', name)
    #Print the input country
    print('country =', country)
    #Print the input **kwargs keys and associated values using a list comprehension to go through each key:value pair
    [print(key,"=",value) for key,value in kwargs.items()]
    #Print a line at the end to show the end of printing for the current function call
    print('---------------------------------------------------------------------------')

def main():
    # Code goes here
    print('\n==========Exercise 1.3.8===========')

    print('This is function_1 using a for loop method:')
    function_1('Smith', 'USA', state="NV", salary="55k", taxrate=2.00)

    print('This is function_2 using a list comprehension method: ')
    function_2('Smith', 'USA', state="NV", taxrate=2.00,Height=69)

    print('\n***Program Complete***')

if __name__ == '__main__':
    main()