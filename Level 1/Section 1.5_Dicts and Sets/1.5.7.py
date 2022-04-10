#Student name: Jianwei Su
#Date: 04/06/2022
#1.5.7

#Extend the mortgage function to return a dict of address:mortgage.
# For simplicity, address should be a unique six-character string.
#Mortgage_amounts() function
#It returns a dict of 100 adresses and mortages(from 100 to 1000)
def Mortgage_amounts():
    return {'5M2DDY': 710, 'VF2HQB': 936, 'HXFY1S': 156, 'G9RI2P': 743, 'G6F7RD': 203, 'M8NEDX': 293, 'XWC2YS': 909, '4IOYTK': 786, 'A4P68C': 303, 'B0W3IV': 818, 'TO4G11': 115, 'XACWSS': 285, 'HOYI23': 318, 'G1WCJ1': 545, '7MN1IZ': 602, 'QJTGMG': 132, 'YT7SSM': 866, '4YSUIB': 963, 'WWBY98': 323, 'OMZLLC': 874, '7OG0BC': 232, '0Q4HFF': 769, 'A4DENW': 448, '8I1D7G': 751, 'TFJKRW': 320, 'AN3P66': 701, '18NWAO': 928, 'ALRA2M': 784, '35XLC4': 687, '34QO30': 383, 'E88QB8': 493, 'CFCUHP': 369, 'H44ZOW': 452, '5EKY0Q': 969, 'NIL9K7': 144, '8PRCKT': 207, '6KI2GZ': 973, 'C47CNO': 958, 'PPAVOW': 622, 'D1YQ21': 668, 'RCXBI9': 538, 'ZTK80K': 933, 'ED39XC': 766, 'JVFRJ2': 313, 'ILDVJK': 810, 'KLODR6': 902, '3XZ7VK': 459, 'C1D30H': 492, '0NLI1F': 387, '86U1M4': 828, 'Z62UOR': 208, '9I9OVF': 973, 'HQUDUL': 191, 'QI9O52': 944, 'PPKXMU': 356, 'QOMP9S': 334, 'NZ5XQP': 114, 'LVMUYU': 688, 'B2BV9E': 227, '1WUT0Z': 624, '64LY8C': 271, 'V2RWKK': 1000, '1G2CHC': 585, 'EOVGCH': 167, 'CGPJVA': 998, 'Q0ZZI1': 132, 'LJK618': 473, 'VP8C6E': 523, 'V6L2W0': 115, 'DYNQ4X': 797, 'GJL7W4': 535, '1X0PKX': 844, 'B1L4JM': 443, 'O2KBXK': 641, 'NOB9DZ': 269, 'DRVPU2': 936, 'P22YMJ': 476, 'C12LCQ': 867, 'ZARLUJ': 848, '57WNUG': 798, '9RIGHK': 733, '1M5IOA': 512, 'Y1QHFW': 389, 'ZJFVWY': 468, '1ZXPQY': 314, 'ME023D': 418, '3CDL2T': 689, 'T4BVZ7': 538, 'P1Y3HQ': 870, '2NBVFR': 309, 'TZW6UT': 355, 'VZ6BSD': 425, 'XFH7A7': 714, 'P0F1RJ': 554, 'C6KVNS': 873, 'TGCN89': 709, 'HSIZS1': 430, 'JOVZYS': 850, 'QKPV4S': 199, 'O5Q29A': 337}

def main():
    # Code goes here
    print('\n==========Exercise 1.5.7===========')

    # mortgage_amounts has 100 adresses and mortages(from 100 to 1000)
    # Print mortgage_amounts on screen
    mortgage_amounts=Mortgage_amounts()
    print("A function that returns an unsorted list of mortgage amounts,range from 100 to 1000(in thousands):",mortgage_amounts,'\n')

    #a. Provide three separate dicts, filtered the same way as problem 1)
    # Filter amounts below 200 from mortgage_amounts and store them in miniMortgages
    # Print miniMortgages on screen
    miniMortgages = {i:j for i,j in mortgage_amounts.items() if j < 200}
    print("Mini Mortgages(in thousands):", miniMortgages,'\n')

    # Filter amounts between 200 and 467 and store them in standardMortgages
    # Print standardMortgages on screen
    standardMortgages = {a:b for a,b in mortgage_amounts.items() if 200 <= b <= 467}
    print("Standard Mortgages(in thousands):", standardMortgages,'\n')

    # Filter amounts greater than 467 and store them in jumboMortgages
    # Print jumboMortgages on screen
    jumboMortgages = {c:d for c,d in mortgage_amounts.items() if d > 467}
    print("Jumbo Mortgages(in thousands):", jumboMortgages,'\n')

    # b. Modify one value in the jumboMortgages dict. Check the original dict; did it remain intact or change? Why?
    jumboMortgages['5M2DDY']=468
    print('Check the original dict for b:',mortgage_amounts,'\n')

    #Yes, it remained intact. Because it only modifies jumboMortgages. Although jumboMortgages is a subset of mortgage_amounts, jumboMortgages is another
    #dictionary, so when user modifies jumboMortgages, mortgage_amounts remains intact.

    # c. Extract the lists of amounts from each separate dict.
    miniMortgages_list=(list(miniMortgages.values()))
    print("Amounts of Mini Mortgages:",miniMortgages_list,'\n')

    standardMortgages_list=(list(standardMortgages.values()))
    print("Amounts of Standard Mortgages:",standardMortgages_list,'\n')

    jumboMortgages_list=(list(jumboMortgages.values()))
    print("Amounts of Jumbo Mortgages:",jumboMortgages_list,'\n')

    #Modify one value in the miniMortgages list.
    list(jumboMortgages.values())[0]=155
    #jumboMortgages_list[0]=155
    #It changes the first value of jumboMortgages_list's first value to 155

    # Does the miniMortgages dict change?
    print(miniMortgages,'\n')

    #No, it does not change

    #How about the original dict? Why?
    print(mortgage_amounts,'\n')

    #It does not change too.
    #It just changes the list amounts of miniMortgages and it doesn't affect mortgage_amounts and miniMortgages because
    #the list amounts of miniMortgages is independent of mortgage_amounts and miniMortgages.

    print('\n***Program Complete***')






if __name__ == '__main__':
    main()