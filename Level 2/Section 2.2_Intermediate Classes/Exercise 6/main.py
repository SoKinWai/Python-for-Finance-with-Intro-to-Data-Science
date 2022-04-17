#Student Name: Jianwei Su
#Date: 04/09/2022
#2.2.6

# Import different classes from asset
from asset.asset import *


def main():
    print('------Exercise 2.2.6------')
    print('Testing the Asset class\n')

    print('\n------Testing block 1----')
    print('Test the init function from Asset class:')

    # Initialize asset with Asset class
    asset=Asset(200000)
    print('The asset‘s initial value is', asset.init_val)

    #print('\n------Testing block 2----')
    #print('Test the annualDeprRate() function from Asset class:')
    #It will rasise an error.
    #print('The annual depreciation rate for the asset is:',asset.annualDeprRate())

    print('\n------Testing block 3----')
    print('Test the annualDeprRate() function from Car class:')

    # Initialize the value for Car class
    car = CarMixin(20000)
    print('The annual depreciation rate for the car is', car.annualDeprRate())

    print('\n------Testing block 4----')
    print('Test the annualDeprRate() function from Toyota class:')

    # Initialize the value for Toyota class
    toyota = Toyota(20000)
    print('The annual depreciation rate for the toyota is', toyota.annualDeprRate())

    print('\n------Testing block 5----')
    print('Test the annualDeprRate() function from Civic class:')

    # Initialize the value for Civic class
    civic = Civic(30000)
    print('The annual depreciation rate for the civic is', civic.annualDeprRate())

    print('\n------Testing block 6----')
    print('Test the annualDeprRate() function from Lexus class:')

    # Initialize the value for Lexus class
    lexus = Lexus(50000)
    print('The annual depreciation rate for the lexus is', lexus.annualDeprRate())

    print('\n------Testing block 7----')
    print('Test the annualDeprRate() function from Lamborghini class:')

    # Initialize the value for Lamborghini class
    lamborghini = Lamborghini(80000)
    print('The annual depreciation rate for the lamborghini is', lamborghini.annualDeprRate())

    print('\n------Testing block 8----')
    print('Test the annualDeprRate() function from HouseBase class:')

    # Initialize the value for HouseBase class
    houseBase = HouseBase(300000)
    print('The annual depreciation rate for the houseBase is', houseBase.annualDeprRate())

    print('\n------Testing block 9----')
    print('Test the annualDeprRate() function from PrimaryHome class:')

    # Initialize the value for PrimaryHome class
    primaryHome = PrimaryHome(400000)
    print('The annual depreciation rate for the primaryHome is', primaryHome.annualDeprRate())

    print('\n------Testing block 10----')
    print('Test the annualDeprRate() function from VacationHome class:')

    # Initialize the value for VacationHome class
    vacationHome = VacationHome(500000)
    print('The annual depreciation rate for the vacationHome is', vacationHome.annualDeprRate())






    print('\n***Program Complete***')


if __name__ == '__main__':
    main()