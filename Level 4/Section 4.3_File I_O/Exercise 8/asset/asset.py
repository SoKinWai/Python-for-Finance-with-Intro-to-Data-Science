#Student Name: Jianwei Su
#Date: 05/05/2022
#4.3.8

import logging

#Class Asset
class Asset(object):

    # init_val is the asset taken out for initially valued at
    # Initialize function with init_val

    def __init__(self, init_val):
        self.init_val = init_val


    #Add getter and setter property functions here
    # Decorators to get and the set values for the instance variable

    # Decorator to create a property function to get the argument init_val
    @property
    def init_val(self):
        return self._init_val

    # Decorator to set the init_val
    @init_val.setter
    def init_val(self, iinit_val):
        if iinit_val>0:
            self._init_val = iinit_val  # Set the instance variable init_val from input
        else:
            logging.error('Something is wrong with the parameter.')
            raise ValueError("Error: Please make sure the input of asset‘s initial value is greater than 0")


    #annualDeprRate method of the Asset class to trigger a not-implemented error.

    #annualDeprRate() function
    #This should return annual deprRate, but raise NotImplementedError is to ensure
    # that no one can directly instantiate an Asset object.
    def annualDeprRate(self,period=None):
        logging.error('This is not implemented.')
        raise NotImplementedError()

    #Create a method that calculates the monthly depreciation rate, from the yearly depreciation rate.

    #monthlyDeprRate() function
    #Returns monthly depreciation rate
    def monthlyDeprRate(self,period=None):
        logging.debug('Monthly depreciation rate is being calculated...')
        return self.annualDeprRate() / 12

    # Create a method that returns the current value of the asset, for a given period.

    # Current value=initial value * total depreciation
    # total depreciation= (1-monthlyDeprRate)**t
    # current_value() function and it's  to calculate the current value.
    def current_value(self,period):
        logging.debug('Current value is being calculated...')
        return ((1-self.monthlyDeprRate())**period)*self.init_val



#Class Car
#Derived class from Asset class
class CarMixin(Asset):
    #Return annual deprRate
    #We choose to return a reasonable constant here
    def annualDeprRate(self, period=None):
        logging.debug('Annual depreciation rate of CarMixin equals 0.25')
        return 0.25

#Derive multiple car types from Car (i.e. Civic, Lexus,Lamborghini, etc.). Give each one a different depreciation rate.

#Class Toyota
#Derived class from Car class
class Toyota(CarMixin):
    # Return annual deprRate
    # We choose to return a reasonable constant here
    def annualDeprRate(self, period=None):
        logging.debug('Annual depreciation rate of Toyota equals 0.1')
        return 0.1

#Class Civic
#Derived class from Car class
class Civic(CarMixin):
    # Return annual deprRate
    # We choose to return a reasonable constant here
    def annualDeprRate(self, period=None):
        logging.debug('Annual depreciation rate of Civic equals 0.15')
        return 0.15

#Class Lexus
#Derived class from Car class
class Lexus(CarMixin):
    # Return annual deprRate
    # We choose to return a reasonable constant here
    def annualDeprRate(self, period=None):
        logging.debug('Annual depreciation rate of Lexus equals 0.22')
        return 0.22

#Class Lamborghini
#Derived class from Car class
class Lamborghini(CarMixin):
    # Return annual deprRate
    # We choose to return a reasonable constant here
    def annualDeprRate(self, period=None):
        logging.debug('Annual depreciation rate of Lamborghini equals 0.22')
        return 0.22

#Create a HouseBase class, derived from Asset.

#Class HouseBase
#Derived class from Asset class
class HouseBase(Asset):
    # Return annual deprRate
    # We choose to return a reasonable constant here
    def annualDeprRate(self, period=None):
        logging.debug('Annual depreciation rate of HouseBase equals 0.006')
        return 0.006

# Derive PrimaryHome and VacationHome from House. Give each one a different depreciation rate

#Note: a vacation home will depreciate slower than a primary home since it is often vacant.

#Class PrimaryHome
#Derived class from HouseBase class
class PrimaryHome(HouseBase):
    # Return annual deprRate
    # We choose to return a reasonable constant here
    def annualDeprRate(self, period=None):
        logging.debug('Annual depreciation rate of PrimaryHome equals 0.005')
        return 0.005

#Class VacationHome
#Derived class from HouseBase class
class VacationHome(HouseBase):
    # Return annual deprRate
    # We choose to return a reasonable constant here
    def annualDeprRate(self, period=None):
        logging.debug('Annual depreciation rate of VacationHome equals 0.004')
        return 0.004