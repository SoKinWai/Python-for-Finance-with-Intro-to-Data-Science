#Student Name: Jianwei Su
#Date: 04/08/2022
#2.1.5


#Asset class
#This class' object takes on the arguments initial_value
class Asset(object):
    #Save an initial asset value upon object initialization

    # Initialize function with initial_value

    def __init__(self, initial_value):
        self.initial_value = initial_value



    # Add getter and setter property functions here
    # Decorators to get and the set values for the instance variable

    # Decorator to create a property function to get the argument initial_value
    @property
    def initial_value(self):
        return self._initial_value

    # Decorator to set the initial_value
    @initial_value.setter
    def initial_value(self, iinitial_value):
        if iinitial_value > 0:
            self._initial_value = iinitial_value  # Set the instance variable init_val from input
        else:
            self._initial_value = '\nError: Please make sure the input of asset‘s initial value is greater than 0.'

    #Create a method that returns a yearly depreciation rate (i.e., 10%).

    #A yearly depreciation rate function.
    #yearly_depre() function, and returns as 0.1 here.
    def yearly_depre(self):
        return 0.1

    #Create a method that calculates the monthly depreciation rate, from the yearly depreciation rate.

    #monthly depreciation rate= yearly depreciation rate/12
    #A monthly depreciation rate function
    # monthly_depre() function.
    def monthly_depre(self):
        return self.yearly_depre()/12

    #Create a method that returns the current value of the asset, for a given period.

    #Current value=initial value * total depreciation
    #total depreciation= (1-monthlyDeprRate)**t
    # current_value() function and it's  to calculate the current value.
    def current_value(self,period):
        return ((1-self.monthly_depre())**period)*self.initial_value