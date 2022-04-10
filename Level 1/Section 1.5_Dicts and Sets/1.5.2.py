#Student name: Jianwei Su
#Date: 04/06/2022
#1.5.2

def main():
    # Code goes here
    print('\n==========Exercise 1.5.2===========')

    #Set 1 should contain the twenty most common male first names in the United States
    set_1={"James","John","Robert","Michael","William","David","Richard","Joseph","Thomas","Charles","Christopher","Daniel","Matthew","Anthony","Donald","Mark","Paul","Steven","Andrew","Kenneth"}

    #Set 2 should contain the twenty most common male first names in Britain
    set_2={"Oliver","Jack","Harry","Jacob","Charlie","Thomas","George","Oscar","James","William","Jake","Connor","Callum","Kyle","Joe","Reece","Rhys","Damian","Damian","Peter","Paul"}

    #a. Find the first names that appear in both sets.
    set_a=set_1.intersection(set_2)
    print("The first names that appear in both sets:",set_a,'\n')

    #b. Find the first names that appear in the United States set, but not Britain.
    set_b=set_1.difference(set_2)
    print("The first names that appear in the United States set, but not Britain:",set_b,'\n')

    #c.Find the first names that appear in the Britain set, but not United States.
    set_c=set_2.difference(set_1)
    print("The first names that appear in the Britain set, but not United States:",set_c,'\n')

    #d. Use a set comprehension to create a subset of names that have more than five letters.
    set_3=set_1.union(set_2)
    set_d={i for i in set_3 if len(i)>5}
    print("A subset of names that have more than five letters:",set_d)

    print('\n***Program Complete***')


if __name__ == '__main__':
    main()
