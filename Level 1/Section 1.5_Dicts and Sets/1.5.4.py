#Student name: Jianwei Su
#Date: 04/06/2022
#1.5.4

def main():
    # Code goes here
    print('\n==========Exercise 1.5.4===========')

    #Create a set of mortgage terms, in years (10, 15, 30):
    mortgage_terms={10,15,30}
    print("A set of mortgage terms, in years (10, 15, 30):",mortgage_terms)

    # a. Add a 5-year term to the set.
    mortgage_terms.add(5)
    print("Add a 5-year term to the set:",mortgage_terms)

    #b. Remove the 15-year term from the set.
    mortgage_terms.remove(15)
    print("Remove the 15-year term from the set:",mortgage_terms)

    # c. Remove a 45-year term from the set. What happens?
    #mortgage_terms.remove(45)
    #It will give an error

    #How can you prevent that?
    #we can use .discard() instead of .remove()
    mortgage_terms.discard(45)
    print("Use .discard() to remove a value does not exist in the set:",mortgage_terms)

    print('\n***Program Complete***')


if __name__ == '__main__':
    main()
