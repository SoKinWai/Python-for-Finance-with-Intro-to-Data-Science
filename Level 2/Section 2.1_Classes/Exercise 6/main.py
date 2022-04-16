#Student Name: Jianwei Su
#Date: 04/08/2022
#2.1.5


# Importing packages
from asset.asset import Asset



def main():
    # Test Asset class thoroughly.
    print('------Exercise 2.1.6------')
    print('Testing the Asset class\n')

    print('\n------Testing block 1-----')
    print('Test the asset initialization: ')
    # Initialize asset with Asset class
    asset=Asset(300000)
    print('The asset information will be(in US dollars):',asset.initial_value)



    #It will show the yearly depreciation rate and print it on screen
    print('\n------Testing block 2-----')
    print('Test the yearly depreciation rate function:')
    print('The yearly depreciation rate will be:', asset.yearly_depre())

    # It will show the monthly depreciation rate and print it on screen
    print('\n------Testing block 3-----')
    print('Test the monthly depreciation rate function:')
    print('The monthly depreciation rate will be:', asset.monthly_depre())

    # It will show the current value of the asset and print it on screen
    print('\n------Testing block 4-----')
    print('Test the current value of the asset function:')
    #Set the time period t to be 20
    t=20
    print('The current value is:', asset.current_value(t))






    print('\n***Program Complete***')



if __name__ == '__main__':
    main()
