#Student name: Jianwei Su
#Date: 04/06/2022
#1.5.5

def main():
    # Code goes here
    print('\n==========Exercise 1.5.5===========')

    #Create a simple dictionary that has country name as the key and population as the value (country:population)
    #Do this for at least ten countries. Numbers in million.
    country_dic={'India':1380,'China':1439,'USA':331,'Indonesia':273,'Pakistan':220,'Brazil':213,'Nigeria':206,'Bangladesh':165,'Russia':146,'Mexico':129}

    print(country_dic)

    # a. Create code that prompts the user for the name of a country (‘0’ to exit).
    a=input('Please enter the name of the country from the dictionary,0 to exit:')
    while a!='0':
        if a == '':
            a=input('Please enter the name of the country from the dictionary,0 to exit:')
        # i. Display a message to the user that the population is unknown and prompt the user to enter the population.
        # ii. Update the dict with the value provided by the user.
        elif country_dic.get(a)==None:
            try:
                number = float(input('Unknown poplution for this country, please enter the population for this country:'))
                #Here is to make sure user enter the positive population number for  the new country.
                if number>0:
                   country_dic[a]=number
                else:
                    raise ValueError
            except ValueError:
                print("You didn't enter a positive number for this new country.")
        else:
         print(country_dic.get(a))
         a=input('Please enter the name of the country from the dictionary,0 to exit:')

    print("\n")

    # b. Display the final dict once the user exits the loop.
    #Note that the above display will not necessarily be sorted.
    unsort_country=(country_dic.items())



    print("Unsorted dict:")
    for i in unsort_country:
        print(i[0],'has population',i[1])

    print("\n")

    # Modify the code from part b to display sorted by 1) country then 2) population, largest first (Hint: Use the sorted function).

    #Print the dictionary sorted by country
    #sort_country_1 = sorted(country_dic.items() will also work, but it's easier for me to understand via using the following method.
    sort_country_1 = sorted(country_dic.items(), key=lambda x: x[0])
    print("Sorted dict by country:")
    for i in sort_country_1:
        print(i[0], 'has population', i[1])

    print("\n")


    #Print the dictionary sorted by population, largest first
    sort_country_2= sorted(country_dic.items(), key=lambda x: x[1], reverse=True)
    print("Sorted dict by population:")
    for i in sort_country_2:
        print(i[0],'has population', i[1])

    print("\n")

    # d. Use a dict comprehension to create a sub-dictionary with countries of population greater than 1 billion.
    country_sub_dict={country:population for country,population in country_dic.items() if population>1000}
    print("A sub-dictionary with countries of population greater than 1 billion:")
    print(country_sub_dict)



    print('\n***Program Complete***')


if __name__ == '__main__':
    main()
